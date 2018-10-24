#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
__autor__ = 'ERic Bastida'
__project__ = 'Proyecto Final de Carrera - Ingeniería en Informática'

import sys
import Parametros
import Joystick
import Vehiculo
import pygame
import GUI_becopter
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL
import HUD
import GraphData_v2
import logging

from pyqtgraph.Qt import QtGui, QtCore


logging.basicConfig(filename='BEcopter.log', level=logging.INFO,
                    format='%(levelname)s: %(asctime)s : %(message)s')



class Capturadorr(QThread):
    "Clase encargada de capturar por background los comandos que se envian del Joystick "
    condicion_para_capturar = False

    def __init__(self,parent):
        super(Capturadorr, self).__init__(parent)
        # QThread.__init__(parent)

    def capturing(self,run):
        self.condicion_para_capturar = run

    def __del__(self):
        self.wait()
        self.quit()
        self.exit(0)


    def capturarComandos(self):
        try:

            while  True :

                if self.condicion_para_capturar:
                    eventos = pygame.event.get()

                    for e in eventos:

                        if e.type == 7: #e.type == 7, es un código de tipo joymotion
                            self.emit(SIGNAL('mostrarEje(int,float)'), e.axis, e.value)
                            self.emit(SIGNAL('sendManualCmd(int,float,bool)'), e.axis + 12, e.value, True)
                        if e.type == 10: #Es de tipo JoyButtonDown
                            self.emit(SIGNAL('sendManualCmd(int,float,bool)'), e.button, 1.0, False)

                # time.sleep(0.5)

        except:

            WindowsError("Error de comando", "Ah ocurrido un error al enviar los comandos" )



