#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from dronekit import connect, APIException, VehicleMode, Command, Vehicle
from pymavlink import mavutil
import logging, time, socket,exceptions


#Configurando los parametros para realizar el log del vehículo.
logging.basicConfig(filename='vehicle.log', level=logging.INFO,
                    format='%(levelname)s: %(asctime)s : %(message)s')
import dronekit,pymavlink

class Vehiculo():

    def __init__(self, ip_host,port_host = None ):
        self.__on = False
        self.__meanRC = 1500
        self.__desvRC = 600
        self.__maxRC = self.__meanRC + self.__desvRC

        self.__modes_manual = [
            'STABILIZE',
            'DRIFT',
            'BRAKE',
            'SPORT',
            'POSHOLD',
            'ACRO',
            'ALT_HOLD',
            'LOITER',
            'CIRCLE'
        ]

        #Los modos comentados han sido probados el 27/08/18 sin ningún exito
        self.__modes = [ 'STABILIZE' ,
                         'LAND',
                         # 'OF_LOITER' ,
                         'RTL' ,
                         'DRIFT'  ,
                         # 'FLIP' ,
                         # 'AUTOTUNE' ,
                         'BRAKE'  ,
                         'GUIDED_NOGPS' ,
                         'AVOID_ADSB' ,
                         # 'POSITION'  ,
                         'SPORT' ,
                         # 'FLOWHOLD'  ,
                         'POSHOLD' ,
                         'AUTO' ,
                         'GUIDED'  ,
                         'ACRO'  ,
                         # 'SMART_RTL'  ,
                         'ALT_HOLD'  ,
                         'LOITER'  ,
                         'CIRCLE'  ,
                         'THROW']


        self.__indx_mode = 0

        try:
            print "Entraste a conectarte con el vehiculo"
            if port_host != None:
                # Connect to the Vehicle (in this case a UDP endpoint)
                source = ip_host + ":" + port_host
                print "A ver: " + source
                self.v = connect(source, wait_ready=True, heartbeat_timeout=10,status_printer=logging.info)  # El parametro wait_ready = True garantiza que connect () no volvera hasta que Vehicle.parameters y la mayoria de los otros atributos predeterminados se hayan rellenado con valores del vehiculo.
            else:#En caso de entrar aquí es porque se ha ingresado un puerto serial
                # print "Entro en puerto"
                source = ip_host
                self.v = connect(ip_host, wait_ready=True, heartbeat_timeout=10,status_printer=logging.info)
            logging.info("Se ha intentado una conexion con la direccion {} de manera exitosa".format(source))

            self.__on = True
            self.descargarMisiones(False)


        # Bad TCP connection
        except socket.error:
            logging.info('No se ha encontrado el vehiculo, por favor compruebe la conexion')
            raise WindowsError('No se ha encontrado el vehiculo, por favor compruebe la conexion')
        # Bad TTY connection
        except exceptions.OSError as e:
            logging.info('No se pudo establecer conexion con el puerto serial')
            raise WindowsError('No se pudo establecer conexion con el puerto serial')
            return
        except APIException:
            logging.info('Se ha excedido el tiempo de espera para establecer la conexion!')
            raise WindowsError('Se ha excedido el tiempo de espera para establecer la conexion!')

        except :
            logging.info('Ah ocurrido un error inesperado. ')
            raise WindowsError('Ah ocurrido un error inesperado. ')

    #------------- Sección Conexión -------------

    def desconectar(self):
        self.v.close()
    def conectado(self):
        if self.__on and self.v.last_heartbeat < 3:
            return True
        else:
            return False

    # ------------- Sección Vehículo -------------

    def obt_estado(self):
            "Funcion que retorna un diccionario con los estados generales del vehículo."
            estados = {'gps': False, 'ekf': False, 'state': False, 'battery' : False, 'ready' : False, 'signal' : False}
            # False -> Error
            # None  -> Warning
            # True  -> Succes


            if self.v.gps_0.fix_type == 2:  # FixType [0-1]->NO, 2 -> 2D YES , 3 -> 3D YES
                estados['gps'] = None
            elif self.v.gps_0.fix_type == 3:
                estados['gps'] = True

            if self.v.battery.level > 20:
                estados['battery'] = True
            elif self.v.battery.level >0 and self.v.battery.level <= 20 or self.v.battery.voltage > 0:
                estados['battery'] = None

            if self.v.is_armable:
                estados['ready'] = True

            if self.v.ekf_ok:
                estados['ekf'] = True

            if self.v.system_status == 'STANDBY':
                estados['state'] = True

            #The observer will be called at the period of the messaging loop (about every 0.01 seconds). Testing on SITL indicates that last_heartbeat averages about .5 seconds, but will rarely exceed 1.5 seconds when connected. Whether heartbeat monitoring can be useful will very much depend on the application.
            if self.v.last_heartbeat > 1 and self.v.last_heartbeat <= 1.5 :
                estados['signal'] = None
            elif self.v.last_heartbeat <= 1 :
                estados['signal'] = True

            return estados

    def prepararVehiculo(self, A_G = True):
        """
        Comprueba el estado del vehículo devolviendo verdadero en caso de estar listo para iniciar las misiones. En caso contrario, utilizar la función estado() para identificar el motivo
            A_G: A = True, este valor le indicara al vehículo que seran realizarán misiones (Automatico)
                 G = False, este valor dará la opción de controlar el vehículo de manera manual
        """

        # mav.mav.command_long_send(mav.target_system, mav.target_component,
        #                           mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1,
        #                           0, 0, 0, 0, 0, 0)
        op = {True : 'AUTO', False:'GUIDED'}

        logVuelo = "\nChequeos pre-vuelo ...\n\n"

        logVuelo += "Estableciendo vehículo en modo " + op[A_G]
        logging.info(logVuelo)
        self.v.mode = VehicleMode(op[A_G])
        self.v.armed = True
        print "Esta listo? ", self.v.armed

        if not self.v.is_armable:
            logVuelo += "Estados: \n GPS: {}, EKF: {}, Estado: {} ".format(self.obt_estado()['gps'],self.obt_estado()['ekf'],self.obt_estado()['state'])
            logVuelo = "No se ha podido iniciar el vuelo ya que uno o varios parámetros no están correctos."
            logging.error(logVuelo)
            return False

        print "Esta listo? ", self.v.armed
        if self.v.armed: #Se realizan varios intentos de asignación en
            logging.info("El vehículo se encuentra listo para iniciar.")
            return True
        else:

            intentos= 1
            while (not self.v.armed) and (intentos < 4) :
                # Copter should arm in GUIDED mode
                self.v.mode = VehicleMode(op[A_G])
                self.v.armed = True
                self.v.armed = True
                self.v.armed = True
                self.v.armed = True
                logging.info("[{}]: Enviando...".format(intentos))
                print self.v.armed , "-> Se grabó!"
                time.sleep(1)
                intentos += 1
                if self.v.armed:
                    logging.info("El vehículo se encuentra listo para iniciar.")
                    print "Esta listo? ", self.v.armed
                    return True
            logging.warning("No se ha podido preparar el vehículo. Compruebe la conexión.")
            # print "naranja"
            return False

    def obt_parametros(self,indx= None):
        "Devuelve en una lista el parametro y valor perteneciente al indicie (indx) seleccionado [Nombre, Valor]. Por defecto se mostraran todos los parametros en formato texto"
        self.parametros = { 0:  ["Firmware V.", "version"],
                            1:  ["Global Frame Latitud", (lambda : self.v.location.global_frame.lat)() , 'location','global_frame','lat'], #Global Frame
                            2:  ["Global Frame Longitud", (lambda : self.v.location.global_frame.lon)(), 'location','global_frame','lon'],
                            3:  ["Global Frame Altitud", (lambda : self.v.location.global_frame.alt)(), 'location','global_frame','alt'],
                            4:  ["Relative Frame Norte",(lambda : self.v.location.local_frame.north)() , 'location','local_frame','lat'], #Relative Frame
                            5:  ["Relative Frame Este",(lambda : self.v.location.local_frame.east)() , 'location','local_frame','east'],
                            6:  ["Relative Frame Abajo",(lambda : self.v.location.local_frame.down)() , 'location','local_frame','down'],
                            7:  ["Pitch", (lambda : self.v.attitude.pitch)(), 'attitude','pitch'],
                            8:  ["Roll", (lambda : self.v.attitude.roll)(), 'attitude','roll'],
                            9:  ["Yaw", (lambda : self.v.attitude.yaw)(), 'attitude','yaw'],
                            10: ["Velocity", (lambda : self.v.velocity)(), 'attitude','pitch'],
                            # @todo Velocity Debería mostrar xyz
                            11: ["Groundspeed", (lambda : self.v.groundspeed)(), 'groundspeed'],
                            12: ["Airspeed", (lambda : self.v.airspeed)(), 'airspeed'],
                            13: ["Bat. Corr.", (lambda : self.v.battery.current)(), 'battery','current'],
                            14: ["Bat. Carga", (lambda : self.v.battery.level)(), 'battery','level'],
                            15: ["Bat. Volt.", (lambda : self.v.battery.voltage)(), 'battery','voltage'],
                            16: ["Last Heartbeat", (lambda : self.v.last_heartbeat)(), 'last_heartbeat'],
                            17: ["Telem. distancia", (lambda : self.v.rangefinder.distance)(), 'rangefinder','distance'],
                            18: ["Telem. voltaje", (lambda : self.v.rangefinder.voltage)(), 'rangefinder','voltage'],
                            19: ["Heading", (lambda : self.v.heading)(), 'heading'],
                            20: ["GPS", (lambda : self.v.gps_0.fix_type)(), 'gps_0','fix_type'],
                            21: ["Estado Sistema", (lambda : self.v.system_status.state)(), 'system_status','state'],
                            22: ["EKF OK?", (lambda : self.v.ekf_ok)(), 'ekf_ok'],
                            23: ["Armado", (lambda : self.v.armed)(), 'armed'],
                            24: ["Armado", (lambda : self.v.armed)(), 'armed'],
                            25: ["Es armable?", (lambda : self.v.is_armable)(), 'is_armable'],
                            26: ["Pos. Horizontal Variance", (lambda : self.v.ekf.pos_horiz_variance)() , 'ekf','pos_horiz_variance'],
                            27: ["Compass Variance", (lambda : self.v.ekf.compass_variance)(), 'ekf','compass_variance'],
                            28: ["Pos. Vertical Variance", (lambda : self.v.ekf.pos_vert_variance)(), 'ekf','pos_vert_variance']
                            # @todo Agregar todos los otros parametros que faltan (Crear clases) 
                           }

        if indx == None:
            info = ""
            n = self.parametros.__len__() #Tamano total de parametros
            for i in range (n):

                info += self.parametros[i][0] + ": " + str(self.parametros[i][1]) +"\n"
            return info
        elif indx == -1: #En caso de necesitar los nombres y valores por separado.
            return self.parametros
        else:
            return self.parametros[indx]


    #------------- Sección Misiones -------------

    # Formato de un comando, según la API de dronekit

    # Command (target_system = El número de identificación del sistema de destino del mensaje (drone, GSC) dentro de la red MAVLink. Defina esto como cero (difusión) cuando se comunica con un ordenador complementario.
    #   target_component = El id de un componente al que el mensaje debe dirigirse dentro del sistema de destino (por ejemplo, la cámara). Ajuste a cero (emisión) en la mayoría de los casos.
    #   seq = El número de secuencia dentro de la misión (el piloto automático rechazará los mensajes enviados fuera de secuencia). Esto debe establecerse en cero, ya que la API establecerá automáticamente el valor correcto al cargar una misión.
    #   frame = El marco de referencia utilizado para los parámetros de ubicación (x, y, z). En la mayoría de los casos esto será mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, que usa el sistema global de coordenadas WGS84 para la latitud y longitud, pero establece la altitud en relación con la posición inicial en metros (altitud de origen = 0).
    #   command = Código identificatorio del comando MAV_CMD_etc,
    #   current = Cero, función no disponible,
    #   autocontinue = Cero, función no disponible,
    #Los siguientes datos, dependerán del tipo de "command" impuesto.
        #   param1,
        #   param2,
        #   param3,
        #   param4,
        #   x,
        #   y,
        #   z
        # )

    # ----- Sección Gestión de misiones -----

    def descargarMisiones(self,temp = True):
        "Devuelve los comandos almacenados en el vehiculo o los temporales"
        if temp:
            return  self.v.commands
        else:
            self.v.commands.download()
            self.v.commands.wait_ready()
            return self.v.commands

    def borrarMisiones(self):
        self.v.commands.clear()

    def enviarMisiones(self):
        self.v.commands.upload()

    def iniciarMisiones(self):
        "Comprueba que el vehículo este en condiciones para iniciar las misiones y las envia"
        flag = False
        if self.v.armed:
