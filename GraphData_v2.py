#!/usr/bin/python
#-*- coding: utf-8 -*-
# Modulo de gráficos de BEcopter

__author__ = "Eric Bastida"


import sys
from PyQt4 import QtGui, QtCore

import numpy as np
import random
import pyqtgraph as pg


class funcion():

    def __init__(self,parent = None,intervalo=100,maxIntervalos = 10, id = -1,color=(0,0,255),startTime=0):
        # En realidad una grafica va a estar compuesta por varias curvas (DataItemplot) concatenadas por intervalos
        # para una mejor optimizacion de memoria. Ya que cuando llegue a cierto limite se procederá a eliminar
        # intervalos viejos
        self._curvas = []
        self._curva = parent.plot()
        self._puntero = 0
        self._indx = 0
        self._intervalo = intervalo
        self._id = id
        self._color = color

        self._parent = parent
        self._data = np.zeros((intervalo + 1, 2))
        self._buffer = np.zeros((1,1))

        self._maxIntervalos = maxIntervalos
        self._starTime = startTime


    def addData(self,data):
        "Funcion que agrega informacion en un buffer para luego ser mostrada"
        # print "Ahora si, tengo datos jeje", data
        self._buffer = np.append(self._buffer,np.array([data]))

    @property
    def color(self):
        return self._color
    @property
    def interval(self):
        return self._intervalo
    @property
    def starTime(self):
        return self._starTime

    def delete(self):
        "Funcion que liminara la funcion en pantalla "
        while len(self._curvas) > 0:
            c = self._curvas.pop(0)
            self._parent.removeItem(c)

    def update(self):
        "Funcion encargada de actualizar por cada iteración del loop principal (timer) los valores de las funciones almacenadas"

        now = pg.ptime.time()

        for curva in self._curvas:
            curva.setPos(-(now-self._starTime), 0)


        # Indice que va desde [0 , self._intervalo -1]
        i = self._indx % self._intervalo

        if i == 0:
            curva = self._parent.plot()
            curva.setPen(pg.mkPen(self._color, width=2))

            self._curvas.append(curva)

            ultimo = self._data[-1]

            self._data = np.empty((self._intervalo+1,2))

            self._data[0] = ultimo

            while len(self._curvas) > self._maxIntervalos:
                c = self._curvas.pop(0)
                self._parent.removeItem(c)
        else:

            curva = self._curvas[-1]

        self._data[i+1,0] = now - self._starTime
        # Pregunto si existe datos almacenados en el buffer

        if len(self._buffer) > 0:

            # En caso de encontrar datos, se procede a concatenarlo y eliminar dicho elemento del buffer
            self._data[i+1,1] = self._buffer[0]
            self._buffer = np.delete(self._buffer,0)

        else:
            # Caso contrario se agrega un nuevo dato igual a cero (con el fin de ver que no se estan llegando datos)
            # Arreglado: Si pongo cero la frecuencia de muestreo es mayor a la reposiciòn de valores provenientes del vehiculo
            # self._data[i + 1, 1] =self._data[i , 1]
            self._data[i + 1, 1] = np.random.normal()

        curva.setData(x=self._data[:i + 2, 0], y=self._data[:i + 2, 1])


        self._indx += 1



