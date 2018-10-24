# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_becopter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1210, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../home/eric/.designer/backup/Icono BEcopter/BEcopter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setWhatsThis(_fromUtf8(""))
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setWhatsThis(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.Opciones = QtGui.QWidget(self.centralwidget)
        self.Opciones.setEnabled(True)
        self.Opciones.setWhatsThis(_fromUtf8(""))
        self.Opciones.setStyleSheet(_fromUtf8("background-color: rgb(20, 20, 20);"))
        self.Opciones.setObjectName(_fromUtf8("Opciones"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.Opciones)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btn_ayud = QtGui.QPushButton(self.Opciones)
        self.btn_ayud.setWhatsThis(_fromUtf8(""))
        self.btn_ayud.setAccessibleName(_fromUtf8(""))
        self.btn_ayud.setAccessibleDescription(_fromUtf8(""))
        self.btn_ayud.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);"))
        self.btn_ayud.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/Icono BEcopter/BEcopter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ayud.setIcon(icon1)
        self.btn_ayud.setIconSize(QtCore.QSize(80, 80))
        self.btn_ayud.setFlat(True)
        self.btn_ayud.setObjectName(_fromUtf8("btn_ayud"))
        self.verticalLayout_2.addWidget(self.btn_ayud)
        self.btn_Inic = QtGui.QPushButton(self.Opciones)
        self.btn_Inic.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Inic.sizePolicy().hasHeightForWidth())
        self.btn_Inic.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        self.btn_Inic.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_Inic.setFont(font)
        self.btn_Inic.setWhatsThis(_fromUtf8("<html>\n"
"<head/>\n"
"<body><p align=\"left\">adsfasd</p></body></html>"))
        self.btn_Inic.setAutoFillBackground(False)
        self.btn_Inic.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"    background-color: rgb(41, 116, 255);\n"
"\n"
"}\n"
"QPushButton {\n"
"text-align: center left;\n"
"border: 0px;\n"
"padding: 1px 1em;\n"
"}\n"
""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/img/leftbar/inicio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Inic.setIcon(icon2)
        self.btn_Inic.setIconSize(QtCore.QSize(64, 64))
        self.btn_Inic.setCheckable(True)
        self.btn_Inic.setChecked(True)
        self.btn_Inic.setFlat(True)
        self.btn_Inic.setObjectName(_fromUtf8("btn_Inic"))
        self.verticalLayout_2.addWidget(self.btn_Inic)
        self.btn_Cone = QtGui.QPushButton(self.Opciones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Cone.sizePolicy().hasHeightForWidth())
        self.btn_Cone.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.btn_Cone.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_Cone.setFont(font)
        self.btn_Cone.setWhatsThis(_fromUtf8(""))
        self.btn_Cone.setAutoFillBackground(False)
        self.btn_Cone.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"    background-color: rgb(41, 116, 255);\n"
"\n"
"}\n"
"QPushButton {\n"
"text-align: center left;\n"
"border: 0px;\n"
"padding: 1px 1em;\n"
"}\n"
""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/img/leftbar/conexion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Cone.setIcon(icon3)
        self.btn_Cone.setIconSize(QtCore.QSize(64, 64))
        self.btn_Cone.setCheckable(True)
        self.btn_Cone.setChecked(True)
        self.btn_Cone.setFlat(True)
        self.btn_Cone.setObjectName(_fromUtf8("btn_Cone"))
        self.verticalLayout_2.addWidget(self.btn_Cone)
        self.btn_coma = QtGui.QPushButton(self.Opciones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_coma.sizePolicy().hasHeightForWidth())
        self.btn_coma.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_coma.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_coma.setFont(font)
        self.btn_coma.setWhatsThis(_fromUtf8(""))
        self.btn_coma.setAutoFillBackground(False)
        self.btn_coma.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"    background-color: rgb(41, 116, 255);\n"
"\n"
"}\n"
"QPushButton {\n"
"text-align: center left;\n"
"border: 0px;\n"
"padding: 1px 1em;\n"
"}\n"
""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/img/leftbar/comando.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_coma.setIcon(icon4)
        self.btn_coma.setIconSize(QtCore.QSize(64, 64))
        self.btn_coma.setCheckable(True)
        self.btn_coma.setChecked(True)
        self.btn_coma.setFlat(True)
        self.btn_coma.setObjectName(_fromUtf8("btn_coma"))
        self.verticalLayout_2.addWidget(self.btn_coma)
        self.btn_conf = QtGui.QPushButton(self.Opciones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_conf.sizePolicy().hasHeightForWidth())
        self.btn_conf.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_conf.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_conf.setFont(font)
        self.btn_conf.setWhatsThis(_fromUtf8(""))
        self.btn_conf.setAutoFillBackground(False)
        self.btn_conf.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"    background-color: rgb(41, 116, 255);\n"