class BEcopter(QtGui.QMainWindow, GUI_becopter.Ui_MainWindow):  # Creo una clase que herede de QtWidgets.QMainWindow y GUI_becopter, que es el tipo de ventana que utilizamos

    # @TODO: Crear las clases para estas estructuras
    opcionesJoyBtn = {
        # ID -> [Action, IsShowing , LastPosition]
        0: ["Aterrizar", False, 0],
        1: ["Cambiar modo", False, 1],
        2: ["Volver al Inicio", False, 2],
        3: ["Estabilizarse", False, 3],
        4: ["ARMAR/DESARMAR", False, 4],
        5: ["", False, 5]
    }

    opcionesJoyEje = {
        0: ["ROLL", False, 0],
        1: ["PITCH", False, 1],
        2: ["THROTTLE", False, 2],
        3: ["YAW", False],
        4: ["", False]
    }

    ejesInvertidos = {
        0: False,
        1: False,
        2: False,
        3: False
    }
    # Variable temporal para los QComboBox -> ComboBox
    lastAction = ""

    def __init__(self,
                 parent=None):  # El segundo parametro indica que esta ventana o dialogo es el padre y no depende de nadie.

        QtGui.QWidget.__init__(self, parent)

        # Aqui conectamos la interfaz grafica que se genero con el Qt Designer
        self.setupUi(self)

        self.btn_ayud.clicked.connect(self.mostrar0)
        self.btn_Inic.clicked.connect(self.mostrar1)
        self.btn_Cone.clicked.connect(self.mostrar2)
        self.btn_coma.clicked.connect(self.mostrar3)
        self.btn_conf.clicked.connect(self.mostrar4)

        # Timer para actualización de datos del vehiculo
        self.timerInfo = QtCore.QTimer()
        self.timerOpt = QtCore.QTimer()

        self.todo.setCurrentIndex(0)  # Se muestra la pestaña de ayuda.
        self.ini_Tabs.setCurrentIndex(0)

        # Habilitar las opciones  - DEBUGGING
        self.set_statusOption(False)

        # AYUDA-------------------------------------------------------------

        self.webView.setUrl(QtCore.QUrl("doc/index.html"))

        # INICIO/VARIABLES---------------------------------------------------
        self.btn_empezar.clicked.connect(self.IniciarMis)
        # Botón "Descargar Misiones" (Obtiene las misiones del vehículo y las representa en una tabla
        self.btn_descargar_mis.clicked.connect(self.descargarMisiones2Tabla)
        # Botón que carga las misiones en forma temporal dentro del objeto vehículo.
        self.btn_enviar_mis.clicked.connect(self.enviarMisiones)

        self.ini_Tabs.currentChanged.connect(self.displayDataGraph)
        # Verision con matplotlib
        # self.Graph = GraphData.Grafico(self.parentWidget())

        # Version con pyqtgraph
        self.Graph = GraphData_v2.Grafico2(self)
        self.layoutGraph.addWidget(self.Graph)
        self.layoutGraph.setStretch(0, 1)
        self.layoutGraph.setStretch(1, 3)

        #   <Botonera

        # Parametros que se ven al inicicar la aplicación
        # En caso de necesitar ver que significa cada codigo ir a la clase vehiculo

        self.paramShow = [3, 1, 2, 19, 16, 11, 20, 22]
        self.listParam = []

        # @TODO: Crear clase botonera

        self.botones = [self.B1_btn, self.B2_btn, self.B3_btn, self.B4_btn, self.B5_btn, self.B6_btn, self.B7_btn,
                        self.B8_btn]
        self.lblbotones = [self.B1_lbl, self.B2_lbl, self.B3_lbl, self.B4_lbl, self.B5_lbl, self.B6_lbl,
                           self.B7_lbl, self.B8_lbl]



        #    Botonera>


        self.icoBecopter = QtGui.QIcon()
        self.icoBecopter.addPixmap(QtGui.QPixmap("img/BEcopter.png"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)

        self.misOpciones = {0: "", 1: "Punto Objetivo", 2: "Holgazanear", 3: "Volver al inicio", 4: "Aterrizar",
                            5: "Despegar"}#, 6: "Cambiar Yaw"}
        self.human = True
        # En pestaña de INICIO - Boton "Agregar Misión"
        self.btn_agregar_mis.clicked.connect(self.agregarMision)

        # Funciones que deshabilitan/habilitan las opciones de navegación cuando el vehículo esta conectado o no
        self.grupoBotones.setEnabled(False)
        self.grupoEjes.setEnabled(False)

        self.displayHUD()
        self.proporcionHUD()

        self.initStyleTable()

        self.styleComboBox = """

QComboBox {
    border: 1px solid #6D6D6D;
    border-radius: 1px;
    padding: 5px 5px 5px 5px;
    min-width: 6em;
color: white;
}

QComboBox:editable {
    background: black;
    background-color: black;
 }

 QComboBox:!editable, QComboBox::drop-down:editable {
      background:black;

 }


 /* QComboBox gets the \ on\  state when the popup is open */
 QComboBox:!editable:on, QComboBox::drop-down:editable:on {
     background: black;
 }

 QComboBox:on { /* shift the text when the popup opens */
     padding-top: 3px;
     padding-left: 4px;
 }

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 50px;

    border-left-width: 1px;
    border-left-color: 6D6D6D;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

 QComboBox::down-arrow {
     image: url(img/DropDownArrow.png);
     width: 4px;
     height: 4px;
     background: #0070FF
 }

 QComboBox::down-arrow:on { /* shift the arrow when popup is open */
     top: 1px;
     left: 1px;
 }

/*Formato de item de la lista desplegable*/

QComboBox QAbstractItemView
{
    border: 1px solid black;
    color: white;
    background: black;
    selection-background-color:  rgb(5, 113, 255);
}
"""

        self.connect(self.timerInfo, QtCore.SIGNAL("timeout()"), self.actualizarBotonera)

        # CONEXION/VARIABLES---------------------------------------------------
        self.btn_conectar.clicked.connect(self.conectarVehiculo)
        self.initIcons()

        self.connect(self.timerInfo, QtCore.SIGNAL("timeout()"), self.actualizarInfoVechicle)
        self.connect(self.timerInfo, QtCore.SIGNAL("timeout()"), self.actualizarConsolaVehicle)

        # COMANDO/VARIABLES---------------------------------------------------
        pygame.init()
        self.initOpJoy()
        self.manualMode = False
        self.btn_coma.clicked.connect(self.showJoysticks)
        self.dispConectados.currentIndexChanged.connect(self.selectJoy)
        self.dispConectados.addCallback(self.checkJoysticks)
        self.dispConectados.setItemText(0, " ")

        self.opA0.currentIndexChanged.connect(self.mapeoJoystick)
        self.opA1.currentIndexChanged.connect(self.mapeoJoystick)
        self.opA2.currentIndexChanged.connect(self.mapeoJoystick)
        self.opA3.currentIndexChanged.connect(self.mapeoJoystick)

        self.cone_op1.currentIndexChanged.connect(self.mapeoJoystick)
        self.cone_op2.currentIndexChanged.connect(self.mapeoJoystick)
        self.cone_op3.currentIndexChanged.connect(self.mapeoJoystick)
        self.cone_op4.currentIndexChanged.connect(self.mapeoJoystick)

        self.invA0.stateChanged.connect(self.mapeoJoystick)
        self.invA1.stateChanged.connect(self.mapeoJoystick)
        self.invA2.stateChanged.connect(self.mapeoJoystick)
        self.invA3.stateChanged.connect(self.mapeoJoystick)
        # Se inicializa un objeto de tipo hilo para que se encargue de capturar los comandos en background
        self.capturador = Capturadorr(self)
        # Se conectan las señales que puede emitir el objeto capturador con las funciones que tenemos en esta clase
        self.connect(self.capturador, SIGNAL('mostrarEje(int,float)'), self.mostrarEje)
        self.connect(self.capturador, SIGNAL('sendManualCmd(int,float,bool)'), self.sendManualCmd)

        self.capturador.start()

        # CONFIGURACION/VARIABLES---------------------------------------------------
        self.btnGuardarParam.clicked.connect(self.guardarParametros)
        self.btnRestaurarParam.clicked.connect(self.cargarParametros2)

        self.ListGP = []
        self.parametros = dict()

        # ------------------  GENERAL Y CONTORNO     ------------------

    def closeEvent(self, *args, **kwargs):
        "Funcion ejecutada una vez que cerremos toda la aplicacion"
        print "ALoja"


        self.capturador.capturing(False)

        self.capturador.exit(0)


        if hasattr(self, 'Joystick'):
            if self.Joystick.obt_estado():
                self.Joystick.saveMap()
                del self.Joystick
        if hasattr(self, 'qcopter'):
            self.qcopter.v.close()
            del self.qcopter

    def mostrar0(self):
        self.todo.setCurrentIndex(0)

    def mostrar1(self):
        self.todo.setCurrentIndex(1)

    def mostrar2(self):
        self.todo.setCurrentIndex(2)

    def mostrar3(self):
        self.todo.setCurrentIndex(3)

    def mostrar4(self):
        self.todo.setCurrentIndex(4)

    def mostrar5(self):
        self.todo.setCurrentIndex(5)

    def switchOpciones(self, bandera):
        "Esta función habilita o desabilita las opciones que son necesarias cuando el vehiculo se encuentra conectado o no"
        self.set_statusOption(bandera)
        # self.set_statusDisplay(bandera)
        self.gb_infoVehiculo.setEnabled(bandera)
        if not (bandera):
            self.limpiarConsolas()

    def set_statusOption(self, status):
        if status:
            self.btn_Inic.setMaximumWidth(16777215)
            self.btn_Inic.setMaximumHeight(16777215)

            self.btn_conf.setMaximumWidth(16777215)
            self.btn_conf.setMaximumHeight(16777215)
        else:
            self.btn_Inic.setMaximumWidth(0)
            self.btn_Inic.setMaximumHeight(0)

            # self.btn_sens.setMaximumWidth(0)
            # self.btn_sens.setMaximumHeight(0)

            self.btn_conf.setMaximumWidth(0)
            self.btn_conf.setMaximumHeight(0)


    # INICIO/FUNCIONES-----------------------------------------------------------------------------
    def initStyleTable(self):

        self.tablaMisiones.setRowCount(0)
        self.tablaMisiones.setColumnCount(7)
        a = self.tablaMisiones.horizontalHeader()
        a.setResizeMode(True)

    def opcionesMis(self, indx):
        "Según el tipo de misión elegida en el QcomboBox se rellenan las siguientes celdas con un hint text de los parametros a ingresar."
        try:
            if (self.human):
                # i= self.tablaMisiones.indexAt(self.comboMis.pos())
                clickme = QtGui.QApplication.focusWidget()
                i = self.tablaMisiones.indexAt(clickme.pos())
                fila = i.row()
                if fila == -1:
                    return
                # Se borra la info anterior
                self.tablaMisiones.cellWidget(fila, 2).setPlaceholderText("")
                self.tablaMisiones.cellWidget(fila, 3).setPlaceholderText("")
                self.tablaMisiones.cellWidget(fila, 4).setPlaceholderText("")
                self.tablaMisiones.cellWidget(fila, 5).setPlaceholderText("")
                # Tipos de misiones
                # {0: "", 1: "Punto Objetivo", 2: "Holgazanear", 3: "Volver al inicio", 4: "Aterrizar", 5: "Despegar",6: "Cambiar Yaw"}

                for i in range(2, 5):
                    line = QtGui.QLineEdit()
                    line.setStyleSheet("background-color: transparent;\ncolor: rgba(255,255,255,255);")
                    line.setPlaceholderText("")
                    # line.setInputMask("00")
                    self.tablaMisiones.setCellWidget(fila, i, line)

                if indx == 1 or indx == 4:
                    self.tablaMisiones.cellWidget(fila, 2).setPlaceholderText("Latitud")
                    self.tablaMisiones.cellWidget(fila, 3).setPlaceholderText("Longitud")
                    self.tablaMisiones.cellWidget(fila, 4).setPlaceholderText("Altitud")
                elif indx == 2:
                    self.tablaMisiones.cellWidget(fila, 2).setPlaceholderText("Tiempo [segundos]")
                    self.tablaMisiones.cellWidget(fila, 3).setPlaceholderText("Latitud")
                    self.tablaMisiones.cellWidget(fila, 4).setPlaceholderText("Longitud")
                    self.tablaMisiones.cellWidget(fila, 5).setPlaceholderText("Altitud")
                elif indx == 5:
                    self.tablaMisiones.cellWidget(fila, 2).setPlaceholderText("Altitud")
                elif indx == 6:
                    # grados, sentido = 1, relativo = True
                    self.tablaMisiones.cellWidget(fila, 2).setPlaceholderText("Grados")
                    self.tablaMisiones.cellWidget(fila, 3).setPlaceholderText("Sentido")
        except:

            QtGui.QMessageBox.critical(self, "No estas conectado", sys.exc_info()[0])

    def eliminarMision(self):
        btn = QtGui.QApplication.focusWidget()

        self.tablaMisiones.removeRow(self.tablaMisiones.indexAt(btn.pos()).row())

        # ------------ [Subtab] Graficos  ------------

    def displayHUD(self):

        "Graficos de los atributos del vehiculo"

        # self.horizontalLayout_28.addStretch(1)

        self.QWidgetHud = HUD.GLWidget(self.DatosGrafica)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QWidgetHud.sizePolicy().hasHeightForWidth())
        self.QWidgetHud.setSizePolicy(sizePolicy)
        self.QWidgetHud.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.QWidgetHud.setObjectName("QWidgetHud")

        self.splitter.addWidget(self.QWidgetHud)

    def proporcionHUD(self, event=None):
        "Funcion unicamente para mantener proporcionado el tamaño del HUD"
        pass
        # w = self.QWidgetHud.width()
        # h = self.QWidgetHud.height()
        # if w > h:
        #     w_dx = (w - h)  # exceso de espacio segun el cuadrado de hxh
        #
        #     self.horizontalLayout_9.setStretch(0, 50 * w_dx / h)
        #     self.horizontalLayout_9.setStretch(1, 100 * (1 - w_dx / h))
        #     self.horizontalLayout_9.setStretch(2, 50 * w_dx / h)
        #
        # else:
        #     self.horizontalLayout_9.setStretch(0, 0)
        #     self.horizontalLayout_9.setStretch(1, 1)
        #     self.horizontalLayout_9.setStretch(2, 0)


    def set_statusOption(self, status):

        if status:
            self.btn_Inic.setMaximumWidth(16777215)
            self.btn_Inic.setMaximumHeight(16777215)

            self.btn_conf.setMaximumWidth(16777215)
            self.btn_conf.setMaximumHeight(16777215)
        else:
            self.btn_Inic.setMaximumWidth(0)
            self.btn_Inic.setMaximumHeight(0)

            # self.btn_sens.setMaximumWidth(0)
            # self.btn_sens.setMaximumHeight(0)

            self.btn_conf.setMaximumWidth(0)
            self.btn_conf.setMaximumHeight(0)

    def agregarMision(self, mision=None):
        "Funcion encargada de agregar una fila (mision) en la tabla de misiones."

        post = self.tablaMisiones.rowCount()
        self.tablaMisiones.insertRow(post)

        self.comboMis = QtGui.QComboBox()
        self.comboFrame = QtGui.QComboBox()

        self.comboMis.setStyleSheet(self.styleComboBox)

        self.comboFrame.setStyleSheet(self.styleComboBox)

        self.comboMis.addItems(self.misOpciones.values())

        self.comboFrame.addItems(["", "Global", "Relativo"])

        self.comboFrame.setStyleSheet(self.styleComboBox)
        self.comboMis.setStyleSheet(self.styleComboBox)

        self.btnDelete = QtGui.QPushButton()

        icon = QtGui.QIcon()
        # d2, d3
        icon.addPixmap(QtGui.QPixmap("img/d4"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.btnDelete.setIcon(icon)
        self.btnDelete.setFlat(True)
        self.btnDelete.setStyleSheet("background-color : #000000")

        # Se agrega los primeros ComboBox
        self.btnDelete.clicked.connect(self.eliminarMision)
        self.comboMis.currentIndexChanged.connect(self.opcionesMis)

        self.tablaMisiones.setCellWidget(post, 0, self.comboMis)
        self.tablaMisiones.setCellWidget(post, 1, self.comboFrame)
        # Luego de los combobox se agregan los QLine para ingresar los parametros
        for i in range(2, 6):
            line = QtGui.QLineEdit()
            # line.setInputMask("00")
            line.setPlaceholderText("")
            line.setStyleSheet("background-color: transparent;\ncolor: rgba(255,255,255,255);")
            self.tablaMisiones.setCellWidget(post, i, line)

        # Después se agrega el último botón para eliminar dicha fila
        self.tablaMisiones.setCellWidget(post, 6, self.btnDelete)

        if mision != False:  # En caso de rellenar los campos de una misión descargada, unicamente se rellenan los widget ya creados
            # print "Se están por cargar las misiones"
            # print "Misión recibida para cargar en el tablewidget - >", mision
            self.human =False #Esta variable es para avisar que no me autocomplete el texthint, ya que de caso contrario me sobreescribe los valores por concurrencia
            self.comboMis.setCurrentIndex(int(mision[0]))
            self.comboFrame.setCurrentIndex(int(mision[1]))
            #FIX - No tienen las mismas posiciones todos los parametros
            # self.tablaMisiones.cellWidget(post, 2).setText(str(mision[2]))
            # self.tablaMisiones.cellWidget(post, 3).setText(str(mision[6]))
            # self.tablaMisiones.cellWidget(post, 4).setText(str(mision[7]))
            # self.tablaMisiones.cellWidget(post, 5).setText(str(mision[8]))
            indx = mision[0]
            print "Tipo de misión que voy a cargar: ", indx
            print "Diccionario : " , self.misOpciones
            print "Lo que voy a cargar: ", mision

            if indx == 1 or indx == 4:
                self.tablaMisiones.cellWidget(post, 2).setText(str(mision[6]))
                self.tablaMisiones.cellWidget(post, 3).setText(str(mision[7]))
                self.tablaMisiones.cellWidget(post, 4).setText(str(mision[8]))

            elif indx == 2:
                self.tablaMisiones.cellWidget(post, 2).setText(str(mision[2]))
                self.tablaMisiones.cellWidget(post, 3).setText(str(mision[6]))
                self.tablaMisiones.cellWidget(post, 4).setText(str(mision[7]))
                self.tablaMisiones.cellWidget(post, 5).setText(str(mision[8]))
            elif indx == 5:
                self.tablaMisiones.cellWidget(post, 2).setText(str(mision[8]))
            elif indx == 6:
                # grados, sentido = 1, relativo = True
                self.tablaMisiones.cellWidget(post, 2).setText(str(mision[2]))
                self.tablaMisiones.cellWidget(post, 3).setText(str(mision[3]))
        self.human=True
            # mision[2] = cmd.param1
            # mision[3] = cmd.param2
            # mision[4] = cmd.param3
            # mision[5] = cmd.param4
            # mision[6] = cmd.x
            # mision[7] = cmd.y
            # mision[8] = cmd.z

    def initListParametros(self):
        "Agrega los parametros en lalistParametros pesataña (GRAFICOS) para agregarlos en el widget GraphData"
        parameters = self.qcopter.obt_parametros(-1)
        nRows = parameters.__len__()
        self.listAtributos.setRowCount(nRows)

        for r in range(1, nRows):
            checkBox = QtGui.QCheckBox()
            checkBox.stateChanged.connect(self.addParam2Graph)
            checkBox.setStyleSheet("margin-left : 50%; background-color: transparent; ")
            # checkBox.setLayoutDirection(2)

            # W = QtGui.QWidget()
            #layoutCheck = QtGui.QHBoxLayout(self.listAtributos)
            #layoutCheck.addWidget(checkBox)
            #layoutCheck.setAlignment(QtCore.Qt.AlignHCenter)
            # W.setLayout(layoutCheck)

            # self.listAtributos.insertRow(r)
            self.listAtributos.setItem(r, 0, QtGui.QTableWidgetItem(parameters[r][0]))
            self.listAtributos.setCellWidget(r, 1, checkBox)

    def displayDataGraph(self, index):
        if index == 1:  # Si estamos en la pestaña de grafico de parametros
            self.Graph.play(True)
        else:
            self.Graph.play(False)

    def callback2DataGraph(self, oVehicle, nameAttr, value):
        "Funcion que conecta el cambio de valores de la lista de atributos para que se puedan graficar"

        # Obtengo el valor de la fila seleccionada
        value = self.qcopter.obt_parametros(self._INDX_PARAM)[1]
        # Al agregar nueva informacion puede ocurrir que la cantidad de graficas maximas permitidas sea superado
        # por lo tanto, se tendrá que eliminar la primer grafica ingresada
        resp = self.Graph.addData(self._INDX_PARAM, value)
        # Si la respuesta es -1, quiere decir que todavia hay espacio para almacenar más gráficas.
        if resp != -1:
            cb_toDisable = self.listAtributos.cellWidget(resp, 1)
            cb_toDisable.setChecked(False)
            self.Graph.removeLine(resp)
            nombre_atributo = self.qcopter.obt_parametros(self._INDX_PARAM)[2]
            self.qcopter.removeCallback(nombre_atributo, self.callback2DataGraph)

    def addParam2Graph(self):
        "Funcion encargada de gestionar la interaccion entre los checkbox pertenecientes a cada parametro y su gràfica"
        QCheckBox_pressed = QtGui.QApplication.focusWidget()


        CB_pos = self.listAtributos.indexAt(QCheckBox_pressed.pos())
        # print CB_pos.row() ,"(Fila). Estado : ", QCheckBox_pressed.isChecked()
        self._INDX_PARAM = CB_pos.row()

        self._NAME_PARAM =  self.listAtributos.item(CB_pos.row(), 0).text()
        # print self._NAME_PARAM  , type(self._NAME_PARAM ), dir(self._NAME_PARAM )

        nombre_atributo = self.qcopter.obt_parametros(self._INDX_PARAM)[2]

        if QCheckBox_pressed.isChecked():
            # El objeto vehiculo contiene por cada parametro un lista descriptiva del atributo asociado
            # Por ejemplo: ["Descripcion", valor en tiempo real del parametro , Nombre objeto , funcion , variable]

            self.qcopter.setCallback2Param(nombre_atributo,self.callback2DataGraph)
        else:
            self.Graph.removeLine(CB_pos.row())
            self.qcopter.removeCallback(nombre_atributo,self.callback2DataGraph)
        #

    def descargarMisiones2Tabla(self):
        "Se descargan las misiones del vehículo "

        #
        # MAV_FRAME_LOCAL_NED    -> 1

        if self.es_iniVehiculo():
            listaMisiones = self.qcopter.descargarMisiones()  # Ojo al piojo, estoy descargando los comandos del vehículo y no los temporales

            numMisiones_cliente = self.tablaMisiones.rowCount()
            numMisiones_vehiculo = listaMisiones.__len__()

            if numMisiones_vehiculo == 0:
                QtGui.QMessageBox.warning(self, "Sin misiones",
                                          "No se han encontrado misiones cargadas en el vehículo.")

            elif numMisiones_vehiculo != numMisiones_cliente:

                mision = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # -> [tipo de misión, frame , param1 , param2, param3, param4, x, y , z]
                for cmd in listaMisiones:
                    print "Mision recibida del vehiculo : ", cmd
                    #Se realiza el mapeo de codigos de los comandos con los codigos de mis indices para mostrar en la tabla
                    if cmd.command == 16:  # 16 -> MAV_CMD_NAV_WAYPOINT
                        mision[0] = 1
                        if cmd.frame == 6:  # 3 -> MAV_FRAME_GLOBAL_RELATIVE_ALT
                            mision[1] = 1
                        else:
                            mision[1] = 2

                    if cmd.command == 19:  # 19 -> MAV_CMD_NAV_LOITER_TIME
                        mision[0] = 2
                        if cmd.frame == 6:  # 3 -> MAV_FRAME_GLOBAL_RELATIVE_ALT
                            mision[1] = 1
                        else:
                            mision[1] = 2

                    if cmd.command == 20:  # 20 -> MAV_CMD_NAV_RETURN_TO_LAUNCH
                        mision[0] = 3
                        mision[1] = 0

                    if cmd.command == 21:  # 19 -> MAV_CMD_NAV_LAND
                        mision[0] = 4
                        if cmd.frame == 6:  # 3 -> MAV_FRAME_GLOBAL_RELATIVE_ALT
                            mision[1] = 1
                        else:
                            mision[1] = 2

                    if cmd.command == 22:  # 22 -> MAV_CMD_NAV_TAKEOFF
                        mision[0] = 5
                        mision[1] = 1

                    if cmd.command == 115:  # 115 -> MAV_CMD_CONDITION_YAW
                        mision[0] = 6

                        if cmd.frame == 6:  # 3 -> MAV_FRAME_GLOBAL_RELATIVE_ALT
                            mision[1] = 1
                        else:
                            mision[1] = 2

                    mision[2] = cmd.param1
                    mision[3] = cmd.param2
                    mision[4] = cmd.param3
                    mision[5] = cmd.param4
                    mision[6] = cmd.x
                    mision[7] = cmd.y
                    mision[8] = cmd.z

                    self.agregarMision(mision)

        else:
            logging.error("Error en la funcion de descargarMisiones2Tabla: " + sys.exc_info())
            QtGui.QMessageBox.warning(self, "Ah ocurrido algo extraño", "Por favor, renicie BEcopter.")

    def validarMisiones(self, Misiones):
        "Comprueba el contenido dentro de cada misión. En caso de haber alguna anomalia enviará el indice correspondiente"
        codigo = []

        for m_i in range(Misiones.__len__()):
            m = Misiones[m_i]
            codOpciones = self.misOpciones  # Es un diccionario con las opciones disponibles

            if m[0] == '' or m[1] == '':  # Se comprueba que que el campo de tipo de misión y frame esten completos
                if m[0] != codOpciones[3]:
                    codigo.append(m_i)
            elif codOpciones[1] == m[0] or codOpciones[4] == m[0]:  # Punto Objetivo y Aterrizar
                if m[-2] == '' or m[-3] == '' or m[-4] == '':
                    codigo.append(m_i)
            elif codOpciones[2] == m[0]:  # Holgazanear
                if m[-1] == '' or m[-2] == '' or m[-3] == '' or m[-4] == '':
                    codigo.append(m_i)
            elif codOpciones[5] == m[0]:  # Despegar
                if m[-4] == '':
                    codigo.append(m_i)
            # elif codOpciones[6] == m[0]:  # Cambiar Yaw
            #     if m[-4] == '' or m[-3] == '':
            #         codigo.append(m_i)

        return codigo

    def enviarMisiones(self):
        "Funcion que obtiene los valores de la tabla (misiones) y se las envia al vehiculo"
        # try:
        n = self.tablaMisiones.rowCount()
        tablaMisiones = self.tablaMisiones
        Misiones = []
        Mision = []
        infcelda = ""
        # Chequeo de datos y tipos de widgets
        nColumnas = self.tablaMisiones.columnCount()

        for f in range(n):  # Recorro las filas
            for c in range(0, nColumnas - 1):
                infcelda = tablaMisiones.cellWidget(f, c)
                # Información de la celda contiene un widget (combobox o lineEdit)
                if c < 2:  # Los combobox están en la posición 1 y 2
                    if infcelda != None:
                        infcelda = str(infcelda.currentText())
                else:
                    if infcelda != None:
                        infcelda = str(infcelda.text())

                Mision.append(infcelda)
            Misiones.append(Mision)
            Mision = []

        if Misiones.__len__() == 0:
            QtGui.QMessageBox.warning(self, "Envío no exitoso",
                                      "No se han ingresado misiones")
            return

        # Decodificación y envio de mensajes al vahículo.

        codigo = self.validarMisiones(Misiones)
        # Se comprueba que los campos de cada misión sean correctos, en caso contrario se enviará el indice de las misiones incompletas/incorrectas

        if codigo == []:
            self.qcopter.borrarMisiones()
            # Se borrar las misiones que estaban en el vehículo para evitar conflictos
            for m in Misiones:
                print "Mision por enviar al vehiculo -> ", m
                if m[0] == "Punto Objetivo":
                    if m[1] == "Global":

                        # mis_irPunto(self, lat, long, alt, relativo=True)
                        self.qcopter.mis_irPunto(int(m[-4]), int(m[-3]), int(m[-2]), False)
                    elif m[1] == "Relativo":
                        self.qcopter.mis_irPunto(int(m[-4]), int(m[-3]), int(m[-2]), False)
                    else:
                        "Elol Punto objetivo"
                elif m[0] == "Holgazanear":
                    # mis_holgazanear(self, segundos, lat, long, alt):
                    self.qcopter.mis_holgazanear(int(m[-4]), int(m[-3]), int(m[-2]), int(m[-1]))
                elif m[0] == "Volver al inicio":
                    self.qcopter.mis_volverInicio()
                elif m[0] == "Aterrizar":
                    # mis_aterrizar(self, lat, long, alt):
                    self.qcopter.mis_aterrizar(int(m[-4]), int(m[-3]), int(m[-2]))
                elif m[0] == "Despegar":
                    # mis_despegar(self, altura):
                    self.qcopter.mis_despegar(int(m[-4]))
                elif m[0] == "Cambiar Yaw":
                    if m[1] == 'Global':
                        self.qcopter.yaw(int(m[-4]), int(m[-3]), False)
                    else:
                        self.qcopter.yaw(int(m[-4]), int(m[-3]), True)

            QtGui.QMessageBox.information(self, "Envío exitoso", "Las misiones se han enviado con éxito.")
        else:
            QtGui.QMessageBox.warning(self, "Envío no exitoso",
                                      "Las misiones no se han podido enviar. Compruebe la/s fila/s :" + str(
                                          map(lambda x: x + 1, codigo)))
        # except:
        #     QtGui.QMessageBox.critical(self, "Error",
        #                                "Funcion enviar misiones:\n" + str(sys.exc_info()) )

    def IniciarMis(self):

        try:
            if self.qcopter.obt_cantMisiones() != 0:

                if not (hasattr(self, 'Joystick')):
                    QtGui.QMessageBox.critical(self, "Ningún comando conectado",
                                               "Por seguridad, por favor seleccione un joystick en la pestaña Comando")
                    return
                if self.qcopter.iniciarMisiones():
                    QtGui.QMessageBox.information(self, "Despegando", "Las misiones han sido enviadas.")
                    self.tablaMisiones.setEnabled(False)
                else:
                    estados = self.qcopter.obt_estado()
                    if not estados['gps']:
                        QtGui.QMessageBox.critical(self, "Error",
                                                   "No se han podido enviar las misiones. Compruebe el GPS.")
                    elif not estados['state']:
                        QtGui.QMessageBox.critical(self, "Error",
                                                   "No se han podido enviar las misiones. Compruebe que el vehículo este en inicializado.")
                    elif not estados['ekf']:
                        QtGui.QMessageBox.critical(self, "Error",
                                                   "No se han podido enviar las misiones. Compruebe que el vehículo este bien ubicado.")
                    else:
                        QtGui.QMessageBox.critical(self, "Error",
                                                   "No se han podido enviar las misiones.")

            else:
                QtGui.QMessageBox.warning(self, "No hay misiones", "No se encuentran misiones cargadas en el vehículo")
        except:
            QtGui.QMessageBox.critical(self, "Error",
                                       "Ocurrió un error al enviar las misiones. \n" + "Detalles: \n" + str(
                                           sys.exc_info()))

    def _initMenuBtn(self):
        "Inicializa las acciones a cada parametro del vehículo"

        self.menu = QtGui.QMenu()
        params = self.qcopter.obt_parametros(-1)
        self.actions = []
        for k in params.keys():
            action = QtGui.QAction(params[k][0], self.menu)
            action.setData(k)
            self.menu.addAction(action)

    def agregarMenuBotones(self):
        "Se asigna a cada boton de la botonera su respectivas opciones"

        #Se inicializan las acciones => Lista de parametros
        self._initMenuBtn()

        #Se asocia el menu creado a los botones
        self.B1_btn.setMenu(self.menu)
        self.B2_btn.setMenu(self.menu)
        self.B3_btn.setMenu(self.menu)
        self.B4_btn.setMenu(self.menu)
        self.B5_btn.setMenu(self.menu)
        self.B6_btn.setMenu(self.menu)
        self.B7_btn.setMenu(self.menu)
        self.B8_btn.setMenu(self.menu)

        self.menu.triggered[QtGui.QAction].connect(self.cambiarBtnParam)

    def cambiarBtnParam(self,action):
        "Funcion encargada de detectar el boton clickeado y cambiar por su nuevo valor"
        clickme = QtGui.QApplication.focusWidget()

        if clickme in self.botones:
            indxBTN = self.botones.index(clickme)
            indxPARAM = action.data().toInt()[0]
            if not( indxPARAM in self.paramShow):
                self.paramShow[indxBTN] =indxPARAM

    def funcMenuBotones(self, indxBtn, indxParam):

        # Desactivar las opciones segun la lista paramShow
        if not (self.paramShow.__contains__(indxParam)):
            self.paramShow[indxBtn] = indxParam
            self.botones[indxBtn] = self.qcopter.obt_parametros(indxParam)[1]
            self.lblbotones[indxBtn] = self.qcopter.obt_parametros(indxParam)[0]

    def actualizarBotonera(self):
        "Actualiza la información seleccionada en los botones"

        if hasattr(self, 'qcopter'):

            for i in range(8):
                self.lblbotones[i].setText(self.qcopter.obt_parametros(self.paramShow[i])[0])
                raw_value = self.qcopter.obt_parametros(self.paramShow[i])[1]

                if not(isinstance(raw_value,float)) and not(isinstance(raw_value,bool)) and not(isinstance(raw_value,int)):
                    value='-'
                else:
                    value = str(round(raw_value, 2))

                self.botones[i].setText(value)

    def extra2HUD(self, oVehicle, nameAttr, value):


        self.QWidgetHud.setInfo("", value.name)# str(round(self.normalizeAngle(value.pitch), 2)))
        if value.name in self.qcopter.manualModes():
            self.QWidgetHud.setJoystick(True)
        else:
            self.QWidgetHud.setJoystick(False)

        # self.QWidgetHud.setInfo("(P,R,Y) :", str(round(PITCH,2)) + "," + str(round(ROLL,2)) + ','+str(round(YAW,2)) )

    def signal2HUD(self, oVehicle, nameAttr, value):

        self.QWidgetHud.setSignal(50)

    def battery2HUD(self, oVehicle, nameAttr, value):

        self.QWidgetHud.setBattery(value.level)

    def status2HUD(self, oVehicle, nameAttr, value):
        error= False
        # @todo Deberia encargarse de esta condición el objeto vehiculo
        if value.state == 'CRITICAL':
            error  = True
        self.QWidgetHud.setStatus(value.state, error )

    def aloja(self, oVehicle, nameAttr, value):

        print oVehicle, nameAttr, value



    def gps2HUD(self, oVehicle, nameAttr, value):
        if value.fix_type > 1:
            self.QWidgetHud.setGPS(value.fix_type,True)
        else:
            self.QWidgetHud.setGPS(value.fix_type, False)

    def PitchRollYaw2HUD(self, oVehiculo, nameAttr, value):

        PITCH = self.normalizeAngle(value.pitch)
        ROLL = self.normalizeAngle(value.roll)

        self.QWidgetHud.setPitch(-1 * PITCH + 360)
        self.QWidgetHud.setRoll(ROLL)

    def normalizeAngle(self, rAngle):
        """Función que normaliza el angulo (en radianes) de [-180 - 180] -> [0 - 360]
        rAnggle:type radiantes
        :return grados
        """
        import math
        # Conversion de radianes a grados
        gAngle = (rAngle * 180) / math.pi

        if gAngle < 0:
            gAngle = 360 + gAngle

        return gAngle

    # CONEXION/FUNCIONES---------------------------------------------------

    def initIcons(self):
        "Funcion que escala los iconos al principio en la pestaña de conexion "
        self.gb_infoVehiculo.setEnabled(False)
        if self.lbl_sta.pixmap():
            factorw = 0.1 * self.width()
            factorh = 0.1 * self.height()

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

        try:
            # Conexión con el vehículo

            self.stateInIP(False, "")
            self.stateInPort(False, "")
            IP = self.inIP.text()
            PORT = self.inPort.text()
            IP = str(IP)
            PORT = str(PORT)

            if IP != "" and PORT != "":

                if hasattr(self, 'qcopter') and self.es_iniVehiculo():

                    self.qcopter.desconectar()
                    self.switchOpciones(False)

                    self.btn_conectar.setText("Conectar")
                    self.gb_infoVehiculo.setEnabled(False)
                    self.timerInfo.stop()
                    self.timerOpt.stop()
                    self.actualizarConsolaVehicle(False)
                    del self.qcopter



                else:

                    self.qcopter = Vehiculo.Vehiculo(IP, PORT)

                    if self.qcopter.conectado():
                        self.set_statusOption(True)  # Se habilitan las opciones del lado izquierdo del programa
                        # self.qcopter.setCallback2Param('heading',self.HUDi)

                        # self.stateBtnConectado(True)
                        # self.infoVehiculo.setPlainText(self.qcopter.obt_parametros())
                        self.btn_conectar.setText("Desconectar")
                        self.timerInfo.start(1000)
                        self.timerOpt.start(700)

                        self.gb_infoVehiculo.setEnabled(True)
                        # Conectamos el vehículo con el HUD, para representarlo graficamente
                        self.qcopter.setCallback2Param('heading', self.QWidgetHud.setHeading)
                        self.qcopter.setCallback2Param('attitude',
                                                       self.PitchRollYaw2HUD)  # Funcion encargada de enviar el pitch, roll y yaw
                        self.qcopter.setCallback2Param('gps_0', self.gps2HUD)
                        self.qcopter.setCallback2Param('battery', self.battery2HUD)
                        self.QWidgetHud.setStatus(self.qcopter.v.battery.level)


                        self.qcopter.setCallback2Param('rangefinder', self.signal2HUD)
                        self.qcopter.setCallback2Param('mode', self.extra2HUD)
                        self.qcopter.setCallback2Param('STATUSTEXT',self.aloja)
                        self.qcopter.setCallback2Param('system_status', self.status2HUD)
                        self.QWidgetHud.setStatus(self.qcopter.v.system_status.state)
                        # print self.qcopter.v.mode , type(self.qcopter.v.mode) , dir(self.qcopter.v.mode)
                        self.cargarParametros()

                        self.initListParametros()
                        self.agregarMenuBotones()




            elif IP == "":
                self.stateInIP(True, "Ingrese una IP valida")
            elif PORT == "":
                self.stateInPort(True, "Ingrese un puerto válido")

            self.actualizarConsolaVehicle()

        except WindowsError as e:

            QtGui.QMessageBox.warning(self, "Error de conexión", e.message)

    def actualizarInfoVechicle(self, conectado=True):
        "Esta funcion se encarga de actualizar los iconos de estados."
        try:
            if self.todo.currentIndex() == 2:
                ste = self.qcopter.obt_estado()

                width = self.cone.width() * 0.1
                height = self.cone.height() * 0.1

                if (conectado == True):
                    # INFORMACION DEL GPS
                    if ste['gps'] == None:
                        GPS = QtGui.QPixmap("../BEcopter/img/conexion/GPSicon/worldwide_war.png")
                    elif ste['gps'] == True:
                        GPS = QtGui.QPixmap("../BEcopter/img/conexion/GPSicon/worldwide_ok.png")
                    else:
                        GPS = QtGui.QPixmap("../BEcopter/img/conexion/GPSicon/worldwide_nok.png")

                    # INFORMACION DE LA BATERIA
                    if ste['battery'] == None:
                        Battery = QtGui.QPixmap("../BEcopter/img/conexion/Batteryicon/battery_war.png")
                    elif ste['battery'] == True:
                        Battery = QtGui.QPixmap("../BEcopter/img/conexion/Batteryicon/battery_ok.png")
                    else:
                        Battery = QtGui.QPixmap("../BEcopter/img/conexion/Batteryicon/battery_nok.png")

                    # INFORMACION DEL FILTRO EXTENDIDO DE KALMAN
                    if ste['ekf'] == None:
                        EKF = QtGui.QPixmap("../BEcopter/img/conexion/warning.png")
                    elif ste['ekf'] == True:
                        EKF = QtGui.QPixmap("../BEcopter/img/conexion/success.png")
                    else:
                        EKF = QtGui.QPixmap("../BEcopter/img/conexion/error.png")

                    # INFORMACION DE LA SEÑAL
                    if ste['signal'] == None:
                        SIGNAL = QtGui.QPixmap("../BEcopter/img/conexion/Signalicon/antenna_war.png")
                    elif ste['signal'] == True:
                        SIGNAL = QtGui.QPixmap("../BEcopter/img/conexion/Signalicon/antenna_ok.png")
                    else:
                        SIGNAL = QtGui.QPixmap("../BEcopter/img/conexion/Signalicon/antenna_nok.png")

                    # INFORMACION SI ESTA LISTO PARA DESPEGAR
                    if ste['ready'] == True:
                        READY = QtGui.QPixmap("../BEcopter/img/conexion/drone_ok.png")
                    else:
                        READY = QtGui.QPixmap("../BEcopter/img/conexion/drone_nok.png")

                    TYPE = QtGui.QPixmap("../BEcopter/img/conexion/quadcopter.png")

                else:
                    READY = QtGui.QPixmap("../BEcopter/img/conexion/drone.png")
                    SIGNAL = QtGui.QPixmap("../BEcopter/img/conexion/Signalicon/antenna.png")
                    EKF = QtGui.QPixmap("../BEcopter/img/conexion/dude.png")
                    Battery = QtGui.QPixmap("../BEcopter/img/conexion/Batteryicon/battery.png")
                    GPS = QtGui.QPixmap("../BEcopter/img/conexion/GPSicon/worldwide.png")

                # INFORMACION DEL TIPO DE VEHICULO (por el momento solo cuadricopteros)
                self.lbl_type.setPixmap(TYPE.scaled(width, height))
                self.lbl_gps.setPixmap(GPS.scaled(width, height))
                self.lbl_bat.setPixmap(Battery.scaled(width, height))
                self.lbl_com.setPixmap(SIGNAL.scaled(width, height))
                self.lbl_sta.setPixmap(EKF.scaled(width, height))
                self.lbl_ok.setPixmap(READY.scaled(width * 0.8, height * 0.8))
                self.lbl_firm.setText(str(self.qcopter.v.version))
        except AttributeError:
            self.set_statusOption(False)
            QtGui.QMessageBox.Warning(self,"Error de conexion", "Vehiculo no inicializado.")

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

    # COMANDO/FUNCIONES---------------------------------------------------

    def mostrarEje(self,eje,value):
        """
        Funcion que se encarga de obtener el valor del joystick (Ejes - Analogicos) y mapea su valor de [0,100]
        para mostrarlo en los progressBar de la pestaña COMANDO
        :param eje   : Id del Eje       :type Entero
        :param value : valor del stick  :type Flotante

        """
        value = 50*(value+1)
        if eje == 0:
            if self.invA0.isChecked():
                value = -value + 100
            self.pbAxis0.setValue(value)
        if eje == 1:
            if self.invA1.isChecked():
                value = -value + 100
            self.pbAxis1.setValue(value)

        if eje == 2:
            if self.invA2.isChecked():
                value = -value + 100
            self.pbAxis2.setValue(value)

        if eje == 3:
            if self.invA3.isChecked():
                value = -value + 100
            self.pbAxis4.setValue(value)





    def checkJoysticks(self, args):


        if self.Joystick.conectados().__len__() == 0:
            self.dispConectados.clear()
            self.dispConectados.insertItem(0, " ")
            logging.info("No se encontraron joysticks conectados.")

    def showJoysticks(self):
        "Cada vez que se toque el boton de comandos en la ventana principal, esta función actualizará los joystick conetados en el qcombobox"

        if not(hasattr(self,'Joystick')):
            self.Joystick = Joystick.Joystick()


        if self.dispConectados.currentText() != " ":

            # Se ejecuta en background el capturador para que se encargue de gestionar los botones ingresados
            self.capturador.capturing(True)



        elif self.dispConectados.count() - 1 < self.Joystick.conectados().__len__():

            dicConectados = self.Joystick.conectados()

            self.dispConectados.clear()
            self.dispConectados.insertItem(0, " ")

            for j in dicConectados:
                self.dispConectados.insertItem(j + 1, dicConectados[j])

    def initOpJoy(self):

        listaEjes = [self.opcionesJoyEje[key][0] for key in self.opcionesJoyEje]
        blankEje = listaEjes.__len__() - 1
        listaBtns = [self.opcionesJoyBtn[key][0] for key in self.opcionesJoyBtn]
        blankBtns = listaBtns.__len__() - 1

        # Botonoes
        self.cone_op1.addItems(listaBtns)
        self.cone_op1.setCurrentIndex(blankBtns)
        self.cone_op2.addItems(listaBtns)
        self.cone_op2.setCurrentIndex(blankBtns)
        self.cone_op3.addItems(listaBtns)
        self.cone_op3.setCurrentIndex(blankBtns)
        self.cone_op4.addItems(listaBtns)
        self.cone_op4.setCurrentIndex(blankBtns)

        # Ejes
        self.opA0.addItems(listaEjes)
        self.opA0.setCurrentIndex(blankEje)

        self.opA1.addItems(listaEjes)
        self.opA1.setCurrentIndex(blankEje)
        self.opA2.addItems(listaEjes)
        self.opA2.setCurrentIndex(blankEje)
        self.opA3.addItems(listaEjes)
        self.opA3.setCurrentIndex(blankEje)

    def sendManualCmd(self,cmd,valor,eje):
        """Funcion que recibe el comando (ya mapeado) y lo envia al vehiculo.
            cmd: Comando grabado en los diccionarios opcionesJoyBtn y opcionesJoysEje.
            valor: el valor a enviar a dicho comando.
            eje: Valor booleano que determina si es un comando de tipo eje o tipo boton.
        """

        cmd = self.Joystick.obt_mapeo(cmd)

        #AQUI SE DEBE IMPLEMENTAR O "CONECTAR" LAS NUEVAS FUNCIONES
        # print "[_sendManualCmd] Mapeador : ", cmd , " Valor : ", valor


        if cmd != '' and hasattr(self,'qcopter'):
            if eje:
                if self.opcionesJoyEje[0][0] == cmd:  #ROLL
                    self.qcopter.canal(1,valor)
                if self.opcionesJoyEje[1][0] == cmd:  # PITCH
                    self.qcopter.canal(2, valor)
                if self.opcionesJoyEje[2][0] == cmd:  # THROTTLE
                    self.qcopter.canal(3, valor)
                if self.opcionesJoyEje[3][0] == cmd:  # YAW
                    self.qcopter.canal(4,valor)
            else:

                if self.opcionesJoyBtn[0][0] == cmd:  #Aterrizar
                    logging.info("[COMANDO ENVIADO ] : Aterrizar")
                    self.qcopter.aterrizar()

                if self.opcionesJoyBtn[1][0] == cmd:  # Cambiar modo
                    print "Cambiar modo"
                    logging.info("[COMANDO ENVIADO ] : Cambiar Modo")
                    self.qcopter.changeMode()

                if self.opcionesJoyBtn[2][0] == cmd: # Volver al Inicio
                    logging.info("[COMANDO ENVIADO ] : Volver al inicio")
                    self.qcopter.volverInicio()

                if self.opcionesJoyBtn[3][0] == cmd: #Estabilizarse
                    logging.info("[COMANDO ENVIADO ] : holgazanear")
                    self.qcopter.holgazanear()

                if self.opcionesJoyBtn[4][0] == cmd: #Armar/Desarmar
                    print "Armar/Desarmar"
                    logging.info("[COMANDO ENVIADO ] : Armar/Desarmar")
                    if not(self.qcopter.obt_estado()['ekf']):
                        self.QWidgetHud.setPreArm(True)
                        logging.info("[COMANDO ENVIADO ] : Armar/Desarmar -> Sin éxito")

                    self.qcopter.toogleARM_DISARM()

        # else:
        #     print "Ningun comando registrado en este boton"




    def selectJoy(self, i):  # Tener cuidado con dos

        # try:
        self.grupoEjes.setEnabled(False)
        self.grupoBotones.setEnabled(False)

        if (i > 0):
            mapBtn = self.Joystick.seleccionarJoy(i - 1)  # i-1 ya que los items del combobox comienzan por 1
            # print "Seleccionaste un joy, y esto te mando guachin ", mapBtn
            self.grupoEjes.setEnabled(True)
            self.grupoBotones.setEnabled(True)
            if mapBtn != None:
                print "Nos vamos al mapeadooooooooooooor"
                self.setMap(mapBtn)

            self.capturador.capturing(True)
            self.capturador.capturarComandos()
            self.Joystick.obt_estado()


        elif i == 0:
            # Que deje de capturar y limpie todo @TODO
            self.capturador.capturing(False)

            self.opA0.setCurrentIndex(self.opcionesJoyEje.__len__())
            self.opA1.setCurrentIndex(self.opcionesJoyEje.__len__())
            self.opA2.setCurrentIndex(self.opcionesJoyEje.__len__())
            self.opA3.setCurrentIndex(self.opcionesJoyEje.__len__())

            self.cone_op1.setCurrentIndex(self.opcionesJoyBtn.__len__())
            self.cone_op2.setCurrentIndex(self.opcionesJoyBtn.__len__())
            self.cone_op3.setCurrentIndex(self.opcionesJoyBtn.__len__())
            self.cone_op4.setCurrentIndex(self.opcionesJoyBtn.__len__())

            self.invA0.setChecked(False)
            self.invA1.setChecked(False)
            self.invA2.setChecked(False)
            self.invA3.setChecked(False)
        # except:
        #         print "Error : ", str(sys.exc_info())
        #         # QtGui.QMessageBox.Warning(super,"Error al capturar comandos" + str(sys.exc_info()[0]))


    def modoManual(self):

        if not self.Joystick.obt_estado():
            QtGui.QMessageBox.critical(self, "Ningún comando conectado",
                                       "Por seguridad, por favor seleccione un joystick en la pestaña Comando")
            return
        # print self.btn_onManual.text()
        if self.btn_onManual.text() == "Activar modo manual":
            self.btn_onManual.setEnabled(False)
            if self.qcopter.prepararVehiculo(False):  # Preparo el vehículo en modo Manual (GUIDED)
                self.btn_onManual.setEnabled(True)
                self.btn_onManual.setText("Desactivar modo manual")

                self.lbl_eje0.setText(self.opA0.currentText())
                self.lbl_eje1.setText(self.opA1.currentText())
                self.lbl_eje2.setText(self.opA2.currentText())
                self.lbl_eje3.setText(self.opA3.currentText())
                self.manualMode = True  # Bandera para poder enviar comandos en tiempo real
                self.capturador.capturing(True)
            else:
                self.btn_onManual.setEnabled(True)
                # print "No se ha podido establecer el modo manual"
        else:
            self.btn_onManual.setText("Activar modo manual")
            self.manualMode = False
            self.qcopter.prepararVehiculo()  # Preparo el vehículo para seguir con las misiones.
            self.ini_Tabs.setCurrentIndex(0)

    def __getKeyfromValue(self, dict, search):

        result = None
        for key, value in dict.items():
            # print "vamos a comprobar esto - >", value[0], " == ",search
            if value[0] == search:
                result = key
        # print "Que estas buscando ??? ", search , ". En -> ", dict, ". Y yo te dije - >", result
        return result

    def setMap(self, mapeo):
        "Funcion que recibe un diccionario con un mapeo ya establecido y los carga en la GUI"

        blankEje = self.opcionesJoyEje.__len__() - 1
        blankBtn = self.opcionesJoyBtn.__len__() - 1

        indx = self.__getKeyfromValue(self.opcionesJoyBtn, mapeo[0])
        # print "Esto recibi la puta madre que lo pario :", indx , ". Type : ",type(indx)
        if indx == None:
            self.cone_op1.setCurrentIndex(blankBtn)
        else:
            self.cone_op1.setCurrentIndex(indx)
            self.opcionesJoyBtn[indx][1] = True

        indx = self.__getKeyfromValue(self.opcionesJoyBtn, mapeo[1])
        if indx == None:
            self.cone_op2.setCurrentIndex(blankBtn)
        else:
            self.cone_op2.setCurrentIndex(indx)
            self.opcionesJoyBtn[indx][1] = True

        indx = self.__getKeyfromValue(self.opcionesJoyBtn, mapeo[2])
        if indx == None:
            self.cone_op3.setCurrentIndex(blankBtn)
        else:
            self.cone_op3.setCurrentIndex(indx)
            self.opcionesJoyBtn[indx][1] = True

        indx = self.__getKeyfromValue(self.opcionesJoyBtn, mapeo[3])
        if indx == None:
            self.cone_op4.setCurrentIndex(blankBtn)
        else:
            self.cone_op4.setCurrentIndex(indx)
            self.opcionesJoyBtn[indx][1] = True

        indx = self.__getKeyfromValue(self.opcionesJoyEje, mapeo[12])
        if indx == None:
            self.opA0.setCurrentIndex(blankEje)  # 0
        else:
            self.opA0.setCurrentIndex(indx)  # 0
            self.opcionesJoyEje[indx][1] = True

        indx = self.__getKeyfromValue(self.opcionesJoyEje, mapeo[13])
        if indx == None:
            self.opA1.setCurrentIndex(blankEje)  # 0
        else:
            self.opA1.setCurrentIndex(indx)  # 0
            self.opcionesJoyEje[indx][1] = True
        indx = self.__getKeyfromValue(self.opcionesJoyEje, mapeo[14])
        if indx == None:
            self.opA2.setCurrentIndex(blankEje)  # 0
        else:
            self.opA2.setCurrentIndex(indx)  # 0
            self.opcionesJoyEje[indx][1] = True
        indx = self.__getKeyfromValue(self.opcionesJoyEje, mapeo[15])
        if indx == None:
            self.opA3.setCurrentIndex(blankEje)  # 0
        else:
            self.opA3.setCurrentIndex(indx)  # 0
            self.opcionesJoyEje[indx][1] = True

        if mapeo[16] == "":
            self.invA0.setChecked(False)

        else:

            self.invA0.setChecked(bool(mapeo[16]))
            self.ejesInvertidos[0] = bool(mapeo[16])

        if mapeo[17] == "":
            self.invA1.setChecked(False)
        else:
            self.invA1.setChecked(bool(mapeo[17]))
            self.ejesInvertidos[1] = bool(mapeo[17])

        if mapeo[18] == "":
            self.invA2.setChecked(False)
        else:
            self.invA2.setChecked(bool(mapeo[18]))
            self.ejesInvertidos[2] = bool(mapeo[18])

        if mapeo[19] == "":
            self.invA3.setChecked(False)
        else:
            self.invA3.setChecked(bool(mapeo[19]))
            self.ejesInvertidos[3] = bool(mapeo[19])

    def mapeoJoystick(self, txt):

        ComboBox = QtGui.QApplication.focusWidget()

        objectName = ComboBox.objectName()

        if objectName in ["opA0", "opA1", "opA2", "opA3"]:
            newAction = ComboBox.currentIndex()
            print newAction
            if self.opcionesJoyEje[ComboBox.currentIndex()][1] == False:

                self.opcionesJoyEje[ComboBox.previusIndex()][1] = False
                if self.opcionesJoyEje[ComboBox.currentIndex()][0] != "":
                    self.opcionesJoyEje[newAction][1] = True

                if objectName == "opA0":
                    self.Joystick.agr_mapeo(12, ComboBox.currentText())
                if objectName == "opA1":
                    self.Joystick.agr_mapeo(13, ComboBox.currentText())
                if objectName == "opA2":
                    self.Joystick.agr_mapeo(14, ComboBox.currentText())
                if objectName == "opA3":
                    self.Joystick.agr_mapeo(15, ComboBox.currentText())

            else:
                ComboBox.setCurrentIndex(ComboBox.previusIndex())


        elif objectName in ["cone_op1", "cone_op2", "cone_op3", "cone_op4"]:
            newAction = ComboBox.currentIndex()

            if self.opcionesJoyBtn[ComboBox.currentIndex()][1] == False:

                self.opcionesJoyBtn[ComboBox.previusIndex()][1] = False

                if self.opcionesJoyBtn[ComboBox.currentIndex()][0] != "":
                    self.opcionesJoyBtn[newAction][1] = True

                if objectName == "cone_op1":
                    self.Joystick.agr_mapeo(0, ComboBox.currentText())
                if objectName == "cone_op2":
                    self.Joystick.agr_mapeo(1, ComboBox.currentText())
                if objectName == "cone_op3":
                    self.Joystick.agr_mapeo(2, ComboBox.currentText())
                if objectName == "cone_op4":
                    self.Joystick.agr_mapeo(3, ComboBox.currentText())
            else:
                ComboBox.setCurrentIndex(ComboBox.previusIndex())

        elif objectName in ["invA0", "invA1", "invA2", "invA3"]:
            # print self.ejesInvertidos

            if objectName == "invA0":
                self.Joystick.agr_mapeo(16, ComboBox.isChecked())
                self.ejesInvertidos[0] = ComboBox.isChecked()
            if objectName == "invA1":
                self.Joystick.agr_mapeo(17, ComboBox.isChecked())
                self.ejesInvertidos[1] = ComboBox.isChecked()
            if objectName == "invA2":
                self.Joystick.agr_mapeo(18, ComboBox.isChecked())
                self.ejesInvertidos[2] = ComboBox.isChecked()
            if objectName == "invA3":
                self.Joystick.agr_mapeo(19, ComboBox.isChecked())
                self.ejesInvertidos[3] = ComboBox.isChecked()
            # print self.ejesInvertidos

    # CONFIGURACION/FUNCIONES---------------------------------------------------

    def cargarParametros2(self):
        INDEX = self.tabConfiguracion.currentIndex()
        print "Te voy a restaurar la concha de tu {}".format(INDEX)
        self.cargarParametros(INDEX)
        # Que cuando cargue el valor del parametro obtenido del vehiculo, este debe ser guardado en un atributo de Parametro

    def cargarParametros(self, indx=None):
        "Carga los parametros en las tablas pertenecientes a la pestaña CONFIGURACION"
        """
            -*Función que carga los parametros almacenados en el archivo y los muestra en sus correspondientes tabs*-
            indx = None -> Carga todos los parametros en en todas las tabs/pestañas. Esto se hace al inicio del programa cuando se establece una conexión y para restaurar (En caso de ser necesario)..
            indx = #    -> Carga los parametros de la pestaña correspondiente al indx.
        """
        # try:
        # Cuando haga esto, tengo que hacer una lista de GestParametros que sea de la misma cantidad de pestañas que tenga en la configuracion
        ntabs = self.tabConfiguracion.count()


        toPlay = []


        # En caso de cargar todas las pesatañas se entra en la primera condición, en caso contrario, únicamente se cargara la pestaña correspondientes (en el elif)
        if indx == None:  # Si el indx @fixme - Esto esta re mal, solamente al recargar debe cargar de nuevlo los valores del parametro (que es lo único editable)

            for hoja in range(ntabs):
                self.ListGP.append(Parametros.GestParametros("data/configParameters.xlsx",
                                                             hoja))  # Lista de gestores de parametros (Correspondiente a cada pestaña
            n = 0
            for l in self.ListGP:
                if l != []:
                    n += 1
            toPlay = range(n)


        else:

            self.ListGP = [Parametros.GestParametros("data/configParameters.xlsx",
                                                     indx)]  # Cargo la informacion perteneciente a los parametros de "ArduPilot Parameters"
            if self.ListGP[0].getParams() == []:
                toPlay = []
            else:
                toPlay = [indx]
        # toPlay, tendra las pestañas correspondientes a tratar

        print "Entramos a cargar las configuraciones"

        for iGP in toPlay:

            if len(toPlay) == 1:
                LP = self.ListGP[0].getParams()  # Lista de Parametros (LP)
            else:
                LP = self.ListGP[iGP].getParams()  # Lista de Parametros (LP)

            tab = self.tabConfiguracion.widget(iGP)  # Voy recorriendo las pestañas y voy obteniendos sus correspondientes tablas



            tab = tab.children()[1]
            tab.setRowCount(0)
            tab.setColumnCount(6)
            if iGP == 0:
                ancho = tab.width()
            # tab.resizeColumnsToContents()

            # tab.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)





            # No hace falta inicializar esta propiedad en True, ya que por defecto lo esta
            tab.setWordWrap(True)

            tab.setColumnWidth(0, ancho/6)
            tab.setColumnWidth(1, ancho/4)
            tab.setColumnWidth(2, ancho/2)
            tab.setColumnWidth(3, ancho/8)
            tab.setColumnWidth(4, ancho/8)
            tab.setColumnWidth(5, ancho/8)

            for p in range(LP.__len__()):
                param = LP[p]
                tab.insertRow(p)


                tab.setItem(p, 0, QtGui.QTableWidgetItem(param.getCode()))
                tab.setItem(p, 1, QtGui.QTableWidgetItem(param.getName()))
                descrip = param.getDescription()
                tab.setRowHeight(p,descrip.__len__()//2)

                tab.setItem(p, 2, QtGui.QTableWidgetItem(descrip))



                # descrip = tab.item(p,2)
                # descrip.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                # descrip.setText(param.getDescription())
                # tab.setItem(p, 2,descrip)



                #Esto es en caso de querer restaurar los valores originales (cuando se inicio la última vez el programa)
                if len(toPlay)  == 1 :
                    tab.setItem(p, 4, QtGui.QTableWidgetItem(str(self.parametros[param.getCode()])))
                else:
                    value = self.qcopter.v.parameters[param.getCode()]
                    # Guardo los parametros cargados en el p-énesimo tab, en caso de querer restaurarlo.
                    self.parametros[param.getCode()] = value
                    tab.setItem(p, 4, QtGui.QTableWidgetItem(str(value)))



                if LP[p].hasRange():

                    slide = QtGui.QSlider(0x1)
                    r1, r2 = LP[p].getRange()
                    scale = LP[p].getScale()

                    slide.setRange(r1*scale, r2*scale)


                    slide.setValue(value)
                    slide.setTickPosition(3)
                    slide.valueChanged.connect(self.moveSliderParam)
                    # slice.setTickPosition(QtGui.QSlider.Tick)
                    tab.setCellWidget(p, 3, slide)

                    tab.setItem(p, 5, QtGui.QTableWidgetItem(LP[p].getUnits()))
    # except KeyError:
    #         print type(self)
    #         QtGui.QMessageBox.Information(self,"Error en la carga de parametros", "Ha ocurrido un error al cargar los paràmetros" + "\n" + str(sys.exc_info()))

    def guardarParametros(self):
        try:
            # print "Vamos por partes, entraste?"
            nTab_current = self.tabConfiguracion.currentIndex()
            tab = self.tabConfiguracion.widget(self.tabConfiguracion.currentIndex())
            if hasattr(self,'children()[1]'):
                tab = tab.children()[1]  # Con esto obtengo la tabla que esta adentro del tab seleccionado
                nRows = tab.rowCount()

                for r in range(nRows):
                    code = tab.item(r, 0)  # Obtengo el widget que tiene el codigo
                    code = str(code.text())  # Obtengo el código (texto)

                    value = tab.item(r, 4)  # Obtengo el widget que tiene el valor del parametro modificado
                    value = float(value.text())  # Obtengo el valor modificado
                    # print "code: ",type(code),code,". Value: ",type(value), value


                    LP = self.ListGP[nTab_current]
                    key = tab.item(r, 0).text()
                    param = LP.getParams(key)

                    self.qcopter.v.parameters[code] = value//param.getScale()  # Lo guardo en los parametros del vehículo
                QtGui.QMessageBox.Information(self,"Parametros guardados","La operaciòn ha sido exitosa")
        except:
            QtGui.QMessageBox.warning(self,"Ha ocurrido un error", "Error al guardar los parámetros")

    def moveSliderParam(self, value):

        nTab_current = self.tabConfiguracion.currentIndex()
        clickme = QtGui.QApplication.focusWidget()
        tab = self.tabConfiguracion.widget(nTab_current)

        tab = tab.children()[1]
        i = tab.indexAt(clickme.pos())
        fila = i.row()

        key = tab.item(fila,0).text()
        LP = self.ListGP[nTab_current]
        param = LP.getParams(key)
        step = param.getScale()*param.getIncrement()
        new_value = step*int(float(value)/float(step))
        print "Este es flotante" , param.isFloat() , "Incremento Real:  " , param.getIncrement() ,". Escalado : ", step ," Escala: ",param.getScale(), new_value

        tab.setItem(fila, 4, QtGui.QTableWidgetItem(str(float(new_value)/float(param.getScale()))))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    vp = BEcopter()  # Ventana principal
    vp.show()
    sys.exit(app.exec_())
