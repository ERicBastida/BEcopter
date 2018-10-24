#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
__autor__   = 'ERic Bastida'
__project__ = 'Proyecto Final de Carrera - Ingeniería en Informática'
import BEcopter
import HUD,  GraphData, GUI_becopter
from PyQt4 import QtCore, QtGui

class pInicio(BEcopter.wBEcopter):
    "Clase que gestiona el comportamiento de la pestaña INICIO dentro de BEcopter"
    def __init__(self):

        super(pInicio, self).__init__(child = True)


        #Timer para actualización de datos del vehiculo
        self.timerInfo = QtCore.QTimer()
        self.timerOpt = QtCore.QTimer()


#INICIO---------------------------------------------------
        self.btn_empezar.clicked.connect(self.IniciarMis)
        #Botón "Descargar Misiones" (Obtiene las misiones del vehículo y las representa en una tabla
        self.btn_descargar_mis.clicked.connect(self.descargarMisiones2Tabla)
        #Botón que carga las misiones en forma temporal dentro del objeto vehículo.
        self.btn_enviar_mis.clicked.connect(self.enviarMisiones)

        self.ini_Tabs.currentChanged.connect(self.displayDataGraph)
        self.Graph = GraphData.Grafico(self.parentWidget())
        self.layoutGraph.addWidget(self.Graph)
        self.layoutGraph.setStretch(0, 1)
        self.layoutGraph.setStretch(1, 3)


        self.paramShow = [3,1,2,19,16,11,20,22] #Parametros que se ven al inicicar la aplicación
        self.listParam =[]

        self.botones    = [            self.B1_btn,            self.B2_btn,            self.B3_btn,            self.B4_btn,            self.B5_btn,            self.B6_btn,            self.B7_btn,            self.B8_btn     ]
        self.lblbotones = [            self.B1_lbl,            self.B2_lbl,            self.B3_lbl,            self.B4_lbl,            self.B5_lbl,            self.B6_lbl,            self.B7_lbl,           self.B8_lbl      ]


        self.icoBecopter = QtGui.QIcon()
        self.icoBecopter.addPixmap(QtGui.QPixmap("img/BEcopter.png"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)



        self.misOpciones = {0: "", 1: "Punto Objetivo", 2: "Holgazanear", 3: "Volver al inicio", 4: "Aterrizar",
                            5: "Despegar", 6: "Cambiar Yaw"}

        # En pestaña de INICIO - Boton "Agregar Misión"
        self.btn_agregar_mis.clicked.connect(self.agregarMision)

        # Funciones que deshabilitan/habilitan las opciones de navegación cuando el vehículo esta conectado o no
        self.grupoBotones.setEnabled(False)
        self.grupoEjes.setEnabled(False)
        # Habilitar las opciones  - DEBUGGING
        self.set_statusOption(True)

        self.displayHUD()
        self.proporcionHUD()


        self.initStyleTable()

        self.styleComboBox = """QComboBox {\n
             border: 1px solid #6D6D6D;\n
             border-radius: 1px;\n 
             padding: 1px 18px 1px 3px;\n 
             min-width: 6em;\n 
             color: #FFFFFF;\n 
             background-color: black;
         }\n 
         \n 
         QComboBox:editable {\n 
             background: black;\n 
             background-color: black;\n 
         }\n 
         \n 
         QComboBox:!editable, QComboBox::drop-down:editable {\n 
              background:black;\n 

         }\n 
         \n 
         /* QComboBox gets the \ on\  state when the popup is open */\n 
         QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n 
             background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n 
                                         stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n 
                                         stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n 
         }\n 
         \n 
         QComboBox:on { /* shift the text when the popup opens */\n 
             padding-top: 3px;\n 
             padding-left: 4px;\n 
         }\n 
         \n 
         QComboBox::drop-down {\n 
             subcontrol-origin: padding;\n 
             subcontrol-position: top right;\n 
             width: 25px;\n 
         \n 
             border-left-width: 1px;\n 
             border-left-color: 6D6D6D;\n 
             border-left-style: solid; /* just a single line */\n 
             border-top-right-radius: 3px; /* same radius as the QComboBox */\n 
             border-bottom-right-radius: 3px;\n 
         }\n 
         \n 
         QComboBox::down-arrow {\n 
             image: url(img/DropDownArrow.png);\n 
             width: 4px;\n 
             height: 4px;\n 
             background: #0070FF\n 
         \n 
             \n 
         }\n 
         \n 
         QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n 
             top: 1px;\n 
             left: 1px;\n 
         } """
        self.connect(self.timerInfo, QtCore.SIGNAL("timeout()"), self.actualizarBotonera)