"\n"
"}\n"
"QPushButton {\n"
"text-align: center left;\n"
"border: 0px;\n"
"padding: 1px 1em;\n"
"}\n"
""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/img/leftbar/configuracion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_conf.setIcon(icon5)
        self.btn_conf.setIconSize(QtCore.QSize(64, 64))
        self.btn_conf.setCheckable(True)
        self.btn_conf.setChecked(True)
        self.btn_conf.setFlat(True)
        self.btn_conf.setObjectName(_fromUtf8("btn_conf"))
        self.verticalLayout_2.addWidget(self.btn_conf)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 10)
        self.verticalLayout_2.setStretch(3, 10)
        self.verticalLayout_2.setStretch(4, 10)
        self.horizontalLayout_7.addWidget(self.Opciones)
        self.todo = QtGui.QStackedWidget(self.centralwidget)
        self.todo.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.todo.sizePolicy().hasHeightForWidth())
        self.todo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        self.todo.setFont(font)
        self.todo.setWhatsThis(_fromUtf8(""))
        self.todo.setStyleSheet(_fromUtf8("background-color: rgb(138, 138, 138);"))
        self.todo.setFrameShape(QtGui.QFrame.Box)
        self.todo.setLineWidth(1)
        self.todo.setMidLineWidth(0)
        self.todo.setObjectName(_fromUtf8("todo"))
        self.ayud = QtGui.QWidget()
        self.ayud.setWhatsThis(_fromUtf8(""))
        self.ayud.setStyleSheet(_fromUtf8("background-color: rgb(50, 50, 50);"))
        self.ayud.setObjectName(_fromUtf8("ayud"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.ayud)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.webView = QtWebKit.QWebView(self.ayud)
        self.webView.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_4.addWidget(self.webView)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.setStretch(0, 1)
        self.todo.addWidget(self.ayud)
        self.inic = QtGui.QWidget()
        self.inic.setWhatsThis(_fromUtf8(""))
        self.inic.setObjectName(_fromUtf8("inic"))
        self.gridLayout = QtGui.QGridLayout(self.inic)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_2 = QtGui.QSplitter(self.inic)
        self.splitter_2.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(16, 16, 16);"))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.DatosGrafica = QtGui.QWidget(self.splitter_2)
        self.DatosGrafica.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 0);"))
        self.DatosGrafica.setObjectName(_fromUtf8("DatosGrafica"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.DatosGrafica)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(self.DatosGrafica)
        self.splitter.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(16, 16, 16);"))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.gridBtns = QtGui.QFrame(self.splitter)
        self.gridBtns.setStyleSheet(_fromUtf8("background-color: rgb(50, 50, 50);"))
        self.gridBtns.setObjectName(_fromUtf8("gridBtns"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridBtns)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.Box3 = QtGui.QVBoxLayout()
        self.Box3.setSpacing(0)
        self.Box3.setObjectName(_fromUtf8("Box3"))
        self.B3_lbl = QtGui.QLabel(self.gridBtns)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.B3_lbl.setFont(font)
        self.B3_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.B3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.B3_lbl.setObjectName(_fromUtf8("B3_lbl"))
        self.Box3.addWidget(self.B3_lbl)
        self.B3_btn = QtGui.QPushButton(self.gridBtns)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B3_btn.sizePolicy().hasHeightForWidth())
        self.B3_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.B3_btn.setFont(font)
        self.B3_btn.setStyleSheet(_fromUtf8("color: rgb(5, 113, 255);"))
        self.B3_btn.setFlat(True)
        self.B3_btn.setObjectName(_fromUtf8("B3_btn"))
        self.Box3.addWidget(self.B3_btn)
        self.Box3.setStretch(0, 1)
        self.Box3.setStretch(1, 4)
        self.gridLayout_5.addLayout(self.Box3, 1, 0, 1, 1)
        self.Box6 = QtGui.QVBoxLayout()
        self.Box6.setSpacing(0)
        self.Box6.setObjectName(_fromUtf8("Box6"))
        self.B6_lbl = QtGui.QLabel(self.gridBtns)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.B6_lbl.setFont(font)
        self.B6_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.B6_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.B6_lbl.setObjectName(_fromUtf8("B6_lbl"))
        self.Box6.addWidget(self.B6_lbl)
        self.B6_btn = QtGui.QPushButton(self.gridBtns)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B6_btn.sizePolicy().hasHeightForWidth())
        self.B6_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.B6_btn.setFont(font)
        self.B6_btn.setStyleSheet(_fromUtf8("color: rgb(5, 113, 255);"))
        self.B6_btn.setFlat(True)
        self.B6_btn.setObjectName(_fromUtf8("B6_btn"))
        self.Box6.addWidget(self.B6_btn)
        self.Box6.setStretch(0, 1)
        self.Box6.setStretch(1, 4)
        self.gridLayout_5.addLayout(self.Box6, 2, 1, 1, 1)
        self.Box4 = QtGui.QVBoxLayout()
        self.Box4.setSpacing(0)
        self.Box4.setObjectName(_fromUtf8("Box4"))
        self.B4_lbl = QtGui.QLabel(self.gridBtns)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.B4_lbl.setFont(font)
        self.B4_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.B4_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.B4_lbl.setObjectName(_fromUtf8("B4_lbl"))
        self.Box4.addWidget(self.B4_lbl)
        self.B4_btn = QtGui.QPushButton(self.gridBtns)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B4_btn.sizePolicy().hasHeightForWidth())
        self.B4_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.B4_btn.setFont(font)
        self.B4_btn.setStyleSheet(_fromUtf8("color: rgb(5, 113, 255);"))
        self.B4_btn.setFlat(True)
        self.B4_btn.setObjectName(_fromUtf8("B4_btn"))
        self.Box4.addWidget(self.B4_btn)
        self.Box4.setStretch(0, 1)
        self.Box4.setStretch(1, 4)
        self.gridLayout_5.addLayout(self.Box4, 1, 1, 1, 1)
        self.Box5 = QtGui.QVBoxLayout()
        self.Box5.setSpacing(0)
        self.Box5.setObjectName(_fromUtf8("Box5"))
        self.B5_lbl = QtGui.QLabel(self.gridBtns)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.B5_lbl.setFont(font)
        self.B5_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.B5_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.B5_lbl.setObjectName(_fromUtf8("B5_lbl"))
        self.Box5.addWidget(self.B5_lbl)
        self.B5_btn = QtGui.QPushButton(self.gridBtns)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B5_btn.sizePolicy().hasHeightForWidth())
        self.B5_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.B5_btn.setFont(font)
        self.B5_btn.setStyleSheet(_fromUtf8("color: rgb(5, 113, 255);"))
        self.B5_btn.setFlat(True)
        self.B5_btn.setObjectName(_fromUtf8("B5_btn"))
        self.Box5.addWidget(self.B5_btn)
        self.Box5.setStretch(0, 1)
        self.Box5.setStretch(1, 4)
        self.gridLayout_5.addLayout(self.Box5, 2, 0, 1, 1)
        self.Box2 = QtGui.QVBoxLayout()
        self.Box2.setSpacing(0)
        self.Box2.setObjectName(_fromUtf8("Box2"))
        self.B2_lbl = QtGui.QLabel(self.gridBtns)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.B2_lbl.setFont(font)
        self.B2_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.B2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.B2_lbl.setObjectName(_fromUtf8("B2_lbl"))
        self.Box2.addWidget(self.B2_lbl)
        self.B2_btn = QtGui.QPushButton(self.gridBtns)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B2_btn.sizePolicy().hasHeightForWidth())
        self.B2_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.B2_btn.setFont(font)
        self.B2_btn.setStyleSheet(_fromUtf8("color: rgb(5, 113, 255);"))
        self.B2_btn.setFlat(True)
        self.B2_btn.setObjectName(_fromUtf8("B2_btn"))
        self.Box2.addWidget(self.B2_btn)
        self.Box2.setStretch(0, 1)
        self.Box2.setStretch(1, 4)
        self.gridLayout_5.addLayout(self.Box2, 0, 1, 1, 1)
        self.Box1 = QtGui.QVBoxLayout()
        self.Box1.setSpacing(0)
        self.Box1.setObjectName(_fromUtf8("Box1"))
        self.B1_lbl = QtGui.QLabel(self.gridBtns)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.B1_lbl.setFont(font)
        self.B1_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.B1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.B1_lbl.setObjectName(_fromUtf8("B1_lbl"))
        self.Box1.addWidget(self.B1_lbl)
        self.B1_btn = QtGui.QPushButton(self.gridBtns)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B1_btn.sizePolicy().hasHeightForWidth())
        self.B1_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.B1_btn.setFont(font)
        self.B1_btn.setStyleSheet(_fromUtf8("color: rgb(5, 113, 255);"))
        self.B1_btn.setFlat(True)
        self.B1_btn.setObjectName(_fromUtf8("B1_btn"))
        self.Box1.addWidget(self.B1_btn)
        self.Box1.setStretch(0, 1)
        self.Box1.setStretch(1, 4)
        self.gridLayout_5.addLayout(self.Box1, 0, 0, 1, 1)
        self.Box7 = QtGui.QVBoxLayout()
        self.Box7.setSpacing(0)
        self.Box7.setObjectName(_fromUtf8("Box7"))
        self.B7_lbl = QtGui.QLabel(self.gridBtns)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.B7_lbl.setFont(font)
        self.B7_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.B7_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.B7_lbl.setObjectName(_fromUtf8("B7_lbl"))
        self.Box7.addWidget(self.B7_lbl)
        self.B7_btn = QtGui.QPushButton(self.gridBtns)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B7_btn.sizePolicy().hasHeightForWidth())
        self.B7_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.B7_btn.setFont(font)
        self.B7_btn.setStyleSheet(_fromUtf8("color: rgb(5, 113, 255);"))
        self.B7_btn.setFlat(True)
        self.B7_btn.setObjectName(_fromUtf8("B7_btn"))
        self.Box7.addWidget(self.B7_btn)
        self.Box7.setStretch(0, 1)
        self.Box7.setStretch(1, 4)
        self.gridLayout_5.addLayout(self.Box7, 3, 0, 1, 1)
        self.Box8 = QtGui.QVBoxLayout()
        self.Box8.setSpacing(0)
        self.Box8.setObjectName(_fromUtf8("Box8"))
        self.B8_lbl = QtGui.QLabel(self.gridBtns)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.B8_lbl.setFont(font)
        self.B8_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.B8_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.B8_lbl.setObjectName(_fromUtf8("B8_lbl"))
        self.Box8.addWidget(self.B8_lbl)
        self.B8_btn = QtGui.QPushButton(self.gridBtns)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B8_btn.sizePolicy().hasHeightForWidth())
        self.B8_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.B8_btn.setFont(font)
        self.B8_btn.setStyleSheet(_fromUtf8("color: rgb(5, 113, 255);"))
        self.B8_btn.setFlat(True)
        self.B8_btn.setObjectName(_fromUtf8("B8_btn"))
        self.Box8.addWidget(self.B8_btn)
        self.Box8.setStretch(0, 1)
        self.Box8.setStretch(1, 4)
        self.gridLayout_5.addLayout(self.Box8, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.splitter)
        self.ini_Tabs = QtGui.QTabWidget(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        self.ini_Tabs.setFont(font)
        self.ini_Tabs.setStyleSheet(_fromUtf8("QTabWidget::pane{\n"
"\n"
"    border-top: 40px solid rgb(0, 0, 0);\n"
"    position: absolute;\n"
"    top: -40px;\n"
"    background: rgba( 0, 0, 0, 0% ); /* For transparent background */\n"
"    min-width: 5ex;\n"
"}\n"
"\n"
"QTabWidget {\n"
"    \n"
"    border-color: white;\n"
"    border:  40px;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"\n"
"    background: rgb(0,0,0);\n"
"    min-width: 12ex;\n"
"    padding: 5px 50px ; \n"
"    font: 14pt \"Agency FB\";\n"
"    color: rgb(255, 255,255);\n"
"\n"
"}\n"
"\n"
"QTabBar{\n"
"    \n"
"    background-color:rgb(31, 96, 244);\n"
"    min-width: 12ex;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"  \n"
"    background-color: black;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"    color: rgb(50,50,50);\n"
"font: 12pt \"Agency FB\";\n"
"}\n"
""))
        self.ini_Tabs.setObjectName(_fromUtf8("ini_Tabs"))
        self.LayoutMisiones = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LayoutMisiones.sizePolicy().hasHeightForWidth())
        self.LayoutMisiones.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        self.LayoutMisiones.setFont(font)
        self.LayoutMisiones.setObjectName(_fromUtf8("LayoutMisiones"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.LayoutMisiones)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.tablaMisiones = QtGui.QTableWidget(self.LayoutMisiones)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.tablaMisiones.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.tablaMisiones.setFont(font)
        self.tablaMisiones.setStyleSheet(_fromUtf8("QTableView {    \n"
"   selection-background-color: rgb(41, 116, 255);    \n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: white;\n"
"    gridline-color: rgb(100, 100, 100);    \n"
"}\n"
"\n"
"\n"
"QTableView QHeaderView::Selected {    \n"
"    color: green;    \n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"    \n"
"}\n"
"\n"
"QHeaderView::section:selected , QTableCornerButton::section {\n"
"    /*Recuadro en la parte superior izquierda*/\n"
"    background-color:black;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"        width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""))
        self.tablaMisiones.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaMisiones.setFrameShadow(QtGui.QFrame.Raised)
        self.tablaMisiones.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablaMisiones.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablaMisiones.setProperty("showDropIndicator", False)
        self.tablaMisiones.setDragDropOverwriteMode(False)
        self.tablaMisiones.setAlternatingRowColors(True)
        self.tablaMisiones.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.tablaMisiones.setGridStyle(QtCore.Qt.DashLine)
        self.tablaMisiones.setCornerButtonEnabled(False)
        self.tablaMisiones.setRowCount(8)
        self.tablaMisiones.setColumnCount(7)
        self.tablaMisiones.setObjectName(_fromUtf8("tablaMisiones"))
        item = QtGui.QTableWidgetItem()
        self.tablaMisiones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaMisiones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaMisiones.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaMisiones.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaMisiones.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaMisiones.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tablaMisiones.setHorizontalHeaderItem(6, item)
        self.tablaMisiones.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_9.addWidget(self.tablaMisiones)
        self.verticalBotones = QtGui.QWidget(self.LayoutMisiones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalBotones.sizePolicy().hasHeightForWidth())
        self.verticalBotones.setSizePolicy(sizePolicy)
        self.verticalBotones.setStyleSheet(_fromUtf8("background-color: rgb(50, 50, 50);"))
        self.verticalBotones.setObjectName(_fromUtf8("verticalBotones"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.verticalBotones)
        self.verticalLayout_15.setMargin(0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.btn_descargar_mis = QtGui.QPushButton(self.verticalBotones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_descargar_mis.sizePolicy().hasHeightForWidth())
        self.btn_descargar_mis.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.btn_descargar_mis.setFont(font)
        self.btn_descargar_mis.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"    background-color: rgb(50,50,50) ;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"/*\n"
"QPushButton:hover {\n"
"    background-color: rgb(41, 116, 255);\n"
"\n"
"}*/\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 96, 245);\n"
"}\n"
"\n"
""))
        self.btn_descargar_mis.setFlat(True)
        self.btn_descargar_mis.setObjectName(_fromUtf8("btn_descargar_mis"))
        self.verticalLayout_15.addWidget(self.btn_descargar_mis)
        self.btn_agregar_mis = QtGui.QPushButton(self.verticalBotones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_agregar_mis.sizePolicy().hasHeightForWidth())
        self.btn_agregar_mis.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.btn_agregar_mis.setFont(font)
        self.btn_agregar_mis.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"    background-color: rgb(50,50,50) ;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"/*\n"
"QPushButton:hover {\n"
"    background-color: rgb(41, 116, 255);\n"
"\n"
"}*/\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 96, 245);\n"
"}\n"
"\n"
""))
        self.btn_agregar_mis.setFlat(True)
        self.btn_agregar_mis.setObjectName(_fromUtf8("btn_agregar_mis"))
        self.verticalLayout_15.addWidget(self.btn_agregar_mis)
        self.btn_enviar_mis = QtGui.QPushButton(self.verticalBotones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_enviar_mis.sizePolicy().hasHeightForWidth())
        self.btn_enviar_mis.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.btn_enviar_mis.setFont(font)
        self.btn_enviar_mis.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"    background-color: rgb(50,50,50) ;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"/*\n"
"QPushButton:hover {\n"
"    background-color: rgb(41, 116, 255);\n"
"\n"
"}*/\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 96, 245);\n"
"}\n"
"\n"
""))
        self.btn_enviar_mis.setFlat(True)
        self.btn_enviar_mis.setObjectName(_fromUtf8("btn_enviar_mis"))
        self.verticalLayout_15.addWidget(self.btn_enviar_mis)
        self.btn_empezar = QtGui.QPushButton(self.verticalBotones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_empezar.sizePolicy().hasHeightForWidth())
        self.btn_empezar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.btn_empezar.setFont(font)
        self.btn_empezar.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"    background-color: rgb(50,50,50) ;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"/*\n"
"QPushButton:hover {\n"
"    background-color: rgb(41, 116, 255);\n"
"\n"
"}*/\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 96, 245);\n"
"}\n"
"\n"
""))
        self.btn_empezar.setFlat(True)
        self.btn_empezar.setObjectName(_fromUtf8("btn_empezar"))
        self.verticalLayout_15.addWidget(self.btn_empezar)
        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 1)
        self.verticalLayout_15.setStretch(2, 1)
        self.verticalLayout_15.setStretch(3, 1)
        self.horizontalLayout_9.addWidget(self.verticalBotones)
        self.horizontalLayout_9.setStretch(0, 5)
        self.horizontalLayout_9.setStretch(1, 1)
        self.ini_Tabs.addTab(self.LayoutMisiones, _fromUtf8(""))
        self.graficos = QtGui.QWidget()
        self.graficos.setObjectName(_fromUtf8("graficos"))
        self.horizontalLayout_30 = QtGui.QHBoxLayout(self.graficos)
        self.horizontalLayout_30.setMargin(0)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.layoutGraph = QtGui.QHBoxLayout()
        self.layoutGraph.setObjectName(_fromUtf8("layoutGraph"))
        self.listAtributos = QtGui.QTableWidget(self.graficos)
        self.listAtributos.setStyleSheet(_fromUtf8("\n"
"QTableView {\n"
"    \n"
"    selection-background-color: rgb(41, 116, 255);\n"
"\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"    \n"
"}\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"    \n"
"}\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"        background: rgb(0,0,0);\n"
"        min-height: 10px;\n"
"}\n"
"QScrollBar::vertical {\n"
"        background: rgb(255,255,255);\n"
"        min-height: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"        background: rgb(0,0,0);\n"
"        min-height: 10px;\n"
"}\n"
"QScrollBar::horizontal {\n"
"        background: rgb(255,255,255);\n"
"        min-height: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.listAtributos.setAlternatingRowColors(True)
        self.listAtributos.setRowCount(5)
        self.listAtributos.setColumnCount(2)
        self.listAtributos.setObjectName(_fromUtf8("listAtributos"))
        item = QtGui.QTableWidgetItem()
        self.listAtributos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.listAtributos.setHorizontalHeaderItem(1, item)
        self.listAtributos.horizontalHeader().setStretchLastSection(True)
        self.layoutGraph.addWidget(self.listAtributos)
        self.horizontalLayout_30.addLayout(self.layoutGraph)
        self.ini_Tabs.addTab(self.graficos, _fromUtf8(""))
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.todo.addWidget(self.inic)
        self.cone = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cone.sizePolicy().hasHeightForWidth())
        self.cone.setSizePolicy(sizePolicy)
        self.cone.setWhatsThis(_fromUtf8(""))
        self.cone.setStyleSheet(_fromUtf8("background-color: rgb(50,50, 50);\n"
"color: rgb(255, 255, 255);"))
        self.cone.setObjectName(_fromUtf8("cone"))
        self.gridLayout_3 = QtGui.QGridLayout(self.cone)
        self.gridLayout_3.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gb_logVehiculo = QtGui.QGroupBox(self.cone)
        self.gb_logVehiculo.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_logVehiculo.sizePolicy().hasHeightForWidth())
        self.gb_logVehiculo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        self.gb_logVehiculo.setFont(font)
        self.gb_logVehiculo.setWhatsThis(_fromUtf8(""))
        self.gb_logVehiculo.setStyleSheet(_fromUtf8("background-color: rgb(50, 50, 50);"))
        self.gb_logVehiculo.setFlat(True)
        self.gb_logVehiculo.setObjectName(_fromUtf8("gb_logVehiculo"))
        self.verticalLayout = QtGui.QVBoxLayout(self.gb_logVehiculo)
        self.verticalLayout.setMargin(20)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.logVehiculo = QtGui.QPlainTextEdit(self.gb_logVehiculo)
        self.logVehiculo.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(13)
        font.setKerning(False)
        self.logVehiculo.setFont(font)
        self.logVehiculo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.logVehiculo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.logVehiculo.setAcceptDrops(False)
        self.logVehiculo.setWhatsThis(_fromUtf8(""))
        self.logVehiculo.setAutoFillBackground(False)
        self.logVehiculo.setStyleSheet(_fromUtf8("QPlainTextEdit{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"        background: rgb(10,10,10);\n"
"        min-height: 10px;\n"
"}\n"
"QScrollBar::vertical {\n"
"        background: rgb(255,255,255);\n"
"        min-height: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"        background: rgb(0,0,0);\n"
"        min-height: 10px;\n"
"}\n"
"QScrollBar::horizontal {\n"
"        background: rgb(255,255,255);\n"
"        min-height: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.logVehiculo.setFrameShape(QtGui.QFrame.HLine)
        self.logVehiculo.setFrameShadow(QtGui.QFrame.Sunken)
        self.logVehiculo.setMidLineWidth(0)
        self.logVehiculo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.logVehiculo.setTabChangesFocus(True)
        self.logVehiculo.setUndoRedoEnabled(False)
        self.logVehiculo.setReadOnly(True)
        self.logVehiculo.setPlainText(_fromUtf8("BEcopter > Ingrese el IP de la maquina cliente. Esta debe ser la misma que se ingreso en el archivo /etc/default/arducopter perteneciente al vehiculo."))
        self.logVehiculo.setTabStopWidth(81)
        self.logVehiculo.setBackgroundVisible(False)
        self.logVehiculo.setCenterOnScroll(True)
        self.logVehiculo.setObjectName(_fromUtf8("logVehiculo"))
        self.verticalLayout.addWidget(self.logVehiculo)
        self.pushButton = QtGui.QPushButton(self.gb_logVehiculo)
        self.pushButton.setWhatsThis(_fromUtf8(""))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"    background-color: rgb(41, 116, 255);\n"
"\n"
"}\n"
"QPushButton {\n"
"text-align: center center;\n"
"border: 0px;\n"
"padding: 5px 1em;\n"
"}\n"
""))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.setStretch(0, 4)
        self.gridLayout_3.addWidget(self.gb_logVehiculo, 1, 0, 1, 1)
        self.gb_infoVehiculo = QtGui.QGroupBox(self.cone)
        self.gb_infoVehiculo.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_infoVehiculo.sizePolicy().hasHeightForWidth())
        self.gb_infoVehiculo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        self.gb_infoVehiculo.setFont(font)
        self.gb_infoVehiculo.setWhatsThis(_fromUtf8(""))
        self.gb_infoVehiculo.setStyleSheet(_fromUtf8("border-color: rgb(0, 255, 0);\n"
"border-top-color: rgb(0, 255, 0);\n"
"alternate-background-color: rgb(255, 85, 255);\n"
"gridline-color: rgb(255, 85, 0);\n"
"background-color: rgb(50, 50, 50);"))
        self.gb_infoVehiculo.setFlat(True)
        self.gb_infoVehiculo.setObjectName(_fromUtf8("gb_infoVehiculo"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.gb_infoVehiculo)
        self.verticalLayout_6.setContentsMargins(15, 20, 20, 20)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_2 = QtGui.QGroupBox(self.gb_infoVehiculo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_25 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_5.addWidget(self.label_9)
        self.lbl_type = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_type.sizePolicy().hasHeightForWidth())
        self.lbl_type.setSizePolicy(sizePolicy)
        self.lbl_type.setStyleSheet(_fromUtf8("margin: 15px 50px;"))
        self.lbl_type.setText(_fromUtf8(""))
        self.lbl_type.setScaledContents(True)
        self.lbl_type.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_type.setObjectName(_fromUtf8("lbl_type"))
        self.verticalLayout_5.addWidget(self.lbl_type)
        self.horizontalLayout_25.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_7.addWidget(self.label_10)
        self.lbl_firm = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_firm.sizePolicy().hasHeightForWidth())
        self.lbl_firm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(20)
        self.lbl_firm.setFont(font)
        self.lbl_firm.setText(_fromUtf8(""))
        self.lbl_firm.setScaledContents(True)
        self.lbl_firm.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_firm.setObjectName(_fromUtf8("lbl_firm"))
        self.verticalLayout_7.addWidget(self.lbl_firm)
        self.horizontalLayout_25.addLayout(self.verticalLayout_7)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.gb_infoVehiculo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_12.addWidget(self.label_19)
        self.lbl_gps = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_gps.sizePolicy().hasHeightForWidth())
        self.lbl_gps.setSizePolicy(sizePolicy)
        self.lbl_gps.setText(_fromUtf8(""))
        self.lbl_gps.setPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/img/conexion/GPSicon/worldwide.png")))
        self.lbl_gps.setScaledContents(True)
        self.lbl_gps.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_gps.setObjectName(_fromUtf8("lbl_gps"))
        self.verticalLayout_12.addWidget(self.lbl_gps)
        self.horizontalLayout_26.addLayout(self.verticalLayout_12)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_20 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_14.addWidget(self.label_20)
        self.lbl_bat = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_bat.sizePolicy().hasHeightForWidth())
        self.lbl_bat.setSizePolicy(sizePolicy)
        self.lbl_bat.setText(_fromUtf8(""))
        self.lbl_bat.setPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/img/conexion/Batteryicon/battery.png")))
        self.lbl_bat.setScaledContents(True)
        self.lbl_bat.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_bat.setObjectName(_fromUtf8("lbl_bat"))
        self.verticalLayout_14.addWidget(self.lbl_bat)
        self.horizontalLayout_26.addLayout(self.verticalLayout_14)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_16.addWidget(self.label_14)
        self.lbl_com = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_com.sizePolicy().hasHeightForWidth())
        self.lbl_com.setSizePolicy(sizePolicy)
        self.lbl_com.setText(_fromUtf8(""))
        self.lbl_com.setPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/img/conexion/Signalicon/antenna.png")))
        self.lbl_com.setScaledContents(True)
        self.lbl_com.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_com.setObjectName(_fromUtf8("lbl_com"))
        self.verticalLayout_16.addWidget(self.lbl_com)
        self.horizontalLayout_26.addLayout(self.verticalLayout_16)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.gb_infoVehiculo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_27 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.label_17 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_17.addWidget(self.label_17)
        self.lbl_sta = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_sta.sizePolicy().hasHeightForWidth())
        self.lbl_sta.setSizePolicy(sizePolicy)
        self.lbl_sta.setText(_fromUtf8(""))
        self.lbl_sta.setPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/img/conexion/dude.png")))
        self.lbl_sta.setScaledContents(True)
        self.lbl_sta.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sta.setObjectName(_fromUtf8("lbl_sta"))
        self.verticalLayout_17.addWidget(self.lbl_sta)
        self.horizontalLayout_27.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.label_18 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_18.addWidget(self.label_18)
        self.lbl_ok = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ok.sizePolicy().hasHeightForWidth())
        self.lbl_ok.setSizePolicy(sizePolicy)
        self.lbl_ok.setText(_fromUtf8(""))
        self.lbl_ok.setPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/img/conexion/drone_nok.png")))
        self.lbl_ok.setScaledContents(True)
        self.lbl_ok.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ok.setObjectName(_fromUtf8("lbl_ok"))
        self.verticalLayout_18.addWidget(self.lbl_ok)
        self.horizontalLayout_27.addLayout(self.verticalLayout_18)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 1)
        self.gridLayout_3.addWidget(self.gb_infoVehiculo, 0, 1, 2, 1)
        self.grupoConectar = QtGui.QGroupBox(self.cone)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grupoConectar.sizePolicy().hasHeightForWidth())
        self.grupoConectar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        self.grupoConectar.setFont(font)
        self.grupoConectar.setWhatsThis(_fromUtf8(""))
        self.grupoConectar.setStyleSheet(_fromUtf8("background-color: rgb(50, 50, 50);\n"
"\n"
"border-color: rgb(255, 0, 0);\n"
"border-top-color: rgb(255, 0, 0);\n"
"border-right-color: rgb(255, 0, 0);\n"
"border-bottom-color: rgb(255, 0, 0);\n"
"border-left-color: rgb(255, 0, 0);\n"
"border-left-color: rgb(255, 0, 0);\n"
"alternate-background-color: rgb(255, 0, 0);\n"
"gridline-color: rgb(255, 0, 0);\n"
"selection-background-color: rgb(255, 0, 0);"))
        self.grupoConectar.setFlat(True)
        self.grupoConectar.setCheckable(False)
        self.grupoConectar.setObjectName(_fromUtf8("grupoConectar"))
        self.gridLayout_4 = QtGui.QGridLayout(self.grupoConectar)
        self.gridLayout_4.setContentsMargins(2, 2, 2, -1)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.inIP = QtGui.QLineEdit(self.grupoConectar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(18)
        self.inIP.setFont(font)
        self.inIP.setWhatsThis(_fromUtf8(""))
        self.inIP.setStyleSheet(_fromUtf8("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"color:  rgb(0, 0, 0);\n"
"}\n"
"QLineEdit::editable {\n"
"background-color: rgb(255, 255, 255);\n"
"color:  rgb(0, 0, 0);\n"
"}"))
        self.inIP.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inIP.setText(_fromUtf8("192.168.1.13"))
        self.inIP.setObjectName(_fromUtf8("inIP"))
        self.gridLayout_4.addWidget(self.inIP, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.grupoConectar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setWhatsThis(_fromUtf8(""))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.grupoConectar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setWhatsThis(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.inPort = QtGui.QLineEdit(self.grupoConectar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(13)
        self.inPort.setFont(font)
        self.inPort.setWhatsThis(_fromUtf8(""))
        self.inPort.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color:  rgb(0, 0, 0);"))
        self.inPort.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inPort.setObjectName(_fromUtf8("inPort"))
        self.gridLayout_4.addWidget(self.inPort, 1, 1, 1, 1)
        self.btn_conectar = QtGui.QPushButton(self.grupoConectar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_conectar.sizePolicy().hasHeightForWidth())
        self.btn_conectar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.btn_conectar.setFont(font)
        self.btn_conectar.setWhatsThis(_fromUtf8(""))
        self.btn_conectar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_conectar.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"    background-color: rgb(41, 116, 255);\n"
"\n"
"}\n"
"QPushButton {\n"
"text-align: center center;\n"
"border: 0px;\n"
"padding: 1px 1em;\n"
"}\n"
""))
        self.btn_conectar.setFlat(True)
        self.btn_conectar.setObjectName(_fromUtf8("btn_conectar"))
        self.gridLayout_4.addWidget(self.btn_conectar, 0, 2, 2, 1)
        self.gridLayout_4.setColumnMinimumWidth(0, 6)
        self.gridLayout_4.setColumnMinimumWidth(1, 1)
        self.gridLayout_4.setColumnMinimumWidth(2, 6)
        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 3)
        self.gridLayout_4.setColumnStretch(2, 2)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_3.addWidget(self.grupoConectar, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setRowStretch(0, 2)
        self.gridLayout_3.setRowStretch(1, 8)
        self.grupoConectar.raise_()
        self.gb_logVehiculo.raise_()
        self.gb_infoVehiculo.raise_()
        self.todo.addWidget(self.cone)
        self.coma = QtGui.QWidget()
        self.coma.setWhatsThis(_fromUtf8(""))
        self.coma.setStyleSheet(_fromUtf8("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 13pt \"Agency FB\";\n"
""))
        self.coma.setObjectName(_fromUtf8("coma"))
        self.gridLayout_2 = QtGui.QGridLayout(self.coma)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.LayoutBtn_Ejes = QtGui.QVBoxLayout()
        self.LayoutBtn_Ejes.setContentsMargins(20, 20, 20, -1)
        self.LayoutBtn_Ejes.setObjectName(_fromUtf8("LayoutBtn_Ejes"))
        self.grupoBotones = QtGui.QGroupBox(self.coma)
        self.grupoBotones.setEnabled(True)
        self.grupoBotones.setWhatsThis(_fromUtf8(""))
        self.grupoBotones.setStyleSheet(_fromUtf8(""))
        self.grupoBotones.setFlat(True)
        self.grupoBotones.setCheckable(False)
        self.grupoBotones.setObjectName(_fromUtf8("grupoBotones"))
        self.formLayout_2 = QtGui.QFormLayout(self.grupoBotones)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setVerticalSpacing(20)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.grupoBotones)
        self.label_4.setWhatsThis(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtGui.QLabel(self.grupoBotones)
        self.label_3.setWhatsThis(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.cone_op2 = ComboBox(self.grupoBotones)
        self.cone_op2.setWhatsThis(_fromUtf8(""))
        self.cone_op2.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 1px solid #6D6D6D;\n"
"    border-radius: 1px;\n"
"    padding: 5px 18px 5px 5px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:black;\n"
"/*     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #626262, stop: 0.4 #505050,\n"
"                                 stop: 0.5 #464646, stop: 1.0 #141414);*/\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 50px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: 6D6D6D;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(img/DropDownArrow.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"    background: #0070FF\n"
"\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}"))
        self.cone_op2.setObjectName(_fromUtf8("cone_op2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.cone_op2)
        self.label_5 = QtGui.QLabel(self.grupoBotones)
        self.label_5.setWhatsThis(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.cone_op3 = ComboBox(self.grupoBotones)
        self.cone_op3.setEnabled(True)
        self.cone_op3.setWhatsThis(_fromUtf8(""))
        self.cone_op3.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 1px solid #6D6D6D;\n"
"    border-radius: 1px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:black;\n"
"/*     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #626262, stop: 0.4 #505050,\n"
"                                 stop: 0.5 #464646, stop: 1.0 #141414);*/\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 50px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: 6D6D6D;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(img/DropDownArrow.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"    background: #0070FF\n"
"\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}"))
        self.cone_op3.setObjectName(_fromUtf8("cone_op3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.cone_op3)
        self.label_6 = QtGui.QLabel(self.grupoBotones)
        self.label_6.setWhatsThis(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.cone_op4 = ComboBox(self.grupoBotones)
        self.cone_op4.setEnabled(True)
        self.cone_op4.setWhatsThis(_fromUtf8(""))
        self.cone_op4.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 1px solid #6D6D6D;\n"
"    border-radius: 1px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:black;\n"
"/*     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #626262, stop: 0.4 #505050,\n"
"                                 stop: 0.5 #464646, stop: 1.0 #141414);*/\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 50px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: 6D6D6D;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(img/DropDownArrow.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"    background: #0070FF\n"
"\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}"))
        self.cone_op4.setObjectName(_fromUtf8("cone_op4"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.cone_op4)
        self.cone_op1 = ComboBox(self.grupoBotones)
        self.cone_op1.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 1px solid #6D6D6D;\n"
"    border-radius: 1px;\n"
"    padding: 5px 18px 5px 5px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:black;\n"
"/*     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #626262, stop: 0.4 #505050,\n"
"                                 stop: 0.5 #464646, stop: 1.0 #141414);*/\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 50px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: 6D6D6D;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(img/DropDownArrow.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"    background: #0070FF\n"
"\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}"))
        self.cone_op1.setObjectName(_fromUtf8("cone_op1"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cone_op1)
        self.LayoutBtn_Ejes.addWidget(self.grupoBotones)
        self.grupoEjes = QtGui.QGroupBox(self.coma)
        self.grupoEjes.setEnabled(True)
        self.grupoEjes.setWhatsThis(_fromUtf8(""))
        self.grupoEjes.setFlat(True)
        self.grupoEjes.setObjectName(_fromUtf8("grupoEjes"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.grupoEjes)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.LayoutEj1 = QtGui.QVBoxLayout()
        self.LayoutEj1.setContentsMargins(0, -1, 0, -1)
        self.LayoutEj1.setObjectName(_fromUtf8("LayoutEj1"))
        self.opA0 = QtGui.QComboBox(self.grupoEjes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opA0.sizePolicy().hasHeightForWidth())
        self.opA0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.opA0.setFont(font)
        self.opA0.setWhatsThis(_fromUtf8(""))
        self.opA0.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 1px solid #6D6D6D;\n"
"    border-radius: 1px;\n"
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:black;\n"
"\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: 6D6D6D;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(img/DropDownArrow.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"    background: #0070FF\n"
"\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}"))
        self.opA0.setObjectName(_fromUtf8("opA0"))
        self.LayoutEj1.addWidget(self.opA0)
        self.pbAxis0 = QtGui.QProgressBar(self.grupoEjes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbAxis0.sizePolicy().hasHeightForWidth())
        self.pbAxis0.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pbAxis0.setPalette(palette)
        self.pbAxis0.setWhatsThis(_fromUtf8(""))
        self.pbAxis0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbAxis0.setAutoFillBackground(False)
        self.pbAxis0.setStyleSheet(_fromUtf8("QProgressBar {\n"
"    background-color:  rgb(20, 20, 20);\n"
"    border-color:  rgb(20, 20, 20);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(41, 116, 255);\n"
"}\n"
""))
        self.pbAxis0.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pbAxis0.setProperty("value", 50)
        self.pbAxis0.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.pbAxis0.setTextVisible(False)
        self.pbAxis0.setOrientation(QtCore.Qt.Vertical)
        self.pbAxis0.setInvertedAppearance(False)
        self.pbAxis0.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.pbAxis0.setObjectName(_fromUtf8("pbAxis0"))
        self.LayoutEj1.addWidget(self.pbAxis0)
        self.invA0 = QtGui.QCheckBox(self.grupoEjes)
        self.invA0.setWhatsThis(_fromUtf8(""))
        self.invA0.setObjectName(_fromUtf8("invA0"))
        self.LayoutEj1.addWidget(self.invA0)
        self.horizontalLayout_3.addLayout(self.LayoutEj1)
        self.LayoutEj2 = QtGui.QVBoxLayout()
        self.LayoutEj2.setObjectName(_fromUtf8("LayoutEj2"))
        self.opA1 = QtGui.QComboBox(self.grupoEjes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.opA1.setFont(font)
        self.opA1.setWhatsThis(_fromUtf8(""))
        self.opA1.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 1px solid #6D6D6D;\n"
"    border-radius: 1px;\n"
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:black;\n"
"/*     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #626262, stop: 0.4 #505050,\n"
"                                 stop: 0.5 #464646, stop: 1.0 #141414);*/\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: 6D6D6D;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(img/DropDownArrow.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"    background: #0070FF\n"
"\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}background-color: rgb(255, 255, 255);"))
        self.opA1.setObjectName(_fromUtf8("opA1"))
        self.LayoutEj2.addWidget(self.opA1)
        self.pbAxis1 = QtGui.QProgressBar(self.grupoEjes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbAxis1.sizePolicy().hasHeightForWidth())
        self.pbAxis1.setSizePolicy(sizePolicy)
        self.pbAxis1.setWhatsThis(_fromUtf8(""))
        self.pbAxis1.setStyleSheet(_fromUtf8("QProgressBar {\n"
"    background-color:  rgb(20, 20, 20);\n"
"    border-color:  rgb(20, 20, 20);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(41, 116, 255);\n"
"}\n"
""))
        self.pbAxis1.setProperty("value", 50)
        self.pbAxis1.setTextVisible(False)
        self.pbAxis1.setOrientation(QtCore.Qt.Vertical)
        self.pbAxis1.setObjectName(_fromUtf8("pbAxis1"))
        self.LayoutEj2.addWidget(self.pbAxis1)
        self.invA1 = QtGui.QCheckBox(self.grupoEjes)
        self.invA1.setWhatsThis(_fromUtf8(""))
        self.invA1.setObjectName(_fromUtf8("invA1"))
        self.LayoutEj2.addWidget(self.invA1)
        self.horizontalLayout_3.addLayout(self.LayoutEj2)
        self.LayoutEj3 = QtGui.QVBoxLayout()
        self.LayoutEj3.setObjectName(_fromUtf8("LayoutEj3"))
        self.opA2 = QtGui.QComboBox(self.grupoEjes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.opA2.setFont(font)
        self.opA2.setWhatsThis(_fromUtf8(""))
        self.opA2.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 1px solid #6D6D6D;\n"
"    border-radius: 1px;\n"
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:black;\n"
"/*     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #626262, stop: 0.4 #505050,\n"
"                                 stop: 0.5 #464646, stop: 1.0 #141414);*/\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: 6D6D6D;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(img/DropDownArrow.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"    background: #0070FF\n"
"\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}background-color: rgb(255, 255, 255);"))
        self.opA2.setObjectName(_fromUtf8("opA2"))
        self.LayoutEj3.addWidget(self.opA2)
        self.pbAxis2 = QtGui.QProgressBar(self.grupoEjes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbAxis2.sizePolicy().hasHeightForWidth())
        self.pbAxis2.setSizePolicy(sizePolicy)
        self.pbAxis2.setWhatsThis(_fromUtf8(""))
        self.pbAxis2.setStyleSheet(_fromUtf8("QProgressBar {\n"
"    background-color:  rgb(20, 20, 20);\n"
"    border-color:  rgb(20, 20, 20);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(41, 116, 255);\n"
"}\n"
""))
        self.pbAxis2.setProperty("value", 50)
        self.pbAxis2.setTextVisible(False)
        self.pbAxis2.setOrientation(QtCore.Qt.Vertical)
        self.pbAxis2.setObjectName(_fromUtf8("pbAxis2"))
        self.LayoutEj3.addWidget(self.pbAxis2)
        self.invA2 = QtGui.QCheckBox(self.grupoEjes)
        self.invA2.setWhatsThis(_fromUtf8(""))
        self.invA2.setObjectName(_fromUtf8("invA2"))
        self.LayoutEj3.addWidget(self.invA2)
        self.horizontalLayout_3.addLayout(self.LayoutEj3)
        self.LayoutEj4 = QtGui.QVBoxLayout()
        self.LayoutEj4.setObjectName(_fromUtf8("LayoutEj4"))
        self.opA3 = QtGui.QComboBox(self.grupoEjes)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.opA3.setFont(font)
        self.opA3.setWhatsThis(_fromUtf8(""))
        self.opA3.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 1px solid #6D6D6D;\n"
