#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
__autor__   = 'ERic Bastida'
__project__ = 'Proyecto Final de Carrera - Ingeniería en Informática'

import HUD,  GraphData, GUI_becopter, Vehiculo
from PyQt4 import QtCore, QtGui

class pConexion(QtGui.QMainWindow, GUI_becopter.Ui_MainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        # CONEXION/VARIABLES---------------------------------------------------
        self.btn_conectar.clicked.connect(self.conectarVehiculo)
        self.initIcons()

        #Timer para actualización de datos del vehiculo
        self.timerInfo = QtCore.QTimer()
        self.timerOpt = QtCore.QTimer()

        self.connect(self.timerInfo, QtCore.SIGNAL("timeout()"), self.actualizarInfoVechicle)
        self.connect(self.timerInfo, QtCore.SIGNAL("timeout()"), self.actualizarConsolaVehicle)

    # CONEXION/FUNCIONES---------------------------------------------------
    def initIcons(self):
        "Funcion que escala los iconos al principio en la pestaña de conexion "
        self.gb_infoVehiculo.setEnabled(False)
        if self.lbl_sta.pixmap():
            factorw = 0.1 * self.width()
            factorh = 0.1 * self.height()

            self.lbl_type.setPixmap(self.lbl_type.pixmap().scaled(factorw, factorh))
            self.lbl_gps.setPixmap(self.lbl_gps.pixmap().scaled(factorh, factorh))
            self.lbl_bat.setPixmap(self.lbl_bat.pixmap().scaled(factorw, factorh))
            self.lbl_com.setPixmap(self.lbl_com.pixmap().scaled(factorw, factorh))
            self.lbl_sta.setPixmap(self.lbl_sta.pixmap().scaled(factorh, factorh))
            self.lbl_ok.setPixmap(self.lbl_ok.pixmap().scaled(factorw, factorh))

    def es_iniVehiculo(self):
        "Retorna verdadero si el objeto vehiculo ya se encuentra inicializado"

        try:
            self.qcopter.conectado()
        except:
            # except AttributeError:
            return False
        else:

            return True
        return True

    def conectarVehiculo(self):
        "Comprueba que los datos obtenidos sean distinto del vacio y establece una conexión con el vehículo, en caso contrario termina dicha conexión"

        self.stateInIP(False, "")
        self.stateInPort(False, "")
        IP = self.inIP.text()
        PORT = self.inPort.text()
        IP = str(IP)
        PORT = str(PORT)

        if IP != "" and PORT != "":

            if self.es_iniVehiculo():
                self.qcopter.desconectar()
                self.switchOpciones(False)

                self.btn_conectar.setText("Conectar")
                self.timerInfo.stop()
                self.timerOpt.stop()
                self.actualizarConsolaVehicle(False)
                del self.qcopter


            else:
                # Conexión con el vehículo

                self.qcopter = Vehiculo.Vehiculo(IP, PORT)

                if self.qcopter.conectado():
                    self.set_statusOption(True)  # Se habilitan las opciones del lado izquierdo del programa
                    # self.qcopter.setCallback2Param('heading',self.HUDi)

                    # self.stateBtnConectado(True)
                    # self.infoVehiculo.setPlainText(self.qcopter.obt_parametros())
                    self.btn_conectar.setText("Desconectar")
                    self.timerInfo.start(1000)
                    self.timerOpt.start(700)
                    # Conectamos el vehículo con el HUD, para representarlo graficamente
                    self.qcopter.setCallback2Param('heading', self.QWidgetHud.setHeading)
                    self.qcopter.setCallback2Param('attitude',
                                                   self.PitchRollYaw2HUD)  # Funcion encargada de enviar el pitch, roll y yaw
                    self.qcopter.setCallback2Param('gps_0', self.gps2HUD)
                    self.qcopter.setCallback2Param('battery', self.battery2HUD)
                    self.qcopter.setCallback2Param('rangefinder', self.signal2HUD)
                    self.qcopter.setCallback2Param('location.global_frame', self.extra2HUD)
                    self.qcopter.setCallback2Param('system_status.state', self.status2HUD)

                    self.cargarParametros()
                    self.initListParametros()




        elif IP == "":
            self.stateInIP(True, "Ingrese una IP valida")
        elif PORT == "":
            self.stateInPort(True, "Ingrese un puerto válido")

        self.actualizarConsolaVehicle()

    def actualizarInfoVechicle(self):
        "Esta funcion se encarga de actualizar los iconos de estados."
        ste = self.qcopter.obt_estado()
        width = self.cone.width() * 0.5
        height = self.cone.height() * 0.3

        if ste['gps'] == None:
            ICO = QtGui.QPixmap("../BEcopter/img/conexion/GPSicon/worldwide_war.png")
            sizeICO = QtCore.QSize(int(width * 0.1), int(height))
            ICO = ICO.scaled(sizeICO, QtCore.Qt.KeepAspectRatio)
            self.lbl_gps.setPixmap(ICO)

        elif ste['gps'] == True:
            ICO = QtGui.QPixmap("../BEcopter/img/conexion/GPSicon/worldwide_ok.png")
            sizeICO = QtCore.QSize(int(width * 0.1), int(height))
            ICO = ICO.scaled(sizeICO, QtCore.Qt.KeepAspectRatio)
            self.lbl_gps.setPixmap(ICO)
        else:
            ICO = QtGui.QPixmap("../BEcopter/img/conexion/GPSicon/worldwide_nok.png")
            sizeICO = QtCore.QSize(int(width * 0.1), int(height))
            ICO = ICO.scaled(sizeICO, QtCore.Qt.KeepAspectRatio)
            self.lbl_gps.setPixmap(ICO)

        if ste['battery'] == None:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/Batteryicon/battery_war.png"))
        elif ste['battery'] == True:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/Batteryicon/battery_ok.png"))
        else:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/Batteryicon/battery_nok.png"))

        if ste['ekf'] == None:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/warning.png"))
        elif ste['ekf'] == True:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/success.png"))
        else:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/error.png"))

        if ste['ready'] == True:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/drone_ok.png"))
        else:  # if ste['ready'] == True:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/dronenok_.png"))
        # else:
        #   self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/GPSicon/worldwide_nok.png"))

        if ste['signal'] == None:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/Signalicon/antenna_war.png"))
        elif ste['signal'] == True:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/Signalicon/antenna_ok.png"))
        else:
            self.lbl_gps.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/Signalicon/antenna_nok.png"))

        pass
        #
        # self.lbl_bat.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/Batteryicon/success.png"))
        # self.lbl_com.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/Signalicon/success.png"))
        # self.lbl_sta.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/succes.png"))
        # self.lbl_ok.setPixmap(QtGui.QPixmap("../BEcopter/img/conexion/drone_nok.png"))
        #     if (self.qcopter.conectado()):
        #         # text=""
        #         # for k  in self.qcopter.v.parameters.keys():
        #         #     text += str(k) + str(self.qcopter.v.parameters[k])+"\n"
        #         # print "entor?"
        #         #
        #         # self.infoVehiculo.setPlainText(text)
        #         self.infoVehiculo.setPlainText(self.qcopter.obt_parametros())
        #         # print self.qcopter.obt_parametros()
        #
        # except AttributeError:
        #     self.infoVehiculo.setPlainText("No se ha obtenido información del vehículo")

    def actualizarConsolaVehicle(self, ini=True):
        texto = "BEcopter > Ingrese el IP de la maquina cliente. Esta debe ser la misma que se ingreso en el archivo /etc/default/arducopter perteneciente al vehiculo."
        if ini:
            archivo = open('vehicle.log', 'r')
            texto = archivo.read()
            archivo.close()

        self.logVehiculo.setPlainText(texto)
        self.vScroll = self.logVehiculo.verticalScrollBar()
        self.vScroll.setSliderPosition(self.logVehiculo.blockCount() - 18)

    def limpiarConsolas(self):
        self.logVehiculo.setPlainText(
            "BEcopter > Ingrese el IP de la máquina cliente. Esta debe ser la misma que se ingresó en el archivo /etc/default/arducopter perteneciente al vehículo.")
        self.infoVehiculo.setPlainText("")

    def stateInIP(self, f,
                  text):  # Si f (flag) proviene en true, cambiara el cuadro de texto a un color rojo, en caso contrario lo pondrá por defecto
        if f:
            self.inIP.setStyleSheet("color: rgb(255,0,0); \n background-color: rgb(255, 255, 255); ")
            if text.__len__() > 0:
                self.inIP.setText(text)
        else:
            self.inIP.setStyleSheet("color: rgb(0,0,0); \n background-color: rgb(255, 255, 255); ")
            if text.__len__() > 0:
                self.inIP.setText(text)

    def stateInPort(self, f,
                    text):  # Si f (flag) proviene en true, cambiara el cuadro de texto a un color rojo, en caso contrario lo pondrá por defecto
        if f:
            self.inPort.setStyleSheet("color: rgb(255,0,0); \n background-color: rgb(255, 255, 255); ")
            if text.__len__() > 0:
                self.inPort.setText(text)
        else:
            self.inPort.setStyleSheet("color: rgb(0,0,0); \n background-color: rgb(255, 255, 255); ")
            if text.__len__() > 0:
                self.inPort.setText(text)