class Grafico2(pg.PlotWidget):
    """

    Objeto: PlotWidget

    Descripción: Clase encargada de graficar los datos(curvas) que se van agregando.

    newversion: La version anterior de esta clase utilizaba matplotlib, la cual contraría problemas
    visuales al mostrar los datos en el Widget correspondiente.

    """

    def __init__(self, parentWidget=None,interval = 100,maxLines = 5):
        super(Grafico2, self).__init__(parent=parentWidget, name= 'Graph Data')


        # --- Parametros de la la figura ---
        # Numero maximo de lineas a graficar
        self.maxLines = maxLines
        # Intervalo del rango de datos a mostrar en el eje x.
        self.interval = interval
        # Contador de intervalor

        # Tiempo maximo mostrado en pantalla actualmente
        self.t = interval

        # Luego de pasar este valor se empiezan a eliminar informacion (Optimización)
        self.maxIntervalos = 10


        self.timer = QtCore.QTimer(parentWidget)
        self.timer.timeout.connect(self.updateFigure)
        # self.timer.timeout.connect(self.updateFigure)

        self.Colors = [(0, 0.56, 0.83, 1), (0.98, 0.30, 0.18, 1), (0.89, 0.68, 0.21, 1), (0.42, 0.56, 0.30, 1), (0.45, 1, 0.54, 1)]
        self._scalingColorsTo(255)

        self.indxColor = 1

        self.setLabel('bottom', 'Tiempo', 's')
        self.setXRange(-10, 0)


        self._lines = dict() #Diccionario que contiene todas las lineas con su correspondiente identificacion (ID)

        # self.init_figure()



    def init_figure(self):
        # Mostramos una grilla en y
        self.showGrid(x=False,y=True)

        # Obtenemos el tiempo de inicio (para iniciar una funcion de prueba) ya que este parametro es necesario
        startTime = pg.ptime.time()
        # La primera linea para mostrar de ejemplo
        self._lines[0] = funcion(parent=self,startTime=startTime)


    def play(self,flag):
        if flag:
            self.timer.start(50)
        else:
            self.timer.stop()


    def removeLine(self,id):
        # print self._lines.keys()
        if self._lines.has_key(id):
            # print "Eliminated", id
            self._lines[id].delete()
            del self._lines[id]



    def addData(self,id=None,data=None):
        """
        Funcion que agrega informacion para graficar, segun los id (Tratar que sea en orden creciente)
                id = Identificador de la linea
                data = Informacion a graficar, deben ser datos individuales

        Descripcion: Esta funcion buscara en la base de lineas almacenada si se encuentra el id especificado,
        en caso de no encontrarla agregara una linea nueva para graficar, teniendo las siguientes restricciones:
            1_ Si el numero maximo de lineas para almacenar esta en su cupo maximo, eliminara la linea con id de
            de menor valor.
            2_ En caso de sobrar espacio, se agregara una nueva linea con su correspondiente id en la base de datos.
        """
        # Esta variable informará que linea se borro en caso de llegar al cupo maximo
        keyLine = -1
        #Si el id no tiene nada hay que actualizar los valores
        # print "Viniste a agregar info puto", id , data
        if  id == None:
            # Cada vez que se actualiza cada funcion/linea se mostrara un valor nulo, es decir cero.
            for l in self._lines:
                l.update()

            self.t += 1

        elif  self._lines.has_key(id):
            # print "Esto tengo ahora : "
            #Si el id de la linea está en la base de datos se agregan los nuevos valores
            # print "Agregaste a algo ya creado"
            self._lines[id].addData(data)

            # xdata = np.append(xdata,range(xdata[-1], ) # FIX - No tiene en cuenta si data es una lista de valores nuevos
            # self.t += 1
            # ydata= np.append(ydata,data)
            # self._lines[id].set_data(xdata,ydata)
        else:
            #En caso de no estar el id, o es un id nuevo y valido, se lo agregará a la base de datos, en caso de sobrepasar
            #la cantidad máxima, se eliminará la primera linea ingresada...

            # LINE = Line2D.Line2D(self.CurrentXAxis,np.array(ydata), color=self.colores())
            startTime = pg.ptime.time()
            LINE = funcion(parent=self,id=id,color=self.colores(),startTime=startTime)
            if self._lines.__len__() >= self.maxLines:
                keyLine = self._lines.keys()[0]  #Retorna el id que se eliminó ya que se completo la cantidad máxima
                # print "Te fuiste por gil"
                self._lines[self._lines.keys()[0]].delete()
                del self._lines[self._lines.keys()[0]]
            # print "Nueva linea con datos"
            LINE.addData(data)
            self._lines[id] = LINE
            # print "Ahora tenemos ", len(self._lines), " lineas"


        return keyLine


    def updateFigure(self):
        # self.setRange(padding=1)
        for iline in self._lines:
            self._lines[iline].update()


    def getCurrentIds(self):
        return self._lines.keys()

    def colores(self):

        Color = self.Colors[self.indxColor]

        self.indxColor += 1
        if self.indxColor >= self.Colors.__len__():
            self.indxColor = 0

        return Color

    def _scalingColorsTo(self,scale=255):
        "Funcion encargada de multiplicar los valores normalizados de los componentes de los colores a mostrar"
        # Scaling colors values
        self.Colors =tuple(tuple(int(i *scale) for i in inner) for inner in self.Colors)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_widget = QtGui.QWidget()
    l = QtGui.QVBoxLayout(main_widget)
    graph = Grafico2(parentWidget=main_widget)
    graph.play(True)
    l.addWidget(graph)
    main_widget.show()
    sys.exit(app.exec_())