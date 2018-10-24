#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
import math
import random
import time

from PyQt4 import QtCore, QtGui, QtOpenGL


try:
    from OpenGL.GL import *
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL overpainting",
            "PyOpenGL must be installed to run this example.")
    sys.exit(1)



class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers), parent)

        self.setAutoBufferSwap(True)

        midnight = QtCore.QTime(0, 0, 0)
        random.seed(midnight.secsTo(QtCore.QTime.currentTime()))

        self.object = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.image = QtGui.QImage()
        self.bubbles = []
        self.lastPos = QtCore.QPoint()



        self.animationTimer = QtCore.QTimer()
        self.animationTimer.setSingleShot(False)
        self.animationTimer.timeout.connect(self.animate)
        self.animationTimer.start(3)

        self.setAutoFillBackground(False)
        self.setMinimumSize(400, 300)
        self.setWindowTitle("Prueba HUD")

        loadedFontID = QtGui.QFontDatabase.addApplicationFont("./fonts/Agency.ttf")
        self.fontName = "Agency"

        self.trolltechGreen = QtGui.QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QtGui.QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

            # Colores
        self.cCielo = QtGui.QColor(3, 190, 255 )
        self.cPiso = QtGui.QColor(8, 122, 1 )

        self.black = QtGui.QColor(0,0,0)
        self.brown = QtGui.QColor(99, 56, 7)
        self.white = QtGui.QColor(255,255,255)
        self.red = QtGui.QColor(255,0,0)

        self.capa0 = 0.0
        self.capa1 = 0.1
        self.capa2 = 0.15

        # Informacion a mostrar

        self.__gps = 0
        self.__is_ok_gps = False
        self.__signal = 0 #Porcentaje
        self.__bateria = 0 #Porcentaje
        self.__altitud = 0
        self.__heading = 0
        self.__pitch = 0
        self.__roll = 0
        self.__info = "AUTO"
        self.__nameinfo = ""
        self.__sta = "STATUS"
        self.__armed = False
        self.__joystick = False
        self.__preArm = False
        self.__preArmAlpha = 255

        # Imagenes: Se las carga aqui con el objetivo de optimizar el rendimiento de la aplicacion

        self._picGPS_ok =  QtGui.QPixmap("img/status/gps.png")
        self._picGPS_nok = QtGui.QPixmap("img/status/gps_nok.png")

        self._picbat_DC = QtGui.QPixmap("img/status/bateria/batDC.png")
        self._picbat_10 = QtGui.QPixmap("img/status/bateria/bat10.png")
        self._picbat_20 = QtGui.QPixmap("img/status/bateria/bat10.png")
        self._picbat_30 = QtGui.QPixmap("img/status/bateria/bat10.png")
        self._picbat_40 = QtGui.QPixmap("img/status/bateria/bat10.png")
        self._picbat_50 = QtGui.QPixmap("img/status/bateria/bat10.png")
        self._picbat_60 = QtGui.QPixmap("img/status/bateria/bat10.png")
        self._picbat_70 = QtGui.QPixmap("img/status/bateria/bat10.png")
        self._picbat_80 = QtGui.QPixmap("img/status/bateria/bat10.png")
        self._picbat_90 = QtGui.QPixmap("img/status/bateria/bat10.png")
        self._picbat_100 = QtGui.QPixmap("img/status/bateria/bat10.png")

        self._picComp = QtGui.QPixmap("img/compassRose.png")
        self._picQcopter = QtGui.QPixmap("img/qcopter.png")

        self._indicador = QtGui.QPixmap("img/indicador")

        self._barra_ind = QtGui.QPixmap("img/barra")

        self._picjoy = QtGui.QPixmap("img/status/joystick_ico.png")

        self._picsig_nok = QtGui.QPixmap("img/status/senal/no_signal.png")
        self._picsig_10 = QtGui.QPixmap("img/status/senal/signal10.png")
        self._picsig_20 = QtGui.QPixmap("img/status/senal/signal20.png")
        self._picsig_60 = QtGui.QPixmap("img/status/senal/signal60.png")
        self._picsig_80 = QtGui.QPixmap("img/status/senal/signal80.png")
        self._picsig_100 = QtGui.QPixmap("img/status/senal/signal100.png")

        self._fondo = QtGui.QPixmap("fondo.PNG")

        # self._fondo2 = QtGui.QImage("img/fondo")


    #Se definen los setters, ya que se utilizaran en los callback de parametros a mostrar
    def setGPS(self,gps,is_ok ):
        self.__is_ok_gps = is_ok
        self.__gps=gps

    def setArmed(self,armed):
        self.__armed = armed

    def setPreArm(self,preArm):
        self.__preArm = preArm
    def setJoystick(self,is_joystick):
        self.__joystick = is_joystick

    def setSignal(self,signal):
        self.__signal=signal

    def setBattery(self,bat):
        self.__bateria=bat

    def setHeading(self,oVehicle,nameParam, head):

        self.__heading=-1*head + 360

    def setPitch(self,pitch):
        self.__pitch = pitch

    def setRoll(self,roll):
        self.__roll = roll

    def setStatus(self,sta,error =False):
        """
        Funcion que recibe el estado el cual se quiere mostrar en pantalla y ademas pudiendo elegir el color del mismo
        Rojo cuando error = True
        Blanco cuando error = False

        :param sta: Texto que se quiere mostrar en pantalla
        :param error: Variable booleana que determina el color del texto (error = True -> Rojo , error = False -> Blanco)
        :return:
        """
        self.__sta = sta
        self.__error_sta = error

    def setInfo(self,nameinfo,info):
        "Función que muestra la información en pantalla en la parte inferior-derecha"
        self.__info =info
        self.__nameinfo =nameinfo

    def __setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle

    def __setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle

    def __setZRotation(self, angle):

        angle = self.normalizeAngle(angle)

        if angle != self.__roll:
            self.__roll = angle

    def __setRotCompas(self, angle):

        angle = self.normalizeAngle(angle)

        if angle != self.__heading:
            self.__heading = angle

    def __setRotAlt(self, angle):

        if angle > 360:
            angle = 0
        elif angle < 1:
            angle = 360

        if angle != self.__pitch:
            self.__pitch = angle

    def initializeGL(self):

        pass

    def paintEvent(self, event):
        self.makeCurrent()
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_LINE_SMOOTH)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()

        # self.qglClearColor(self.red)
        glClearColor(0, 0, 0, 0)
        self.setupViewport(self.width(), self.height())
        self.pintor = QtGui.QPainter(self)
        # self.drawHorizonteArt()
        self.makeObject()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def makeObject(self):

        self.aux = ""
        self.upDown = 0
        self.radius = 0
        self.rot = self.__roll
        # self.rot = self.__roll/16

        self.fontSize = 0.04*min(self.height(),self.width())

        self.origenDy  = QtCore.QPointF(0,-self.height()*0.1)
        self.origenCen = QtCore.QPointF(self.width()/2,self.height()/2)
        self.origenLB  = QtCore.QPointF(0,self.height())


        self.pintor.setRenderHint(QtGui.QPainter.Antialiasing)
        # self.drawHorizonteArt(self.__pitch)


        self.pintor.save()
        self.pintor.translate(self.origenLB)
        self.pintor.scale(1.0,-1.0,) # Posicionando el origen izquierda-abajo

        #Posicionamos el origien en el centro de la pantalla temporalmente para imitar la direccion de la vista
        self.pintor.translate(self.origenCen)
        # self.pintor.translate(0,self.__pitch)
        self.pintor.rotate(self.rot)

        self.pintor.translate(self.origenCen*-1)

        #@fixme: Optimizar esta funcion

        # self.drawHorizonteArt_opt(self.__pitch)

        # ------------------  Origen en el centro de pantalla   ------------------
        self.pintor.translate(self.origenCen)

        self.drawLinesHorizonte()
        self.drawAnguloBanco()



        self.pintor.restore()

        # -------------      Origen en el lado izquierdo superior y fijo    ------------------------
        self.setAltura()


        #-----  Rectangulo superior ---------

        if 300 <= self.rot or self.rot <= 60:
            self.drawIndicator()
        self.drawLineRef()

        self.rectSupAlt = self.height()*0.1

        infoRect = QtCore.QRect(0,0,self.width(),self.rectSupAlt )

        self.pintor.setPen(QtGui.QColor(0,0,0,0))

        self.pintor.drawRect(infoRect)

        sizeIcons = QtCore.QSize(int(self.width()*0.1),int(self.rectSupAlt*0.7))
        self.drawSignal(sizeIcons)
        self.drawBateria(sizeIcons)
        self.drawGPS(sizeIcons)

        self.drawCompassRose()
        self.drawStatus()
        self.drawArmed()
        self.drawPreArm()
        self.drawJoystick(sizeIcons)
        self.pintor.end()

    def drawJoystick(self,sizePix):
        """
        Funcion encargada de dibujar un joystick en la parte inferior central de la pantalla
            siempre y cuando la variable booleana lo permita
        :param sizePix : Objeto que tiene el tamaño de referencia
        :type QSize

        """
        if self.__joystick:

            sizePix.setHeight(sizePix.height()*5)
            ancho =sizePix.width()*2
            alto = sizePix.height()*1.5

            picjoy = self._picjoy .scaled(ancho,alto, QtCore.Qt.KeepAspectRatio)

            self.pintor.drawPixmap(QtCore.QPoint(self.width()*0.5-ancho*0.5, self.height()-ancho*0.7), picjoy)

    def drawPreArm(self):

        if  (self.__preArm):
        # if  (True):
            if (self.__preArmAlpha < 10):
                self.__preArm = False
                self.__preArmAlpha = 255

            self.pintor.save()
            self.pintor.setFont(QtGui.QFont(self.fontName, self.fontSize))
            punto = QtCore.QPoint(0, 0)
            self.pintor.setPen(QtGui.QColor.fromRgb(255, 0, 0, self.__preArmAlpha))
            # drawText(int x, int  y, int  width, int     height, int        flags, const        # QString & text, QRect * boundingRect = 0)
            self.pintor.drawText(self.width() * 0.05, self.height() * 0.885, self.width() * 0.5, self.height() * 0.2,
                                 QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop, "PREARM")
            self.__preArmAlpha -= 10
            self.pintor.restore()

    def drawArmed(self):

        if not(self.__armed):
            self.pintor.save()
            self.pintor.setFont(QtGui.QFont(self.fontName,self.fontSize))
            punto = QtCore.QPoint(0, 0)
            self.pintor.setPen(QtGui.QColor.fromRgb(255,0,0,255))
            # drawText(int x, int  y, int  width, int     height, int        flags, const        # QString & text, QRect * boundingRect = 0)
            self.pintor.drawText(self.width()*0.25,self.height()*0.44,self.width()*0.5,self.height()*0.2,QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop, "DESARMADO" )
            self.pintor.restore()

    def drawStatus(self):

        pencil = QtGui.QPen(self.white)
        pencil.setWidth(2)
        self.pintor.setPen(pencil)
        self.pintor.setFont(QtGui.QFont(self.fontName,self.fontSize))
        punto = QtCore.QPoint(self.width() * 0.1, self.height() * 0.07)

        self.pintor.drawText(punto,self.__sta)

    def drawSignal(self,sizePix):
        "Funcion encargada de graficar el nivel de señal según el valor de la señal almacenada"

        picsignal = self._picsig_nok

        if 0 < self.__signal <= 10:
            picsignal = self._picsig_10
        if 10 < self.__signal <= 20:
            picsignal = self._picsig_20
        if 20 < self.__signal <= 60:
            picsignal = self._picsig_60
        if 60 < self.__signal <= 80:
            picsignal = self._picsig_80
        if 80 < self.__signal <= 100:
            picsignal = self._picsig_100

        picsignal = picsignal.scaled(sizePix, QtCore.Qt.KeepAspectRatio)

        self.pintor.drawPixmap(QtCore.QPoint(self.width() - sizePix.width() * 1, 5), picsignal)

    def drawBateria(self,sizePix):

        picbat = self._picbat_DC


        if 0 < self.__signal <= 10:
            picbat = self._picbat_10
        if 10 < self.__signal <= 20:
            picbat = self._picbat_20
        if 20 < self.__signal <= 30:
            picbat = self._picbat_30
        if 30 < self.__signal <= 40:
            picbat = self._picbat_40
        if 40 < self.__signal <= 50:
            picbat = self._picbat_50
        if 50 < self.__signal <= 60:
            picbat = self._picbat_60
        if 60 < self.__signal <= 70:
            picbat = self._picbat_70
        if 70 < self.__signal <= 80:
            picbat = self._picbat_80
        if 80 < self.__signal <= 90:
            picbat = self._picbat_90
        if 90 < self.__signal <= 100:
            picbat = self._picbat_100

        picbat = picbat.scaled(sizePix, QtCore.Qt.KeepAspectRatio)
        self.pintor.drawPixmap(QtCore.QPoint(self.width() - sizePix.width() * 2, 5), picbat)

    def drawGPS(self,sizePix):
        if self.__is_ok_gps:
            picGPS = self._picGPS_ok
        else:
            picGPS = self._picGPS_nok

        picGPS = picGPS.scaled(sizePix, QtCore.Qt.KeepAspectRatio)
        punto = QtCore.QPoint(picGPS.width()*0.25, self.rectSupAlt-picGPS.height()*1.2)
        self.pintor.drawPixmap(punto, picGPS)

    def drawCompassRose(self):
        "Funcion encargada de dibujar la orientacion del vehiculo respecto al polo norte-sur"

        pSize = 0.2 #Tamano proporcional al tama?o de la ventana
        nSize = QtCore.QSize(self.height()*pSize, self.height()*pSize)



        # recCompas = QtCore.QRect(0,self.height()-self.height()*pSize, self.height()*pSize, self.height())


        imgComp = self._picComp.scaled(nSize,transformMode=1)
        imgQcopter = self._picQcopter.scaled(nSize,transformMode=1)


        punto0 = QtCore.QPoint(0.5*self.height()*pSize,self.height()*(1-pSize*0.5))
        punto = QtCore.QPoint(0,self.height()*(1-pSize))


        self.pintor.setRenderHint(QtGui.QPainter.HighQualityAntialiasing,True)
        self.pintor.setBrush(QtGui.QColor(0,0,0,127))
        self.pintor.setPen(QtGui.QColor(0,0,0,255))


        self.pintor.drawEllipse(punto0,0.6*pSize*self.height(),0.6*pSize*self.height())

        self.pintor.drawPixmap(punto, imgQcopter)

        self.pintor.save()
        self.pintor.translate(punto0)

        self.pintor.rotate(self.__heading)

        self.pintor.translate(QtCore.QPoint(-0.5*self.height()*pSize,-self.height()*(1-pSize*0.5)))
        self.pintor.drawPixmap(punto, imgComp)

        self.pintor.restore()

    def setAltura(self):
        "Funcion que grafica un cuarto de circulo en la parte inferior-izquierda que contiene informaci?n de la altura"
        #Origen superior-izquierdo

        self.pintor.save()


        grad = QtGui.QLinearGradient(self.width()*0.5,0,self.width(),0)
        grad.setColorAt(0,QtGui.QColor(0,0,0,0))
        grad.setColorAt(1,QtGui.QColor(0,0,0,255))

        rectAltura = QtCore.QRectF(self.width()*(0.65),self.height()*(0.85), self.width()*0.35,self.height()*0.15)
        self.pintor.setPen(QtGui.QColor(0,0,0,0))

        self.pintor.fillRect(rectAltura,grad)
        self.pintor.drawRect(rectAltura)


        self.pintor.setPen(QtCore.Qt.white)
        fuente = QtGui.QFont(QtGui.QFont(self.fontName,self.fontSize*self.width()*0.002))
        self.pintor.setFont(fuente)

        # self.pintor.drawText(p,"Altura: "+str(self.__altitud)+" [mts]")
        self.pintor.drawText(rectAltura, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight ,self.__nameinfo +" "+ str(self.__info)+"   ")
        # "Pitch: "+str(360-self.__pitch)+self.aux +"  ")

        self.pintor.restore()

    def drawHorizonteArt(self,pitch=0):
        "Dibuja el horizonte artificial, mediante dos rectangulos que representan el cielo y la tierra, con fines orientativos."
        # Origen abajo-izquierda

        mSide = max(self.width(),self.height())

        # Ya que el dibujo sufrira rotaciones, al momento de este hecho, los cuadrados dejaran espacios libres en las esquinas,
        # por lo que se tendra que agregar un espacio de sobra (aux), con el objetivo de evitar este inconveniente.
        aux = 0.25*mSide


        self.pintor.save()


        self.pintor.scale(1.0, -1.0)
        self.pintor.translate(0.5*self.width(),-0.5*self.height()) #Origen en el centro de la pantalla


        # print self.height()

        factorReductor = 1
        anchoIMG = self.width()+4*aux
        anchoIMG = factorReductor*anchoIMG
        altoIMG = 2*4*self.height()
        altoIMG = factorReductor*altoIMG

        fondo = self._fondo.scaled(anchoIMG,altoIMG)
        pitch = 360 - pitch

        #Mapeo de la imagen
        if pitch <= 180:
            dy =  (pitch*2*self.height())/180
        else:
            dy = ((pitch % 180)- 180)*2*self.height()/180

        if pitch == 360:
            dy = 0

        self.aux = " / " + str(dy)




        self.pintor.save()
        self.pintor.translate(0,dy)
        self.pintor.drawPixmap(-0.5 * anchoIMG, -0.5 * altoIMG, fondo)
        self.pintor.restore()


        self.pintor.restore()

    def drawHorizonteArt_opt(self, pitch=0):
        "Dibuja el horizonte artificial, mediante dos rectangulos que representan el cielo y la tierra, con fines orientativos."
        # Origen abajo-izquierda
        origen = QtCore.QPointF(0, 0)
        ancho = self.width()
        alto = self.height()
        # print "Ancho y Alto " + str(ancho) + "  " + str(alto)
        self.pintor.save()
        self.pintor.translate(200, 200)
        self.pintor.drawImage(origen, self._fondo2)

        self.pintor.restore()
        # mSide = max(self.width(), self.height())
        #
        # # Ya que el dibujo sufrira rotaciones, al momento de este hecho, los cuadrados dejaran espacios libres en las esquinas,
        # # por lo que se tendra que agregar un espacio de sobra (aux), con el objetivo de evitar este inconveniente.
        # aux = 0.25 * mSide

        # self.pintor.save()

        # self.pintor.scale(1.0, -1.0)
        # self.pintor.translate(0.5 * self.width(), -0.5 * self.height())  # Origen en el centro de la pantalla

        # print self.height()

        # factorReductor = 1
        # anchoIMG = self.width() + 4 * aux
        # anchoIMG = factorReductor * anchoIMG
        # altoIMG = 2 * 4 * self.height()
        # altoIMG = factorReductor * altoIMG
        #
        # fondo = self._fondo.scaled(anchoIMG, altoIMG)
        # pitch = 360 - pitch
        #
        # # Mapeo de la imagen
        # if pitch <= 180:
        #     dy = (pitch * 2 * self.height()) / 180
        # else:
        #     dy = ((pitch % 180) - 180) * 2 * self.height() / 180
        #
        # if pitch == 360:
        #     dy = 0
        #
        # self.aux = " / " + str(dy)
        #
        # self.pintor.save()
        # self.pintor.translate(0, dy)
        # self.pintor.drawPixmap(-0.5 * anchoIMG, -0.5 * altoIMG, fondo)
        # self.pintor.restore()
        #
        # self.pintor.restore()

    def drawLinesHorizonte(self):
        "Dibuja lineas equiespaciadas con origen en el centro de la pantalla, con el fin de representar el pitch del veh?culo."
        self.pintor.setPen(QtCore.Qt.black)
        h= min (self.height(),self.width())
        eleva = {0:"-40",1:"-30",2:"-20",3:"-10",4:" 0 ",5:"10",6:"20",7:"30",8:"40",9:"*********"}
        # yini = int(0.25*h)
        yini = int(0.25*h)
        # yfin = int(0.75*h)
        yfin = -yini
        ystep = int(0.5*h/8)
        # print yini, yfin, ystep, h
        # ancho = int(0.05*self.width())
        ancho = int(0.05*h)
        indx = 0
        l = range(yfin,yini+ystep,ystep)

        for y in l:
             # y -= int(h/2) #Desplazamiento en caso de que el origen este abajo-izquierda
             factor = (math.fabs(y)/100)*h*0.05
             x1 = -ancho-factor
             x2 = -x1
             self.pintor.drawLine(x1, y, x2, y)

             self.pintor.save()
             self.pintor.translate(QtCore.QPointF(0,y))
             self.pintor.scale(1.0,-1.0)
             self.pintor.drawText(0.0,0,eleva[indx])
             self.pintor.restore()

             indx +=1
             if indx > 8:
                 break

    def drawIndicator(self):
        "Dibuja el indicador de indicar? la inclinaci?n o roll del vehiculo, seg?n el angulo de banco"


        t = min(self.width(), self.height())
        t = 0.1*t
        ind = self._indicador.scaled(QtCore.QSize(t * 2, t))

        self.pintor.drawPixmap(0.5*( self.width()-ind.width()), 0.5*self.height() - self.radius, ind)

    def drawLineRef(self):

        t = min(self.width(), self.height())
        t = 0.04 * t
        ind = self._barra_ind.scaled(QtCore.QSize(t*5 , t))

        self.pintor.drawPixmap(0, self.height()*0.5, ind)
        self.pintor.drawPixmap(self.width()-ind.width(), self.height()*0.5, ind)

    def drawAnguloBanco(self):
        h = min(self.width(),self.height())
        h = h*0.8
        x1 = -0.5*h
        x2 = -x1
        y2 = 0.5 * h
        y1 = -y2
        self.radius = (y2-y1)/2


        leftbutton = QtCore.QPointF(x1,y1)
        rightop = QtCore.QPointF(x2,y2)
        Arco = QtCore.QRectF(leftbutton,rightop)
        # self.pintor.fillRect(Arco,QtGui.QColor(0,0,0,127))

        startAngle = -30 * 16
        spanAngle = - 120 * 16
        stepAngle = spanAngle / 12

        pencil = QtGui.QPen(self.black)
        pencil.setWidth(2)
        self.pintor.setPen(pencil)
        self.pintor.drawArc(Arco, startAngle, spanAngle)

        startAngle =startAngle/16
        spanAngle = spanAngle /16
        stepAngle = spanAngle / 10

        self.pintor.setFont(QtGui.QFont(self.fontName,self.fontSize))
        domain = range(startAngle,spanAngle+startAngle + stepAngle,stepAngle)

        for angle in domain:
            angle = -angle*math.pi/180
            x1 = (h*0.5)*math.cos(angle)
            y1 = (h*0.5)*math.sin(angle)
            x2 = (h*0.52)*math.cos(angle)
            y2 = (h*0.52)*math.sin(angle)
            punto1 = QtCore.QPointF(x1,y1)
            punto2 = QtCore.QPointF(x2,y2)
            self.pintor.drawLine(punto1,punto2)
            self.pintor.save()
            self.pintor.translate(punto2)
            self.pintor.scale(1.0,-1.0)
            angle2 = (angle*180/math.pi)-90.0
            angle2 = math.trunc(angle2)


            if 180 < self.rot <= 300 and angle2 == 60:
                self.pintor.setPen(self.red)
                self.pintor.setFont(QtGui.QFont(self.fontName,self.fontSize*1.5))
            elif 180 >= self.rot >= 60 and angle2 == -60 :
                self.pintor.setFont(QtGui.QFont(self.fontName, self.fontSize * 1.5))
                self.pintor.setPen(self.red)
            else:
                self.pintor.setPen(self.black)

            if angle2 > 0:
                self.pintor.translate(-15,0)

            self.pintor.drawText(0.0,0.0,str(math.trunc(math.fabs(angle2))))
            self.pintor.restore()

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def resizeGL(self, width, height):
        self.setupViewport(width, height)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def animate(self):
        for bubble in self.bubbles:
            bubble.move(self.rect())

        self.update()

    def setupViewport(self, width, height):

        side = min(width, height)
        side2 = max(width,height)
        # self.resize(side2,side2)

        glViewport((side2 - side) / 2, (side2 - side) / 2, side, side)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        glMatrixMode(GL_MODELVIEW)



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = GLWidget()
    window.show()
    sys.exit(app.exec_())