#Comprobar si realmente se despega el vehículo.
            self.v.commands.upload()
            return True
        else:
            return False

    def obt_cantMisiones(self):
        return self.v.commands.count

        # ---- Sección Misiones y Comandos en tiempo real ----

    def mis_irPunto(self,lat,long,alt,relativo = True):
        if relativo:
            logging.info("Se carga un Punto con coordenadas relativas: latitud={}, longitud={}, altitud={}".format(lat,long,alt))
            logging.info("Se carga un Punto conPreArm coordenadas relativas: latitud={}, longitud={}, altitud={}".format(lat,long,alt))
            cmd =Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_LOCAL_NED,
                    mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, lat, long, alt)
        else:
            logging.info("Se carga un Punto con coordenadas globales: latitud={}, longitud={}, altitud={}".format(lat, long, alt))

            cmd = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
                          mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, lat, long, alt)

        self.v.commands.add(cmd)

    def mis_holgazanear(self, segundos,lat,long,alt):
        logging.info("Se carga un Holgazanear : segundos={}, latitud={}, longitud={}, altitud={}".format(segundos,lat, long, alt))
        #Command(target_system, target_component, seq, frame, command, current, autocontinue, param1, param2, param3, param4, x, y, z)
        cmd = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
                      mavutil.mavlink.MAV_CMD_NAV_LOITER_TIME, 0,0,segundos, 0, 0, 0, lat, long, alt)
        self.v.commands.add(cmd)

    def mis_volverInicio(self):
        logging.info("Se carga un volver a inicio.")
        cmd = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
                      mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0,0,0, 0, 0, 0, 0, 0, 0)
        self.v.commands.add(cmd)

    def mis_aterrizar(self,lat, long, alt):
        logging.info("Se carga un aterrizar relativo Relativo: latitud={}, longitud={}, altitud={}".format(lat, long, alt))
        cmd = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
                      mavutil.mavlink.MAV_CMD_NAV_LAND, 0,0,0, 0, 0, 0, lat, long, alt)
        self.v.commands.add(cmd)

    def mis_despegar(self,altura):
        logging.info("Se carga un despegar relativo: Altura = {}".format(altura))
        cmd = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
                      mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0,0,0, 0, 0, 0, 0, 0, altura)
        self.v.commands.add(cmd)


    def velocidad(self,v_x, v_y, v_z, duracion):
        """
        Velocidades realizadas en el frame NED (North, East, Down) mediante el ingreso de un vector
        """
        msg = self.v.message_factory.set_position_target_local_ned_encode(
            0,  # time_boot_ms (not used)
            0, 0,  # target system, target component
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,  # frame
            0b0000111111000111,  # type_mask (only speeds enabled)
            0, 0, 0,  # x, y, z positions (not used)
            v_x, v_y, v_z,  # x, y, z velocity in m/s
            0, 0, 0,  # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
            0, 0)  # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

        # send command to vehicle on 1 Hz cycle
        for x in range(0, duracion):
            self.v.send_mavlink(msg)
            time.sleep(1)

    def despegar(self,altura):
        "Arma el vehiculo y luego vuela a la altura estipulada"

        """Poll on Vehicle.is_armable until the vehicle is ready to arm.
            Set the Vehicle.mode to GUIDED
            Set Vehicle.armed to True and poll on the same attribute until the vehicle is armed.
            Call Vehicle.simple_takeoff with a target altitude.
            Poll on the altitude and allow the code to continue only when it is reached."""

        # print("Taking off!")
        self.v.simple_takeoff(altura)  # Take off to target altitude

        # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
        #  after Vehicle.simple_takeoff will execute immediately).
        while True:
            # print(" Altitude: ", self.v.location.global_relative_frame.alt)
            if self.v.location.global_relative_frame.alt >= altura * 0.95:  # Trigger just below target alt.
                # print("Reached target altitude")
                break
            time.sleep(1)

    def yaw(self, grados, sentido = 1,relativo=True):
        """
        Point (yaw) the nose of the vehicle towards a specified heading.
        El frente del vehiculo apunto a la direccion especifica, segun los grados y el sentido (sentido antihorario (-1) o sentido horario (1))

        El parametro relavito si es 0 (absoluto) toma como referencia el sistema NED (north, East, Down). En cambio,
        si es 1 (relativo) toma como referencia la direccion actual del vehiculo.
        """
        # create the CONDITION_YAW command using command_long_encode()
        msg = self.v.message_factory.command_long_encode(
            0, 0,  # target system, target component
            mavutil.mavlink.MAV_CMD_CONDITION_YAW,  # command
            0,  # confirmation
            grados,  # param 1, yaw in degrees
            0,  # param 2, yaw speed deg/s
            sentido,  # param 3, direction -1 ccw, 1 cw
            relativo,  # param 4, relative offset 1, absolute angle 0
            0, 0, 0)  # param 5 ~ 7 not used
        # send command to vehicle
        self.v.send_mavlink(msg)

    def apuntar_cam(self,location):
        """
        Este comando es utilizado para mover el gimbal que sujeta a la camara a un punto determinado

        """
        # create the MAV_CMD_DO_SET_ROI command
        msg = self.v.message_factory.command_long_encode(
            0, 0,  # target system, target component
            mavutil.mavlink.MAV_CMD_DO_SET_ROI,  # command
            0,  # confirmation
            0, 0, 0, 0,  # params 1-4
            location.lat,
            location.lon,
            location.alt
        )
        # send command to vehicle
        self.v.send_mavlink(msg)

    # def goto(self, dNorth, dEast, gotoFunction):
    #     """
    #     Moves the vehicle to a position dNorth metres North and dEast metres East of the current position.
    #
    #     The method takes a function pointer argument with a single `dronekit.lib.LocationGlobal` parameter for
    #     the target position. This allows it to be called with different position-setting commands.
    #     By default it uses the standard method: dronekit.lib.Vehicle.simple_goto().
    #
    #     The method reports the distance to target every two seconds.
    #     """
    #
    #     currentLocation = vehicle.location.global_relative_frame
    #     targetLocation = get_location_metres(currentLocation, dNorth, dEast)
    #     targetDistance = get_distance_metres(currentLocation, targetLocation)
    #     gotoFunction(targetLocation)
    #
    #     # print "DEBUG: targetLocation: %s" % targetLocation
    #     # print "DEBUG: targetLocation: %s" % targetDistance
    #
    #     while self.v.mode.name == "GUIDED":  # Stop action if we are no longer in guided mode.
    #         # print "DEBUG: mode: %s" % vehicle.mode.name
    #         remainingDistance = self.get_distance_metres(self.v.location.global_relative_frame, targetLocation)
    #         print("Distance to target: ", remainingDistance)
    #         if remainingDistance <= targetDistance * 0.01:  # Just below target, in case of undershoot.
    #             print("Reached target")
    #             break;
    #         time.sleep(2)
    def velocidad_ned(self, v_x, v_y, v_z, duracion):
        """
        Move vehicle in direction based on specified velocity vectors and
        for the specified duration.

        This uses the SET_POSITION_TARGET_LOCAL_NED command with a type mask enabling only
        velocity components
        (http://dev.ardupilot.com/wiki/copter-commands-in-guided-mode/#set_position_target_local_ned).

        Note that from AC3.3 the message should be re-sent every second (after about 3 seconds
        with no message the velocity will drop back to zero). In AC3.2.1 and earlier the specified
        velocity persists until it is canceled. The code below should work on either version
        (sending the message multiple times does not cause problems).

        See the above link for information on the type_mask (0=enable, 1=ignore).
        At time of writing, acceleration and yaw bits are ignored.
        """
        msg = self.v.message_factory.set_position_target_local_ned_encode(
            0,  # time_boot_ms (not used)
            0, 0,  # target system, target component
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,  # frame
            0b0000111111000111,  # type_mask (only speeds enabled)
            0, 0, 0,  # x, y, z positions (not used)
            v_x, v_y, v_z,  # x, y, z velocity in m/s
            0, 0, 0,  # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
            0, 0)  # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

        # send command to vehicle on 1 Hz cycle
        for x in range(0, duracion):
            self.v.send_mavlink(msg)
            #time.sleep(1)


    def holgazanear(self):

        msg = self.v.message_factory.command_long_encode(
            0, 0,  # target_system, target_component
            mavutil.mavlink.MAV_CMD_NAV_LOITER_TIME,  # command
            0,    # confirmation
            0,    # param 1, Empty
            0,    # param 2, Empty
            0,    # param 3, Empty
            0,  # param 4, Target latitude. If zero, the vehicle will loiter at the current latitude.
            0,  #Target longitude. If zero, the vehicle will loiter at the current longitude.
            0)  #	Target altitude. If zero, the vehicle will loiter at the current altitude.

        # send command to vehicle
        self.v.send_mavlink(msg)

    def volverInicio(self):
        self.v.mode = VehicleMode("RTL")
        self.v.flush()

    def aterrizar(self):
        self.velocidad_ned(0,0,1,1)


    def velocidad_glo(self, v_x, v_y, v_z, duracion):
        """
        Move vehicle in direction based on specified velocity vectors.

        This uses the SET_POSITION_TARGET_GLOBAL_INT command with type mask enabling only
        velocity components
        (http://dev.ardupilot.com/wiki/copter-commands-in-guided-mode/#set_position_target_global_int).

        Note that from AC3.3 the message should be re-sent every second (after about 3 seconds
        with no message the velocity will drop back to zero). In AC3.2.1 and earlier the specified
        velocity persists until it is canceled. The code below should work on either version
        (sending the message multiple times does not cause problems).

        See the above link for information on the type_mask (0=enable, 1=ignore).
        At time of writing, acceleration and yaw bits are ignored.
        """
        msg = self.v.message_factory.set_position_target_global_int_encode(
            0,  # time_boot_ms (not used)
            0, 0,  # target system, target component
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,  # frame
            0b0000111111000111,  # type_mask (only speeds enabled)
            0,  # lat_int - X Position in WGS84 frame in 1e7 * meters
            0,  # lon_int - Y Position in WGS84 frame in 1e7 * meters
            0,  # alt - Altitude in meters in AMSL altitude(not WGS84 if absolute or relative)
            # altitude above terrain if GLOBAL_TERRAIN_ALT_INT
            v_x,  # X velocity in NED frame in m/s
            v_y,  # Y velocity in NED frame in m/s
            v_z,  # Z velocity in NED frame in m/s
            0, 0, 0,  # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
            0, 0)  # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

        # send command to vehicle on 1 Hz cycle
        for x in range(0, duracion):
            self.v.send_mavlink(msg)
            time.sleep(1)

    def setCallback2Param(self,atributo,funcion):
        "Esta función es un Listener, cuando el atributo seleccionado sufra algún tipo de cambio activará a la función ingresada"
        self.v.add_attribute_listener(atributo,funcion)
    def removeCallback(self,nom_atrib,func):
        "Elimina de la lista de escucha según el atributo la funcion asociada"
        self.v.remove_attribute_listener(nom_atrib,func)

    # @v.on_message('STATUSTEXT')
    # def my_method(self, name, msg):
    #     print name , msg
    # The status has a state property with one of the following values:
    #
    # UNINIT: Uninitialized system, state is unknown.
    # BOOT: System is booting up.
    # CALIBRATING: System is calibrating and not flight-ready.
    # STANDBY: System is grounded and on standby. It can be launched any time.
    # ACTIVE: System is active and might be already) airborne. Motors are engaged.
    # CRITICAL: System is in a non-normal flight mode. It can however still navigate.
    # EMERGENCY: System is in a non-normal flight mode. It lost control over parts or over the whole airframe. It is in mayday and going down.
    # POWEROFF: System just initialized its power-down sequence, will shut down now.
    # velocity

    def canal(self,id,value):
        """
        Funcion encargada de enviar la informacion por los canales (los mismos que se utilizan para el RC)
        :param id: Identificacion del canal a enviar la info
        :param value: Valor entre [-1,1]
        """
        #@TODO: tener en cuenta que cantidad de canales son necesarios
        if 0 < id <= 8 :
            # print "Channel : ", id, ". Value: ", value
            v = self.__desvRC*value + self.__meanRC
            if v < 0:
                v = 0
            if v > self.__maxRC:
                v = self.__maxRC

            self.v.channels.overrides[str(id)] = v


    def probandoARMED(self):
        self.v.mode = VehicleMode('GUIDED')
        self.v.armed = True
        print "\nEstado cambiado a True? = ", self.v.armed
        if (self.v.armed == False):
            print "Probando con la otra opcion...."

            # msg = self.v.message_factory.command_long_encode(self.v._master.target_system, self.v._master.target_component,
            #                                       mavutil.mavlink.MAV_CMD_DO_SET_MODE, 128,
            #                                       128,
            #                                       0, 0, 0, 0, 0, 0)
            msg = self.v.message_factory.set_mode_encode(
                0,  # time_boot_ms (not used)
                0, 0,  # target system, target component
                mavutil.mavlink.MAV_CMD_DO_SET_MODE,
                0,
                128,
                0, 0, 0, 0, 0, 0)

            # send command to vehicle on 1 Hz cycle
            for x in range(0, 3):
                self.v.send_mavlink(msg)
                time.sleep(1)
        self.v.armed = True
        print "\nAhora? = ", str(self.v.armed)

    def changeMode(self,name=None):
        """
        Funcion encargada de cambiar el modo del vehiculo
            :param name : Contiene el nombre PERTENECIENTE  a los modos que puede cambiar el vehiculo. En caso de no ingresarlo se establecera el siguiente modo con respecto al actual
        """
        # try:


        if name in self.__modes:
            print "Nombre : ", name
            #En caso de que exista el modo al cual asignar, se obtiene su ID
            new_mode =  name
        else:

            #En caso contrario, se obtiene el nombre del modo actual y se asigna el siguiente al mismo.
            mode = self.v.mode
            indx = self.__modes.index(mode)
            # print "Modo actual ", mode
            #Adicionalmente, si se quiere obtener el modo que pertenece a la ultima + 1 posciion, se retorna el primero
            if indx < self.__modes.__len__()-1:

                new_mode = self.__modes[indx +1 ]
                # print "Primero ", new_mode
            else:
                new_mode = self.__modes[0]
                # print "Segundo ", new_mode

        # logging.info("Cambio de modo: " + name)
        # print "/////Cambio de modo a : " , new_mode
        self.v.mode = VehicleMode(new_mode)


        # except:
        #     AttributeError("Error en changeMode", "Hubo un error en intentar cambiar el modo de vuelo del vehículo")




    def toogleARM_DISARM(self):
        # Arm
        # master.arducopter_arm() or:
        logging.info("Se intenta cambiar ARM/DISARMED")

        print self.v.ekf_ok

        print "ARMADO : ",self.v.armed
        if self.v.armed:
            self.v.armed = False
            print "Armado->Desarmado*"

        else:
            print "Estatus" , self.v.ekf.__str__()
            self.v.armed = True

            print "Desarmado->Armado*"


    def manualModes(self):
        return self.__modes_manual






if __name__ == "__main__":
    vehicle = Vehiculo("192.168.1.13","14550")

    print "Estado del vehiculo : ", vehicle.v.system_status
    vehicle.v.mode = VehicleMode('GUIDED')
    print "Alojaa" , vehicle.v.ekf.pos_horiz_variance
    time.sleep(3)
    print "ALoja 2 " , vehicle.v.ekf.compass_variance
    time.sleep(3)

    print vehicle.v.mode