"    border-radius: 1px;\n"
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:black;\n"
"/*     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #626262, stop: 0.4 #505050,\n"
"                                 stop: 0.5 #464646, stop: 1.0 #141414);*/\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: 6D6D6D;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(img/DropDownArrow.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"    background: #0070FF\n"
"\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}"))
        self.opA3.setObjectName(_fromUtf8("opA3"))
        self.LayoutEj4.addWidget(self.opA3)
        self.pbAxis4 = QtGui.QProgressBar(self.grupoEjes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbAxis4.sizePolicy().hasHeightForWidth())
        self.pbAxis4.setSizePolicy(sizePolicy)
        self.pbAxis4.setWhatsThis(_fromUtf8(""))
        self.pbAxis4.setStyleSheet(_fromUtf8("QProgressBar {\n"
"    background-color:  rgb(20, 20, 20);\n"
"    border-color:  rgb(20, 20, 20);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(41, 116, 255);\n"
"}\n"
""))
        self.pbAxis4.setProperty("value", 50)
        self.pbAxis4.setTextVisible(False)
        self.pbAxis4.setOrientation(QtCore.Qt.Vertical)
        self.pbAxis4.setObjectName(_fromUtf8("pbAxis4"))
        self.LayoutEj4.addWidget(self.pbAxis4)
        self.invA3 = QtGui.QCheckBox(self.grupoEjes)
        self.invA3.setWhatsThis(_fromUtf8(""))
        self.invA3.setObjectName(_fromUtf8("invA3"))
        self.LayoutEj4.addWidget(self.invA3)
        self.horizontalLayout_3.addLayout(self.LayoutEj4)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.LayoutBtn_Ejes.addWidget(self.grupoEjes)
        self.LayoutBtn_Ejes.setStretch(0, 2)
        self.LayoutBtn_Ejes.setStretch(1, 3)
        self.gridLayout_2.addLayout(self.LayoutBtn_Ejes, 0, 2, 2, 1)
        self.Joystick_layout = QtGui.QVBoxLayout()
        self.Joystick_layout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.Joystick_layout.setContentsMargins(10, 10, -1, -1)
        self.Joystick_layout.setObjectName(_fromUtf8("Joystick_layout"))
        self.groupBox_5 = QtGui.QGroupBox(self.coma)
        self.groupBox_5.setWhatsThis(_fromUtf8(""))
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.dispConectados = ComboBox(self.groupBox_5)
        self.dispConectados.setWhatsThis(_fromUtf8(""))
        self.dispConectados.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 1px solid #6D6D6D;\n"
