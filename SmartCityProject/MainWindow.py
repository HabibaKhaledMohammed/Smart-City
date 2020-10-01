# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 600)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 80, 571, 331))
        self.pushButton.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/smart-city-686x386.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(500, 500))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 440, 151, 51))
        self.pushButton_2.setStyleSheet("background-color:rgb(0, 85, 127);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 20, 31, 21))
        self.label_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 40, 31, 21))
        self.label_3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 20, 31, 21))
        self.label_4.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 40, 31, 21))
        self.label_5.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 20, 31, 21))
        self.label_6.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 40, 31, 21))
        self.label_7.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 20, 31, 21))
        self.label_8.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 40, 31, 21))
        self.label_9.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(260, 20, 31, 21))
        self.label_10.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 0, 16, 21))
        self.label_11.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(230, 20, 16, 20))
        self.label_12.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(230, 0, 16, 21))
        self.label_13.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(350, 0, 16, 20))
        self.label_14.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(310, 0, 16, 20))
        self.label_15.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(310, 20, 16, 20))
        self.label_16.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(270, 0, 16, 20))
        self.label_17.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(500, 20, 16, 20))
        self.label_18.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(500, 0, 16, 20))
        self.label_19.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(580, 20, 16, 20))
        self.label_20.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(580, 0, 16, 20))
        self.label_21.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(540, 0, 16, 20))
        self.label_22.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(460, 0, 16, 20))
        self.label_23.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 14pt \"Kozuka Gothic Pro B\";\n"
"color:rgb(0,0,0);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "  C"))
        self.label_3.setText(_translate("MainWindow", "   I"))
        self.label_4.setText(_translate("MainWindow", "  T"))
        self.label_5.setText(_translate("MainWindow", "  Y"))
        self.label_6.setText(_translate("MainWindow", "  S"))
        self.label_7.setText(_translate("MainWindow", " M"))
        self.label_8.setText(_translate("MainWindow", "  T"))
        self.label_9.setText(_translate("MainWindow", "  A"))
        self.label_10.setText(_translate("MainWindow", "  R"))



