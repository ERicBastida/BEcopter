#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

import numpy as np
import matplotlib
matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import random
import matplotlib.lines as Line2D





class Grafico(FigureCanvas):

    def __init__(self, parent=None,interval = 100,maxLines = 5):
        plt.style.use('ggplot')
        # plt.style.use('ERic_style')
        self.maxLines = maxLines #Numero maximo de lineas a graficar
        self.interval = interval
        self.t = interval #Tiempo maximo mostrado en pantalla actualmente
        self.t_front = 20 #Tiempo extra adicional para poder visualizar los nuevos valores en la imagen
        self.ymax = 1.65
        self.ymin = -1.65
        self.fig = plt.figure(1)
        self.ax = self.fig.add_subplot(111)
        self.ax.grid(True)
        super(Grafico, self).__init__(figure=self.fig)
        self.setParent(parent)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateFigure)

        self.Colors = [(0, 0.56, 0.83, 1), (0.98, 0.30, 0.18, 1), (0.89, 0.68, 0.21, 1), (0.42, 0.56, 0.30, 1), (0.45, 1, 0.54, 1)]
        self.indxColor = 1
        self.lines = dict() #Diccionario que contiene todas las lineas con su correspondiente identificacion (ID)

        self.init_figure()

    def init_figure(self):
        self.lines = dict()

        xaxis = np.arange(0, self.interval, 1)
        self.values = [0]*self.interval

        yaxis = np.array(self.values)
        self.ax.set_title("Realtime Signal Plot")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Amplitude")
        self.CurrentXAxis = np.arange(len(self.values) - self.interval, len(self.values), 1)
        self.ax.axis([0, self.t + self.t_front , self.ymin, self.ymax])


        LINE = Line2D.Line2D(xaxis,yaxis,color=self.colores()) #Linea temporal....

        self.ax.add_line(LINE)

        self.lines[0]=LINE


    def play(self,flag):
        if flag:
            self.timer.start(5)
        else:
            self.timer.stop()


    def removeLine(self,id):
        if self.lines.has_key(id):
            del self.lines[id]



    def addData(self,id=None,data=None):
        """Funcion que agrega informacion para graficar, segun los id (Tratar que sea en orden creciente)
                id = Identificador de la linea
                data = Informacion a graficar, deben ser datos individuales

        Descripcion: Esta funcion buscara en la base de lineas almacenada si se encuentra el id especificado,
        en caso de no encontrarla agregara una linea nueva para graficar, teniendo las siguientes restricciones:
            1_ Si el numero maximo de lineas para almacenar esta en su cupo maximo, eliminara la linea con id de
            de menor valor.
            2_ En caso de sobrar espacio, se agregara una nueva linea con su correspondiente id en la base de datos.
        """

        keyLine = -1
        #Si el id no tiene nada hay que actualizar los valores
        if  id == None:
            for l in self.lines:
                ydata = self.lines[l].get_ydata()
                xdata = self.lines[l].get_xdata()

                xdata = np.append(xdata, xdata[-1] + 1)  # FIX - No tiene en cuenta si data es una lista de valores nuevos
                ydata = np.append(ydata, ydata[-1])

                #En este caso (cuando no se pasan argumentos) únicamente se actualizan todas las lineas con su ultimo valor.
                #para simular el movimiento continuo de la linea a traves del tiempo.
                self.lines[l].set_data(xdata, ydata)

            self.t += 1

        elif  self.lines.has_key(id):
            #Si el id de la linea está en la base de datos se agregan los nuevos valores
            ydata = self.lines[id].get_ydata()
            xdata = self.lines[id].get_xdata()
            xdata = np.append(xdata,xdata[-1]+1) # FIX - No tiene en cuenta si data es una lista de valores nuevos
            # xdata = np.append(xdata,range(xdata[-1], ) # FIX - No tiene en cuenta si data es una lista de valores nuevos
            self.t += 1
            ydata= np.append(ydata,data)
            self.lines[id].set_data(xdata,ydata)
        else:#En caso de no estar el id, o es un id nuevo y valido, se lo agregará a la base de datos, en caso de sobrepasar
            #la cantidad máxima, se eliminará la primera linea ingresada...


            ydata =  [0]*(self.interval-1) + [data]

            LINE = Line2D.Line2D(self.CurrentXAxis,np.array(ydata), color=self.colores())
            if self.lines.__len__() >= self.maxLines:
                keyLine = self.lines.keys()[0]  #Retorna el id que se eliminó ya que se completo la cantidad máxima
                del self.lines[self.lines.keys()[0]]

            self.lines[id] = LINE




        self.CurrentXAxis = np.arange(self.t - self.interval, self.t, 1)

        return keyLine


    def updateFigure(self):

        self.ax.clear()
        self.addData()
        self.ax.grid(True)
        for ikey in self.lines: #Actualizo los valores de todas las lineas almacenadas
            self.ax.add_line(self.lines[ikey])

        self.ax.axis([self.CurrentXAxis.min(), self.CurrentXAxis.max()+self.t_front , -1.5, 1.5])
        self.draw()
    def getCurrentIds(self):
        return self.lines.keys()

    def colores(self):

        Color = self.Colors[self.indxColor]

        self.indxColor += 1
        if self.indxColor >= self.Colors.__len__():
            self.indxColor = 0

        return Color


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_widget = QtGui.QWidget()
    l = QtGui.QVBoxLayout(main_widget)
    graph = Grafico(main_widget)

    l.addWidget(graph)
    main_widget.show()
    sys.exit(app.exec_())