"    border-radius: 1px;\n"
"    padding: 5px 18px 5px 5px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:black;\n"
"/*     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #626262, stop: 0.4 #505050,\n"
"                                 stop: 0.5 #464646, stop: 1.0 #141414);*/\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 50px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: 6D6D6D;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(img/DropDownArrow.png);\n"
"    width: 4px;\n"
"    height: 4px;\n"
"    background: #0070FF\n"
"\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}"))
        self.dispConectados.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.dispConectados.setObjectName(_fromUtf8("dispConectados"))
        self.dispConectados.addItem(_fromUtf8(""))
        self.dispConectados.setItemText(0, _fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.dispConectados)
        self.Joystick_layout.addWidget(self.groupBox_5)
        self.dibujo1 = QtGui.QLabel(self.coma)
        self.dibujo1.setWhatsThis(_fromUtf8(""))
        self.dibujo1.setText(_fromUtf8(""))
        self.dibujo1.setObjectName(_fromUtf8("dibujo1"))
        self.Joystick_layout.addWidget(self.dibujo1)
        self.dibujo2 = QtGui.QLabel(self.coma)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dibujo2.sizePolicy().hasHeightForWidth())
        self.dibujo2.setSizePolicy(sizePolicy)
        self.dibujo2.setWhatsThis(_fromUtf8(""))
        self.dibujo2.setAutoFillBackground(False)
        self.dibujo2.setText(_fromUtf8(""))
        self.dibujo2.setPixmap(QtGui.QPixmap(_fromUtf8("../BEcopter/img/joystick.png")))
        self.dibujo2.setScaledContents(True)
        self.dibujo2.setObjectName(_fromUtf8("dibujo2"))
        self.Joystick_layout.addWidget(self.dibujo2)
        self.Joystick_layout.setStretch(0, 1)
        self.Joystick_layout.setStretch(2, 10)
        self.gridLayout_2.addLayout(self.Joystick_layout, 0, 0, 2, 2)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.todo.addWidget(self.coma)
        self.conf = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conf.sizePolicy().hasHeightForWidth())
        self.conf.setSizePolicy(sizePolicy)
        self.conf.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);"))
        self.conf.setObjectName(_fromUtf8("conf"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.conf)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.layoutConfiguracion = QtGui.QWidget(self.conf)
        self.layoutConfiguracion.setStyleSheet(_fromUtf8("background-color: rgb(50, 50, 50);"))
        self.layoutConfiguracion.setObjectName(_fromUtf8("layoutConfiguracion"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutConfiguracion)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabConfiguracion = QtGui.QTabWidget(self.layoutConfiguracion)
        self.tabConfiguracion.setEnabled(True)
        self.tabConfiguracion.setStyleSheet(_fromUtf8("QTabWidget::pane{\n"
"    border-top: 30px solid rgb(0, 0, 0);\n"
"    position: absolute;\n"
"    top: -30px;\n"
"    background: rgba( 0, 0, 0, 0% ); /* For transparent background */\n"
"    \n"
"}\n"
"\n"
"QTabWidget {\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"\n"
"    background: rgb(0,0,0);\n"
"    min-width: 8ex;\n"
"    padding: 12px ;\n"
"    font: 12pt \"Agency FB\";\n"
"    color: rgb(255, 255,255);\n"
"    \n"
"\n"
"}\n"
"\n"
"QTabBar{\n"
"    \n"
"    background-color:rgb(31, 96, 244);\n"
"\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"  \n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 3px; /* make non-selected tabs look smaller */\n"
"}"))
        self.tabConfiguracion.setTabPosition(QtGui.QTabWidget.North)
        self.tabConfiguracion.setObjectName(_fromUtf8("tabConfiguracion"))
        self.layoutConf_1 = QtGui.QWidget()
        self.layoutConf_1.setObjectName(_fromUtf8("layoutConf_1"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.layoutConf_1)
        self.horizontalLayout_11.setMargin(0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.tablaConf_1 = QtGui.QTableWidget(self.layoutConf_1)
        self.tablaConf_1.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""))
        self.tablaConf_1.setFrameShape(QtGui.QFrame.Panel)
        self.tablaConf_1.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed)
        self.tablaConf_1.setAlternatingRowColors(True)
        self.tablaConf_1.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tablaConf_1.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_1.setWordWrap(False)
        self.tablaConf_1.setRowCount(4)
        self.tablaConf_1.setColumnCount(6)
        self.tablaConf_1.setObjectName(_fromUtf8("tablaConf_1"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_1.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_1.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_1.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_1.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_1.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        self.tablaConf_1.setItem(1, 1, item)
        self.tablaConf_1.horizontalHeader().setStretchLastSection(True)
        self.tablaConf_1.verticalHeader().setVisible(False)
        self.horizontalLayout_11.addWidget(self.tablaConf_1)
        self.tabConfiguracion.addTab(self.layoutConf_1, _fromUtf8(""))
        self.layoutConf_2 = QtGui.QWidget()
        self.layoutConf_2.setObjectName(_fromUtf8("layoutConf_2"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.layoutConf_2)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.tablaConf_2 = QtGui.QTableWidget(self.layoutConf_2)
        self.tablaConf_2.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_2.setAlternatingRowColors(True)
        self.tablaConf_2.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_2.setRowCount(4)
        self.tablaConf_2.setColumnCount(6)
        self.tablaConf_2.setObjectName(_fromUtf8("tablaConf_2"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_2.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_2.setHorizontalHeaderItem(5, item)
        self.tablaConf_2.horizontalHeader().setStretchLastSection(True)
        self.tablaConf_2.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_13.addWidget(self.tablaConf_2)
        self.tabConfiguracion.addTab(self.layoutConf_2, _fromUtf8(""))
        self.layoutConf_3 = QtGui.QWidget()
        self.layoutConf_3.setObjectName(_fromUtf8("layoutConf_3"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.layoutConf_3)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.tablaConf_3 = QtGui.QTableWidget(self.layoutConf_3)
        self.tablaConf_3.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_3.setAlternatingRowColors(True)
        self.tablaConf_3.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_3.setRowCount(5)
        self.tablaConf_3.setColumnCount(12)
        self.tablaConf_3.setObjectName(_fromUtf8("tablaConf_3"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_3.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_3.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_3.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_3.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_3.setHorizontalHeaderItem(5, item)
        self.tablaConf_3.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_12.addWidget(self.tablaConf_3)
        self.tabConfiguracion.addTab(self.layoutConf_3, _fromUtf8(""))
        self.layoutConf_4 = QtGui.QWidget()
        self.layoutConf_4.setObjectName(_fromUtf8("layoutConf_4"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.layoutConf_4)
        self.horizontalLayout_14.setMargin(0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.tablaConf_4 = QtGui.QTableWidget(self.layoutConf_4)
        self.tablaConf_4.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_4.setAlternatingRowColors(True)
        self.tablaConf_4.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_4.setRowCount(5)
        self.tablaConf_4.setColumnCount(12)
        self.tablaConf_4.setObjectName(_fromUtf8("tablaConf_4"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_4.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_4.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_4.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_4.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_4.setHorizontalHeaderItem(5, item)
        self.tablaConf_4.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_14.addWidget(self.tablaConf_4)
        self.tabConfiguracion.addTab(self.layoutConf_4, _fromUtf8(""))
        self.layoutConf_5 = QtGui.QWidget()
        self.layoutConf_5.setObjectName(_fromUtf8("layoutConf_5"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.layoutConf_5)
        self.horizontalLayout_15.setMargin(0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.tablaConf_5 = QtGui.QTableWidget(self.layoutConf_5)
        self.tablaConf_5.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_5.setAlternatingRowColors(True)
        self.tablaConf_5.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_5.setRowCount(5)
        self.tablaConf_5.setColumnCount(12)
        self.tablaConf_5.setObjectName(_fromUtf8("tablaConf_5"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_5.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_5.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_5.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_5.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_5.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_5.setHorizontalHeaderItem(5, item)
        self.tablaConf_5.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_15.addWidget(self.tablaConf_5)
        self.tabConfiguracion.addTab(self.layoutConf_5, _fromUtf8(""))
        self.layoutConf_6 = QtGui.QWidget()
        self.layoutConf_6.setObjectName(_fromUtf8("layoutConf_6"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.layoutConf_6)
        self.horizontalLayout_16.setMargin(0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.tablaConf_6 = QtGui.QTableWidget(self.layoutConf_6)
        self.tablaConf_6.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_6.setAlternatingRowColors(True)
        self.tablaConf_6.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_6.setRowCount(5)
        self.tablaConf_6.setColumnCount(12)
        self.tablaConf_6.setObjectName(_fromUtf8("tablaConf_6"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_6.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_6.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_6.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_6.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_6.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_6.setHorizontalHeaderItem(5, item)
        self.tablaConf_6.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_16.addWidget(self.tablaConf_6)
        self.tabConfiguracion.addTab(self.layoutConf_6, _fromUtf8(""))
        self.layoutConf_7 = QtGui.QWidget()
        self.layoutConf_7.setObjectName(_fromUtf8("layoutConf_7"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.layoutConf_7)
        self.horizontalLayout_17.setMargin(0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.tablaConf_7 = QtGui.QTableWidget(self.layoutConf_7)
        self.tablaConf_7.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_7.setAlternatingRowColors(True)
        self.tablaConf_7.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_7.setRowCount(5)
        self.tablaConf_7.setColumnCount(12)
        self.tablaConf_7.setObjectName(_fromUtf8("tablaConf_7"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_7.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_7.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_7.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_7.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_7.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_7.setHorizontalHeaderItem(5, item)
        self.tablaConf_7.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_17.addWidget(self.tablaConf_7)
        self.tabConfiguracion.addTab(self.layoutConf_7, _fromUtf8(""))
        self.layoutConf_8 = QtGui.QWidget()
        self.layoutConf_8.setObjectName(_fromUtf8("layoutConf_8"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.layoutConf_8)
        self.horizontalLayout_18.setMargin(0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.tablaConf_8 = QtGui.QTableWidget(self.layoutConf_8)
        self.tablaConf_8.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_8.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_8.setAlternatingRowColors(True)
        self.tablaConf_8.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_8.setRowCount(5)
        self.tablaConf_8.setColumnCount(12)
        self.tablaConf_8.setObjectName(_fromUtf8("tablaConf_8"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_8.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_8.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_8.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_8.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_8.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_8.setHorizontalHeaderItem(5, item)
        self.tablaConf_8.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_18.addWidget(self.tablaConf_8)
        self.tabConfiguracion.addTab(self.layoutConf_8, _fromUtf8(""))
        self.layoutConf_9 = QtGui.QWidget()
        self.layoutConf_9.setObjectName(_fromUtf8("layoutConf_9"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.layoutConf_9)
        self.horizontalLayout_19.setMargin(0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.tablaConf_9 = QtGui.QTableWidget(self.layoutConf_9)
        self.tablaConf_9.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_9.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_9.setAlternatingRowColors(True)
        self.tablaConf_9.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_9.setRowCount(5)
        self.tablaConf_9.setColumnCount(11)
        self.tablaConf_9.setObjectName(_fromUtf8("tablaConf_9"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_9.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_9.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_9.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_9.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_9.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_9.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_9.setItem(0, 6, item)
        self.tablaConf_9.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_19.addWidget(self.tablaConf_9)
        self.tabConfiguracion.addTab(self.layoutConf_9, _fromUtf8(""))
        self.layoutConf_10 = QtGui.QWidget()
        self.layoutConf_10.setObjectName(_fromUtf8("layoutConf_10"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout(self.layoutConf_10)
        self.horizontalLayout_20.setMargin(0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.tablaConf_10 = QtGui.QTableWidget(self.layoutConf_10)
        self.tablaConf_10.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_10.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_10.setAlternatingRowColors(True)
        self.tablaConf_10.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_10.setRowCount(50)
        self.tablaConf_10.setColumnCount(11)
        self.tablaConf_10.setObjectName(_fromUtf8("tablaConf_10"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_10.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_10.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_10.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_10.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_10.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_10.setHorizontalHeaderItem(5, item)
        self.tablaConf_10.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_20.addWidget(self.tablaConf_10)
        self.tabConfiguracion.addTab(self.layoutConf_10, _fromUtf8(""))
        self.layoutConf_11 = QtGui.QWidget()
        self.layoutConf_11.setObjectName(_fromUtf8("layoutConf_11"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.layoutConf_11)
        self.horizontalLayout_21.setMargin(0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.tablaConf_11 = QtGui.QTableWidget(self.layoutConf_11)
        self.tablaConf_11.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_11.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_11.setAlternatingRowColors(True)
        self.tablaConf_11.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_11.setRowCount(5)
        self.tablaConf_11.setColumnCount(11)
        self.tablaConf_11.setObjectName(_fromUtf8("tablaConf_11"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_11.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_11.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_11.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_11.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_11.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_11.setHorizontalHeaderItem(5, item)
        self.tablaConf_11.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_21.addWidget(self.tablaConf_11)
        self.tabConfiguracion.addTab(self.layoutConf_11, _fromUtf8(""))
        self.layoutConf_12 = QtGui.QWidget()
        self.layoutConf_12.setObjectName(_fromUtf8("layoutConf_12"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout(self.layoutConf_12)
        self.horizontalLayout_22.setMargin(0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.tablaConf_12 = QtGui.QTableWidget(self.layoutConf_12)
        self.tablaConf_12.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QScrollBar:vertical {           \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"       width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"\n"
""))
        self.tablaConf_12.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_12.setAlternatingRowColors(True)
        self.tablaConf_12.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_12.setRowCount(5)
        self.tablaConf_12.setColumnCount(11)
        self.tablaConf_12.setObjectName(_fromUtf8("tablaConf_12"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_12.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_12.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_12.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_12.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_12.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_12.setHorizontalHeaderItem(5, item)
        self.tablaConf_12.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_22.addWidget(self.tablaConf_12)
        self.tabConfiguracion.addTab(self.layoutConf_12, _fromUtf8(""))
        self.layoutConf_13 = QtGui.QWidget()
        self.layoutConf_13.setObjectName(_fromUtf8("layoutConf_13"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.layoutConf_13)
        self.horizontalLayout_23.setMargin(0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.tablaConf_13 = QtGui.QTableWidget(self.layoutConf_13)
        self.tablaConf_13.setStyleSheet(_fromUtf8("QTableView {\n"
"    selection-background-color: rgb(41, 116, 255);\n"
"    alternate-background-color: rgb(70,70,70);\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QTableView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView::section, QTableCornerButton::section {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"QHeaderView:selected{\n"
"    background-color:rgb(0, 0, 0)\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"            border: 1px solid black;\n"
"            background: black;\n"
"            height: 20px;\n"
"   \n"
"        }\n"
"\n"
"        QScrollBar::handle:horizontal {\n"
"            background: rgb(50,50,50);\n"
"            min-width: 26px;\n"
"        }\n"
"\n"
"        QScrollBar::add-line:horizontal {\n"
"            background: none;\n"
"            width: 26px;\n"
"            subcontrol-position: right;\n"
"            subcontrol-origin: margin;\n"
"            \n"
"        }\n"
"\n"
"        QScrollBar::sub-line:horizontal {\n"
"            background: none;\n"
"            width: 26px;\n"
"            subcontrol-position: top left;\n"
"            subcontrol-origin: margin;\n"
"            position: absolute;\n"
"        }\n"
"\n"
"        QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"            width: 26px;\n"
"            height: 26px;\n"
"            background: none;\n"
"\n"
"        }\n"
"\n"
"        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"            background: none;\n"
"        }\n"
"\n"
"        /* VERTICAL */\n"
"        QScrollBar:vertical {\n"
"            border: none;\n"
"            background: black;\n"
"            width: 26px;\n"
"            margin: 26px 0 26px 0;\n"
"        }\n"
"\n"
"        QScrollBar::handle:vertical {\n"
"            background: rgb(50,50,50);\n"
"            min-height: 26px;\n"
"        }\n"
"\n"
"        QScrollBar::add-line:vertical {\n"
"            background: none;\n"
"            height: 26px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"\n"
"        QScrollBar::sub-line:vertical {\n"
"            background: none;\n"
"            height: 26px;\n"
"            subcontrol-position: top left;\n"
"            subcontrol-origin: margin;\n"
"            position: absolute;\n"
"        }\n"
"\n"
"        QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"            width: 26px;\n"
"            height: 26px;\n"
"            background: none;\n"
"\n"
"        }\n"
"\n"
"        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"            background: none;\n"
"        }"))
        self.tablaConf_13.setFrameShape(QtGui.QFrame.NoFrame)
        self.tablaConf_13.setAlternatingRowColors(True)
        self.tablaConf_13.setGridStyle(QtCore.Qt.DashLine)
        self.tablaConf_13.setRowCount(5)
        self.tablaConf_13.setColumnCount(11)
        self.tablaConf_13.setObjectName(_fromUtf8("tablaConf_13"))
        item = QtGui.QTableWidgetItem()
        self.tablaConf_13.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_13.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_13.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_13.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_13.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablaConf_13.setHorizontalHeaderItem(5, item)
        self.tablaConf_13.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_23.addWidget(self.tablaConf_13)
        self.tabConfiguracion.addTab(self.layoutConf_13, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabConfiguracion)
        self.layoutBotones = QtGui.QWidget(self.layoutConfiguracion)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutBotones.sizePolicy().hasHeightForWidth())
        self.layoutBotones.setSizePolicy(sizePolicy)
        self.layoutBotones.setWhatsThis(_fromUtf8(""))
        self.layoutBotones.setStyleSheet(_fromUtf8("background-color: rgb(20, 20,20);"))
        self.layoutBotones.setObjectName(_fromUtf8("layoutBotones"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutBotones)
        self.horizontalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.btnRestaurarParam = QtGui.QPushButton(self.layoutBotones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRestaurarParam.sizePolicy().hasHeightForWidth())
        self.btnRestaurarParam.setSizePolicy(sizePolicy)
        self.btnRestaurarParam.setWhatsThis(_fromUtf8(""))
        self.btnRestaurarParam.setStyleSheet(_fromUtf8("background-color: rgb(50, 50, 50);"))
        self.btnRestaurarParam.setObjectName(_fromUtf8("btnRestaurarParam"))
        self.horizontalLayout_8.addWidget(self.btnRestaurarParam)
        self.btnGuardarParam = QtGui.QPushButton(self.layoutBotones)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGuardarParam.sizePolicy().hasHeightForWidth())
        self.btnGuardarParam.setSizePolicy(sizePolicy)
        self.btnGuardarParam.setWhatsThis(_fromUtf8(""))
        self.btnGuardarParam.setStyleSheet(_fromUtf8("background-color: rgb(50, 50, 50);"))
        self.btnGuardarParam.setObjectName(_fromUtf8("btnGuardarParam"))
        self.horizontalLayout_8.addWidget(self.btnGuardarParam)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.layoutBotones)
        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout_5.addWidget(self.layoutConfiguracion)
        self.todo.addWidget(self.conf)
        self.horizontalLayout_7.addWidget(self.todo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.todo.setCurrentIndex(1)
        self.ini_Tabs.setCurrentIndex(1)
        self.opA0.setCurrentIndex(-1)
        self.opA1.setCurrentIndex(-1)
        self.opA3.setCurrentIndex(-1)
        self.dispConectados.setCurrentIndex(0)
        self.tabConfiguracion.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_conf, self.btn_Cone)
        MainWindow.setTabOrder(self.btn_Cone, self.btn_Inic)
        MainWindow.setTabOrder(self.btn_Inic, self.btn_coma)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BEcopter", None))
        self.btn_Inic.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.btn_Inic.setText(_translate("MainWindow", "Inicio", None))
        self.btn_Cone.setText(_translate("MainWindow", "Conexión", None))
        self.btn_coma.setText(_translate("MainWindow", "Comando", None))
        self.btn_conf.setText(_translate("MainWindow", "Configuración", None))
        self.B3_lbl.setText(_translate("MainWindow", "Latitud", None))
        self.B3_btn.setText(_translate("MainWindow", "0", None))
        self.B6_lbl.setText(_translate("MainWindow", "Last Hearbeart", None))
        self.B6_btn.setText(_translate("MainWindow", "0", None))
        self.B4_lbl.setText(_translate("MainWindow", "Longitud", None))
        self.B4_btn.setText(_translate("MainWindow", "0", None))
        self.B5_lbl.setText(_translate("MainWindow", "Heading", None))
        self.B5_btn.setText(_translate("MainWindow", "0", None))
        self.B2_lbl.setText(_translate("MainWindow", "AirSpeed", None))
        self.B2_btn.setText(_translate("MainWindow", "0", None))
        self.B1_lbl.setText(_translate("MainWindow", "Altura", None))
        self.B1_btn.setText(_translate("MainWindow", "0", None))
        self.B7_lbl.setText(_translate("MainWindow", "GroundSpeed", None))
        self.B7_btn.setText(_translate("MainWindow", "0", None))
        self.B8_lbl.setText(_translate("MainWindow", "GPS Enabled", None))
        self.B8_btn.setText(_translate("MainWindow", "0", None))
        item = self.tablaMisiones.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Misión", None))
        item = self.tablaMisiones.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Referencia", None))
        item = self.tablaMisiones.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Param 1", None))
        item = self.tablaMisiones.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Param 2", None))
        item = self.tablaMisiones.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Param 3", None))
        item = self.tablaMisiones.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Param 4", None))
        item = self.tablaMisiones.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Eliminar", None))
        self.btn_descargar_mis.setText(_translate("MainWindow", "Descargar Misiones", None))
        self.btn_agregar_mis.setText(_translate("MainWindow", "Agregar Mision", None))
        self.btn_enviar_mis.setText(_translate("MainWindow", "Enviar Misiones", None))
        self.btn_empezar.setText(_translate("MainWindow", "Iniciar", None))
        self.ini_Tabs.setTabText(self.ini_Tabs.indexOf(self.LayoutMisiones), _translate("MainWindow", "Misiones", None))
        item = self.listAtributos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Atributo", None))
        item = self.listAtributos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Graficar", None))
        self.ini_Tabs.setTabText(self.ini_Tabs.indexOf(self.graficos), _translate("MainWindow", "Gráficos", None))
        self.gb_logVehiculo.setTitle(_translate("MainWindow", "Registro de conexión", None))
        self.pushButton.setText(_translate("MainWindow", "Borrar", None))
        self.gb_infoVehiculo.setTitle(_translate("MainWindow", "Información obtenida", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Vehículo", None))
        self.label_9.setText(_translate("MainWindow", "Tipo de vehículo", None))
        self.label_10.setText(_translate("MainWindow", "Firmware", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sensores", None))
        self.label_19.setText(_translate("MainWindow", "GPS", None))
        self.label_20.setText(_translate("MainWindow", "Bateria", None))
        self.label_14.setText(_translate("MainWindow", "Señal", None))
        self.groupBox.setTitle(_translate("MainWindow", "Sistema", None))
        self.label_17.setText(_translate("MainWindow", "Estado del Sistema", None))
        self.label_18.setText(_translate("MainWindow", "En condiciones para volar", None))
        self.grupoConectar.setTitle(_translate("MainWindow", "Conectar", None))
        self.label_2.setText(_translate("MainWindow", "Puerto:            ", None))
        self.label.setText(_translate("MainWindow", "Dirección IP:            ", None))
        self.inPort.setText(_translate("MainWindow", "14550", None))
        self.btn_conectar.setText(_translate("MainWindow", "Conectar", None))
        self.grupoBotones.setTitle(_translate("MainWindow", "Botones", None))
        self.label_4.setText(_translate("MainWindow", "1", None))
        self.label_3.setText(_translate("MainWindow", "2", None))
        self.label_5.setText(_translate("MainWindow", "3", None))
        self.label_6.setText(_translate("MainWindow", "4", None))
        self.grupoEjes.setTitle(_translate("MainWindow", "Ejes", None))
        self.invA0.setText(_translate("MainWindow", "Invertir", None))
        self.invA1.setText(_translate("MainWindow", "Invertir", None))
        self.invA2.setText(_translate("MainWindow", "Invertir", None))
        self.invA3.setText(_translate("MainWindow", "Invertir", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Mando", None))
        self.tablaConf_1.setSortingEnabled(False)
        item = self.tablaConf_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_1.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_1.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        __sortingEnabled = self.tablaConf_1.isSortingEnabled()
        self.tablaConf_1.setSortingEnabled(False)
        self.tablaConf_1.setSortingEnabled(__sortingEnabled)
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_1), _translate("MainWindow", "ArduPilot", None))
        item = self.tablaConf_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_2), _translate("MainWindow", "Armado", None))
        item = self.tablaConf_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_3), _translate("MainWindow", "Bateria", None))
        item = self.tablaConf_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_4), _translate("MainWindow", "Motores", None))
        item = self.tablaConf_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_5), _translate("MainWindow", "Servo OUTPUT", None))
        item = self.tablaConf_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_6.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_6), _translate("MainWindow", "Telemetría", None))
        item = self.tablaConf_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_7.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_7), _translate("MainWindow", "EK2", None))
        item = self.tablaConf_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_8.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_8.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_8), _translate("MainWindow", "Compas", None))
        item = self.tablaConf_9.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_9.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_9.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_9.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_9.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_9.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        __sortingEnabled = self.tablaConf_9.isSortingEnabled()
        self.tablaConf_9.setSortingEnabled(False)
        self.tablaConf_9.setSortingEnabled(__sortingEnabled)
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_9), _translate("MainWindow", "GPS", None))
        item = self.tablaConf_10.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_10.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_10.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_10.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_10.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_10.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_10), _translate("MainWindow", "Estadisticas", None))
        item = self.tablaConf_11.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_11.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_11.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_11.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_11.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_11.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_11), _translate("MainWindow", "RC", None))
        item = self.tablaConf_12.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_12.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_12.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_12.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_12.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_12.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_12), _translate("MainWindow", "Waypoint", None))
        item = self.tablaConf_13.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COD", None))
        item = self.tablaConf_13.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE", None))
        item = self.tablaConf_13.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIPCION", None))
        item = self.tablaConf_13.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "INTERVALO", None))
        item = self.tablaConf_13.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR", None))
        item = self.tablaConf_13.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UNIDADES", None))
        self.tabConfiguracion.setTabText(self.tabConfiguracion.indexOf(self.layoutConf_13), _translate("MainWindow", "Misiones", None))
        self.btnRestaurarParam.setText(_translate("MainWindow", "Restaurar", None))
        self.btnGuardarParam.setText(_translate("MainWindow", "Guardar", None))

class ComboBox(QtGui.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()
    prevIndex = 0
    __function = None
    __arguments = None

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        if self.__function != None:
            self.__function(self.__arguments)

        super(ComboBox, self).showPopup()
        self.prevIndex = self.currentIndex()

    def addCallback(self, f, *arg):
        self.__function = f
        self.__arguments = arg

    def previusIndex(self):
        return self.prevIndex

from PyQt4 import QtWebKit
