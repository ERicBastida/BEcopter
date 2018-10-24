#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
__autor__   = 'ERic Bastida'
__project__ = 'Proyecto Final de Carrera - Ingeniería en Informática'

import  GUI_becopter, Vehiculo
from PyQt4 import QtCore, QtGui



class pConfiguracion(QtGui.QMainWindow, GUI_becopter.Ui_MainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.btnGuardarParam.clicked.connect(self.guardarParametros)
        self.btnRestaurarParam.clicked.connect(self.cargarParametros2)
        # self.listParametros.cellClicked.connect(self.clickListParam)
        self.ListGP = []

    def cargarParametros2(self):
        INDEX = self.tabConfiguracion.currentIndex()
        # print "Implementar una restauracion"
        # self.cargarParametros(INDEX)
        #Que cuando cargue el valor del parametro obtenido del vehiculo, este debe ser guardado en un atributo de Parametro

    def cargarParametros(self, indx = None):
        """
            -*Función que carga los parametros almacenados en el archivo y los carga en sus correspondientes tab*-
            indx = None -> Carga todos los parametros en en todas las tabs/pestañas. Esto se hace al inicio del programa cuando se establece una conexión y para restaurar (En caso de ser necesario)..
            indx = #    -> Carga los parametros de la pestaña correspondiente al indx.
        """
        #Cuando haga esto, tengo que hacer una lista de GestParametros que sea de la misma cantidad de pestañas que tenga en la configuracion
        ntabs = self.tabConfiguracion.count()
        toPlay = []


        if indx == None:#Si el indx FIX - Esto esta re mal, solamente al recargar debe cargar de nuevlo los valores del parametro (que es lo único editable)
            for hoja in range(ntabs):
                self.ListGP.append(Parametros.GestParametros("data/configParameters.xlsx",hoja))    # Lista de gestores de parametros (Correspondiente a cada pestaña)
            n = 0
            for l in self.ListGP:
                if l != []:
                    n +=1
            toPlay = range(n)

        else:
            self.ListGP = [Parametros.GestParametros("data/configParameters.xlsx", indx)]  # Cargo la informacion perteneciente a los parametros de "ArduPilot Parameters"
            if self.ListGP[0].getParams() == []:
                toPlay = []
            else:
                toPlay = [indx]


        for iGP in toPlay:
            LP = self.ListGP[iGP].getParams() #Lista de Parametros (LP)
            tab = self.tabConfiguracion.widget(iGP)  # Voy recorriendo las pestañas y voy obteniendos sus correspondientes tablas

            tab = tab.children()[1]
            tab.setRowCount(0)


            for p in range(LP.__len__()):

                tab.insertRow(p)


                tab.setItem(p,0,QtGui.QTableWidgetItem(LP[p].getCode()))
                tab.setItem(p,1,QtGui.QTableWidgetItem(LP[p].getName()))

                tab.setItem(p,2,QtGui.QTableWidgetItem(LP[p].getDescription()))
                value = self.qcopter.v.parameters[LP[p].getCode()]
                tab.setItem(p,4,QtGui.QTableWidgetItem(str(value)))

                if LP[p].hasRange():
                    slice = QtGui.QSlider(0x1)
                    r1,r2 = LP[p].getRange()
                    slice.setRange(r1,r2)
                    slice.setSingleStep(LP[p].getIncrement())
                    slice.valueChanged.connect(self.moveSliderParam)
                    # slice.setTickPosition(QtGui.QSlider.Tick)
                    tab.setCellWidget(p,3,slice)

                    tab.setItem(p, 5, QtGui.QTableWidgetItem(LP[p].getUnits()))

    def guardarParametros(self):

        # print "Vamos por partes, entraste?"

        tab = self.tabConfiguracion.widget(self.tabConfiguracion.currentIndex())
        tab = tab.children()[1]                     #Con esto obtengo la tabla que esta adentro del tab seleccionado
        nRows = tab.rowCount()

        for r in range(nRows):
            code = tab.item(r,0) #Obtengo el widget que tiene el codigo
            code = str(code.text()) #Obtengo el código (texto)

            value = tab.item(r,4) #Obtengo el widget que tiene el valor del parametro modificado
            value = float(value.text())              #Obtengo el valor modificado
            # print "code: ",type(code),code,". Value: ",type(value), value
            self.qcopter.v.parameters[code] = value  #Lo guardo en los parametros del vehículo

    def moveSliderParam(self,value):
        clickme = QtGui.QApplication.focusWidget()
        i = self.tableArduPilot.indexAt(clickme.pos())
        fila = i.row()

        tab = self.tabConfiguracion.widget(self.tabConfiguracion.currentIndex())
        tab =  tab.children()[1]
        tab.setItem(fila,4,QtGui.QTableWidgetItem(str(value)))
        # self.tableArduPilot
