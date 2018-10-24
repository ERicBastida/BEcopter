#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
__autor__   = 'ERic Bastida'
__project__ = 'Proyecto Final de Carrera - Ingeniería en Informática'

import  GUI_becopter
from PyQt4 import QtCore, QtGui



class pComando(QtGui.QMainWindow, GUI_becopter.Ui_MainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.opcionesJoyBtn = {
            # ID -> [Action, IsShowing , LastPosition]
            0: ["Aterrizar", False, 0],
            1: ["Cambiar modo", False, 1],
            2: ["Volver al Inicio", False, 2],
            3: ["Estabilizarse", False, 3],
            4: ["ARMAR/DESARMAR", False, 4],
            5: ["", False, 5]
        }

        self.opcionesJoyEje = {
            0: ["ROLL", False, 0],
            1: ["PITCH", False, 1],
            2: ["THROTTLE", False, 2],
            3: ["YAW", False,4],
            4: ["", False,5]
        }

        self.ejesInvertidos = {
            0: False,
            1: False,
            2: False,
            3: False
        }



    def checkJoysticks(self, args):

        Joystick.Joystick()

        if self.Joystick.conectados().__len__() == 0:
            self.dispConectados.clear()
            self.dispConectados.insertItem(0," ")

    def showJoysticks(self):
        "Cada vez que se toque el boton de comandos en la ventana principal, esta función actualizará los joystick conetados en el qcombobox"
        self.Joystick = Joystick.Joystick()

        # print "Que tenes guachin : (",self.dispConectados.currentText(),").",self.dispConectados.currentText().__len__()


        if self.dispConectados.currentText() != " " :

            global capturar

            capturar= True
            self.capturarComandos()

        elif self.dispConectados.count() - 1 < self.Joystick.conectados().__len__():

            dicConectados = self.Joystick.conectados()

            self.dispConectados.clear()
            self.dispConectados.insertItem(0," ")
            for j in dicConectados:
                self.dispConectados.insertItem(j + 1, dicConectados[j])

    def initOpJoy(self):

        listaEjes = [self.opcionesJoyEje[key][0] for key in self.opcionesJoyEje]
        blankEje = listaEjes.__len__()-1
        listaBtns = [self.opcionesJoyBtn[key][0] for key in self.opcionesJoyBtn]
        blankBtns = listaBtns.__len__()-1



        #Botonoes
        self.cone_op1.addItems(listaBtns)
        self.cone_op1.setCurrentIndex(blankBtns)
        self.cone_op2.addItems(listaBtns)
        self.cone_op2.setCurrentIndex(blankBtns)
        self.cone_op3.addItems(listaBtns)
        self.cone_op3.setCurrentIndex(blankBtns)
        self.cone_op4.addItems(listaBtns)
        self.cone_op4.setCurrentIndex(blankBtns)

        #Ejes
        self.opA0.addItems(listaEjes)
        self.opA0.setCurrentIndex(blankEje)

        self.opA1.addItems(listaEjes)
        self.opA1.setCurrentIndex(blankEje)
        self.opA2.addItems(listaEjes)
        self.opA2.setCurrentIndex(blankEje)
        self.opA3.addItems(listaEjes)
        self.opA3.setCurrentIndex(blankEje)

    def __sendManualCmd(self,cmd,valor,eje):
        """Funcion que recibe el comando (ya mapeado) y lo envia al vehiculo.
            cmd: Comando grabado en los diccionarios opcionesJoyBtn y opcionesJoysEje.
            valor: el valor a enviar a dicho comando.
            eje: Valor booleano que determina si es un comando de tipo eje o tipo boton.
        """
        # opcionesJoyBtn = {
        #     # ID -> [Action, IsShowing , LastPosition]
        #     0: ["Aterrizar", False, 0],
        #     1: ["Cambiar modo", False, 1],
        #     2: ["Volver al Inicio", False, 2],
        #     3: ["Estabilizarse", False, 3],
        #     4: ["ARMAR/DESARMAR", False, 4],
        #     5: ["", False, 5]
        # }
        #
        # opcionesJoyEje = {
        #     0: ["ROLL", False, 0],
        #     1: ["PITCH", False, 1],
        #     2: ["THROTTLE", False, 2],
        #     3: ["YAW", False],
        #     4: ["", False]
        # }
        #AQUI SE DEBE IMPLEMENTAR O "CONECTAR" LAS NUEVAS FUNCIONES
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
            if self.opcionesJoyEje[0][0] == cmd:  #Aterrizar
                self.qcopter.aterrizar()

            if self.opcionesJoyEje[1][0] == cmd:  # Cambiar modo
                self.qcopter.changeMode()

            if self.opcionesJoyEje[2][0] == cmd: # Volver al Inicio
                self.qcopter.volverInicio()

            if self.opcionesJoyEje[3][0] == cmd: #Estabilizarse
                self.qcopter.holgazanear()

            if self.opcionesJoyEje[4][0] == cmd: #Armar/Desarmar
                self.qcopter.toogleARM_DISARM()

    def capturarComandos(self):

        delay = 0
        global capturar
        # print " *** Condiciones para capturar comandos ***"
        # print "Esta dentro de las pestañas? : ", ((self.todo.currentIndex() == 3) or (self.todo.currentIndex() == 1))
        # print "Se habilito la bandera? : ", capturar
        while ( ((self.todo.currentIndex() == 3) or (self.todo.currentIndex() == 1)) and capturar ) :
            eventos = pygame.event.get()


            # bandera = self.todo.currentIndex() == 1 and self.ini_Tabs.currentIndex() == 1 and self.manualMode
            # Logica: Si estoy conectado con el drone, ya empiezo a enviar informacion, de la misma forma que lo hace el RC
            bandera = hasattr(self,'qcopter')

            if bandera:
                for e in eventos:
                    print "Evento :"
                    print e
                    #@TODO - Ahora buscar el código para botones
                    if e.type == 7: #e.type == 7, es un código de tipo joymotion
                        valor = 50 * (e.value + 1)
                        if e.axis == 0: #12
                            if self.invA0.isChecked():
                                valor = -valor + 100
                            self.pbAxis0.setValue(valor)

                            # print "enviaste un comandoo"
                            cmd = self.Joystick.obt_mapeo(12)
                            self.__sendManualCmd(cmd,valor, True)

                        if e.axis == 1: # 13
                            if self.invA1.isChecked():
                                valor = -valor + 100
                            self.pbAxis1.setValue(valor)
                            # self.pbEje2.setValue(valor)
                            # print "enviaste un comandoo"
                            cmd = self.Joystick.obt_mapeo(13)
                            self.__sendManualCmd(cmd,valor,True)


                        if e.axis == 2: # 14
                            if self.invA2.isChecked():
                                valor = -valor + 100
                            self.pbAxis2.setValue(valor)
                            # self.pbEje3.setValue(valor)

                                # print "enviaste un comandoo"
                            cmd = self.Joystick.obt_mapeo(14)
                            self.__sendManualCmd(cmd,valor,True)


                        if e.axis == 3: # 15
                            if self.invA3.isChecked():
                                valor = -valor + 100
                            self.pbAxis4.setValue(valor)
                            # self.pbEje4.setValue(valor)
                            # print "enviaste un comandoo"
                            cmd = self.Joystick.obt_mapeo(15)
                            self.__sendManualCmd(cmd,valor,True)



    def selectJoy(self, i):  # Tener cuidado con dos
        global capturar
        self.grupoEjes.setEnabled(False)
        self.grupoBotones.setEnabled(False)

        if (i > 0):
            mapBtn = self.Joystick.seleccionarJoy(i - 1)  # i-1 ya que los items del combobox comienzan por 1
            # print "Seleccionaste un joy, y esto te mando guachin ", mapBtn
            self.grupoEjes.setEnabled(True)
            self.grupoBotones.setEnabled(True)
            if mapBtn != None:
                # print "Nos vamos al mapeadooooooooooooor"
                self.setMap(mapBtn )


            capturar = True
            self.capturarComandos()
            self.Joystick.obt_estado()


        elif i == 0:
            #Que deje de capturar y limpie todo
            capturar = False
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
                self.capturarComandos()
            else:
                self.btn_onManual.setEnabled(True)
                # print "No se ha podido establecer el modo manual"
        else:
            self.btn_onManual.setText("Activar modo manual")
            self.manualMode = False
            self.qcopter.prepararVehiculo()  # Preparo el vehículo para seguir con las misiones.
            self.ini_Tabs.setCurrentIndex(0)

    def __getKeyfromValue(self,dict,search):

        result = None
        for key, value in dict.items():
            # print "vamos a comprobar esto - >", value[0], " == ",search
            if value[0] == search:
                result= key
        # print "Que estas buscando ??? ", search , ". En -> ", dict, ". Y yo te dije - >", result
        return result

    def setMap(self,mapeo):
        "Funcion que recibe un diccionario con un mapeo ya establecido y los carga en la GUI"

        blankEje = self.opcionesJoyEje.__len__()-1
        blankBtn = self.opcionesJoyBtn.__len__()-1


        indx = self.__getKeyfromValue(self.opcionesJoyBtn,mapeo[0])
        # print "Esto recibi la puta madre que lo pario :", indx , ". Type : ",type(indx)
        if indx == None:
            self.cone_op1.setCurrentIndex(blankBtn)
        else:
            self.cone_op1.setCurrentIndex(indx)
            self.opcionesJoyBtn[indx][1]=True

        indx = self.__getKeyfromValue(self.opcionesJoyBtn,mapeo[1])
        if indx == None:
            self.cone_op2.setCurrentIndex(blankBtn)
        else:
            self.cone_op2.setCurrentIndex(indx)
            self.opcionesJoyBtn[indx][1]=True

        indx = self.__getKeyfromValue(self.opcionesJoyBtn,mapeo[2])
        if indx == None:
            self.cone_op3.setCurrentIndex(blankBtn)
        else:
            self.cone_op3.setCurrentIndex(indx)
            self.opcionesJoyBtn[indx][1]=True

        indx = self.__getKeyfromValue(self.opcionesJoyBtn,mapeo[3])
        if indx == None:
            self.cone_op4.setCurrentIndex(blankBtn)
        else:
            self.cone_op4.setCurrentIndex(indx)
            self.opcionesJoyBtn[indx][1]=True


        indx = self.__getKeyfromValue(self.opcionesJoyEje,mapeo[12])
        if indx == None:
            self.opA0.setCurrentIndex(blankEje) #0
        else:
            self.opA0.setCurrentIndex(indx)  # 0
            self.opcionesJoyEje[indx][1]=True

        indx = self.__getKeyfromValue(self.opcionesJoyEje,mapeo[13])
        if indx == None:
            self.opA1.setCurrentIndex(blankEje) #0
        else:
            self.opA1.setCurrentIndex(indx)  # 0
            self.opcionesJoyEje[indx][1]=True
        indx = self.__getKeyfromValue(self.opcionesJoyEje,mapeo[14])
        if indx == None:
            self.opA2.setCurrentIndex(blankEje) #0
        else:
            self.opA2.setCurrentIndex(indx)  # 0
            self.opcionesJoyEje[indx][1]=True
        indx = self.__getKeyfromValue(self.opcionesJoyEje,mapeo[15])
        if indx == None:
            self.opA3.setCurrentIndex(blankEje) #0
        else:
            self.opA3.setCurrentIndex(indx)  # 0
            self.opcionesJoyEje[indx][1]=True


        if mapeo[16] == "":
            self.invA0.setChecked(False)

        else:

            self.invA0.setChecked(bool(mapeo[16]))
            self.ejesInvertidos[0]=bool(mapeo[16])

        if mapeo[17] == "":
            self.invA1.setChecked(False)
        else:
            self.invA1.setChecked(bool(mapeo[17]))
            self.ejesInvertidos[1]=bool(mapeo[17])

        if mapeo[18] == "":
            self.invA2.setChecked(False)
        else:
            self.invA2.setChecked(bool(mapeo[18]))
            self.ejesInvertidos[2]=bool(mapeo[18])

        if mapeo[19] == "":
            self.invA3.setChecked(False)
        else:
            self.invA3.setChecked(bool(mapeo[19]))
            self.ejesInvertidos[3]=bool(mapeo[19])

    def mapeoJoystick(self,txt):

        QComboBox = QtGui.QApplication.focusWidget()



        objectName = QComboBox.objectName()


        if objectName in ["opA0", "opA1", "opA2", "opA3"]:
            newAction = QComboBox.currentIndex()

            if self.opcionesJoyEje[QComboBox.currentIndex()][1] == False:


                self.opcionesJoyEje[QComboBox.previusIndex()][1] = False
                if self.opcionesJoyEje[QComboBox.currentIndex()][0] != "":
                    self.opcionesJoyEje[newAction][1] = True

                if  objectName == "opA0":
                    self.Joystick.agr_mapeo(12, QComboBox.currentText())
                if  objectName == "opA1":
                    self.Joystick.agr_mapeo(13, QComboBox.currentText())
                if  objectName == "opA2":
                    self.Joystick.agr_mapeo(14, QComboBox.currentText())
                if  objectName == "opA3":
                    self.Joystick.agr_mapeo(15, QComboBox.currentText())

            else:
                QComboBox.setCurrentIndex(QComboBox.previusIndex())


        elif objectName in ["cone_op1", "cone_op2", "cone_op3", "cone_op4"]:
            newAction = QComboBox.currentIndex()

            if self.opcionesJoyBtn[QComboBox.currentIndex()][1] == False:

                self.opcionesJoyBtn[QComboBox.previusIndex()][1] = False

                if self.opcionesJoyBtn[QComboBox.currentIndex()][0] != "":
                    self.opcionesJoyBtn[newAction][1] = True

                if  objectName == "cone_op1":
                    self.Joystick.agr_mapeo(0, QComboBox.currentText())
                if  objectName == "cone_op2":
                    self.Joystick.agr_mapeo(1, QComboBox.currentText())
                if  objectName == "cone_op3":
                    self.Joystick.agr_mapeo(2, QComboBox.currentText())
                if  objectName == "cone_op4":
                    self.Joystick.agr_mapeo(3, QComboBox.currentText())
            else:
                QComboBox.setCurrentIndex(QComboBox.previusIndex())

        elif objectName in ["invA0", "invA1", "invA2", "invA3"]:
            # print self.ejesInvertidos

            if objectName == "invA0":
                self.Joystick.agr_mapeo(16, QComboBox.isChecked())
                self.ejesInvertidos[0]= QComboBox.isChecked()
            if objectName == "invA1":
                self.Joystick.agr_mapeo(17, QComboBox.isChecked())
                self.ejesInvertidos[1] = QComboBox.isChecked()
            if objectName == "invA2":
                self.Joystick.agr_mapeo(18, QComboBox.isChecked())
                self.ejesInvertidos[2] = QComboBox.isChecked()
            if objectName == "invA3":
                self.Joystick.agr_mapeo(19, QComboBox.isChecked())
                self.ejesInvertidos[3] = QComboBox.isChecked()
            # print self.ejesInvertidos


