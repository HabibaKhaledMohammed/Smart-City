from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.cluster import AgglomerativeClustering
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use('TkAgg')
import warnings; warnings.filterwarnings(action='once')
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import calmap
import DVFunction.Correlation as co
import DVFunction.Deviation as de
import DVFunction.Distribution as di
import DVFunction.Ranking as ra
import DVFunction.Composition as comp
import DVFunction.Groups as gro
import DVFunction.Change as cha
import gc
try:
    import collections.abc as collections_abc # only works on python 3.3+
except ImportError:
    import collections as collections_abc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(957, 587)
        Dialog.setModal(False)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 961, 621))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MV Boli\";")
        self.tabWidget.setIconSize(QtCore.QSize(40, 40))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 961, 571))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("font: 75 11pt \"Maiandra GD\";\n"
"background-color: rgb(0,0,0);")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 490, 41, 41))
        self.pushButton_2.setStyleSheet("border: 2px solid  rgb(52, 85, 97);")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Image20190428005646.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 490, 41, 41))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border: 2px solid  rgb(52, 85, 97);")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Image20190428005622.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 40, 80, 26))
        self.pushButton_3.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 70, 181, 26))
        self.pushButton_4.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 100, 211, 26))
        self.pushButton_5.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 130, 161, 26))
        self.pushButton_6.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 160, 101, 26))
        self.pushButton_7.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 190, 151, 26))
        self.pushButton_8.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 220, 131, 26))
        self.pushButton_9.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 250, 91, 26))
        self.pushButton_10.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 280, 91, 26))
        self.pushButton_11.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 70, 111, 26))
        self.pushButton_12.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_13.setGeometry(QtCore.QRect(290, 40, 101, 26))
        self.pushButton_13.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_14.setGeometry(QtCore.QRect(290, 100, 131, 26))
        self.pushButton_14.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_15.setGeometry(QtCore.QRect(290, 130, 171, 26))
        self.pushButton_15.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_16.setGeometry(QtCore.QRect(290, 160, 81, 26))
        self.pushButton_16.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_17.setGeometry(QtCore.QRect(550, 130, 81, 26))
        self.pushButton_17.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_18.setGeometry(QtCore.QRect(550, 160, 101, 26))
        self.pushButton_18.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_19.setGeometry(QtCore.QRect(550, 40, 121, 26))
        self.pushButton_19.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_20.setGeometry(QtCore.QRect(550, 70, 101, 26))
        self.pushButton_20.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_21.setGeometry(QtCore.QRect(290, 220, 171, 26))
        self.pushButton_21.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_22.setGeometry(QtCore.QRect(550, 100, 75, 26))
        self.pushButton_22.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_23.setGeometry(QtCore.QRect(290, 250, 161, 26))
        self.pushButton_23.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_24.setGeometry(QtCore.QRect(290, 280, 91, 26))
        self.pushButton_24.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_25.setGeometry(QtCore.QRect(290, 310, 211, 26))
        self.pushButton_25.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_26.setGeometry(QtCore.QRect(290, 340, 75, 26))
        self.pushButton_26.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_27.setGeometry(QtCore.QRect(550, 340, 75, 26))
        self.pushButton_27.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_28.setGeometry(QtCore.QRect(550, 310, 71, 26))
        self.pushButton_28.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_29.setGeometry(QtCore.QRect(550, 280, 71, 26))
        self.pushButton_29.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_30.setGeometry(QtCore.QRect(550, 250, 91, 26))
        self.pushButton_30.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_30.setObjectName("pushButton_30")
       # self.pushButton_31 = QtWidgets.QPushButton(self.groupBox)
        #self.pushButton_31.setGeometry(QtCore.QRect(290, 520, 121, 26))
      #  self.pushButton_31.setStyleSheet("background-color: rgb(170, 63, 0);\n"
#"color: rgb(255, 255, 255);\n"
#"")
       # self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_32.setGeometry(QtCore.QRect(290, 490, 141, 26))
        self.pushButton_32.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_33.setGeometry(QtCore.QRect(290, 460, 91, 26))
        self.pushButton_33.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_34.setGeometry(QtCore.QRect(290, 430, 111, 26))
        self.pushButton_34.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_35.setGeometry(QtCore.QRect(290, 400, 75, 26))
        self.pushButton_35.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_36.setGeometry(QtCore.QRect(290, 370, 141, 26))
        self.pushButton_36.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_36.setObjectName("pushButton_36")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(300, 190, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(570, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(810, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(580, 380, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(570, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.pushButton_41 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_41.setGeometry(QtCore.QRect(750, 340, 131, 26))
        self.pushButton_41.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_56 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_56.setGeometry(QtCore.QRect(750, 160, 171, 26))
        self.pushButton_56.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_52 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_52.setGeometry(QtCore.QRect(750, 70, 151, 26))
        self.pushButton_52.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_38 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_38.setGeometry(QtCore.QRect(750, 190, 161, 26))
        self.pushButton_38.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_38.setObjectName("pushButton_38")
        #self.pushButton_37 = QtWidgets.QPushButton(self.groupBox)
        #self.pushButton_37.setGeometry(QtCore.QRect(750, 220, 141, 26))
        #self.pushButton_37.setStyleSheet("background-color: rgb(170, 63, 0);\n"
#"color: rgb(255, 255, 255);\n"
#"")
        #self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_39 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_39.setGeometry(QtCore.QRect(750, 220, 171, 26))
        self.pushButton_39.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_55 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_55.setGeometry(QtCore.QRect(750, 130, 151, 26))
        self.pushButton_55.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_54 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_54.setGeometry(QtCore.QRect(750, 100, 141, 26))
        self.pushButton_54.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_40 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_40.setGeometry(QtCore.QRect(750, 250, 151, 26))
        self.pushButton_40.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_51 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_51.setGeometry(QtCore.QRect(750, 40, 111, 26))
        self.pushButton_51.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_53 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_53.setGeometry(QtCore.QRect(750, 310, 91, 26))
        self.pushButton_53.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_42 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_42.setGeometry(QtCore.QRect(750, 280, 131, 26))
        self.pushButton_42.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_48 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_48.setGeometry(QtCore.QRect(550, 480, 111, 26))
        self.pushButton_48.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_47 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_47.setGeometry(QtCore.QRect(550, 510, 141, 26))
        self.pushButton_47.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_50 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_50.setGeometry(QtCore.QRect(550, 420, 91, 26))
        self.pushButton_50.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_49 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_49.setGeometry(QtCore.QRect(550, 450, 81, 26))
        self.pushButton_49.setStyleSheet("background-color: rgb(40,64,73);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_43 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_43.setGeometry(QtCore.QRect(150, 490, 41, 41))
        self.pushButton_43.setStyleSheet("border: 2px solid  rgb(40,64,73);")
        self.pushButton_43.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_43.setIcon(icon2)
        self.pushButton_43.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_43.setObjectName("pushButton_43")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(0, -10, 191, 571))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("font: 75 11pt \"Maiandra GD\";\n"
"background-color: rgb(0,0,0);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_44 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_44.setGeometry(QtCore.QRect(40, 50, 111, 25))
        self.pushButton_44.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_44.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"MV Boli\";\n"
"border: 2px solid  rgb(52, 85, 97);\n"
"background-color: rgb(40,64,73);")
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_45.setGeometry(QtCore.QRect(40, 170, 111, 25))
        self.pushButton_45.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_45.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"MV Boli\";\n"
"border: 2px solid  rgb(52, 85, 97);\n"
"background-color: rgb(40,64,73);")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_46.setGeometry(QtCore.QRect(40, 110, 111, 25))
        self.pushButton_46.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_46.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"MV Boli\";\n"
"border: 2px solid  rgb(52, 85, 97);\n"
"background-color: rgb(40,64,73);")
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_57 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_57.setGeometry(QtCore.QRect(40, 230, 111, 25))
        self.pushButton_57.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_57.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"MV Boli\";\n"
"border: 2px solid  rgb(52, 85, 97);\n"
"background-color: rgb(40,64,73);")
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_58.setGeometry(QtCore.QRect(40, 290, 111, 25))
        self.pushButton_58.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_58.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"MV Boli\";\n"
"border: 2px solid  rgb(52, 85, 97);\n"
"background-color: rgb(40,64,73);")
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_59.setGeometry(QtCore.QRect(40, 350, 111, 25))
        self.pushButton_59.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_59.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"MV Boli\";\n"
"border: 2px solid  rgb(52, 85, 97);\n"
"background-color: rgb(40,64,73);")
        self.pushButton_59.setObjectName("pushButton_59")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(200, 0, 751, 541))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 748, 501))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_14.setObjectName("label_14")
        self.pushButton_62 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_62.setGeometry(QtCore.QRect(220, 0, 301, 41))
        self.pushButton_62.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_62.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"MV Boli\";\n"
"border: 2px solid  rgb(52, 85, 97);\n"
"background-color: rgb(40,64,73);")
        self.pushButton_62.setObjectName("pushButton_62")
        self.tabWidget.addTab(self.tab_2, "")
        ############################ change#######################################
        self.pushButton_100 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_100.setGeometry(QtCore.QRect(20, 310, 140, 30))
        self.pushButton_100.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(40,64,73);")
        self.pushButton_100.setObjectName("pushButton_100")
        ##########################################################################
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Find_Path()
        self.pushButtonsActions()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "Scatter plot"))
        self.pushButton_4.setText(_translate("Dialog", "Bubble plot with Encircling"))
        self.pushButton_5.setText(_translate("Dialog", "Scatter plot with line of best fit"))
        self.pushButton_6.setText(_translate("Dialog", "Jittering with stripplot"))
        self.pushButton_7.setText(_translate("Dialog", "Counts Plot"))
        self.pushButton_8.setText(_translate("Dialog", "Marginal Histogram"))
        self.pushButton_9.setText(_translate("Dialog", "Marginal Boxplot"))
        self.pushButton_10.setText(_translate("Dialog", "Correlogram"))
        self.pushButton_11.setText(_translate("Dialog", "Pairwise Plot"))
        self.pushButton_12.setText(_translate("Dialog", "Diverging Texts"))
        self.pushButton_13.setText(_translate("Dialog", "Diverging Bars"))
        self.pushButton_14.setText(_translate("Dialog", "Diverging Dot Plot"))
        self.pushButton_15.setText(_translate("Dialog", "Diverging Lollipop Chart "))
        self.pushButton_16.setText(_translate("Dialog", "Area Chart"))
        self.pushButton_17.setText(_translate("Dialog", "Slope Chart"))
        self.pushButton_18.setText(_translate("Dialog", "Dumbbell Plot"))
        self.pushButton_19.setText(_translate("Dialog", "Ordered Bar Chart"))
        self.pushButton_20.setText(_translate("Dialog", "Lollipop Chart"))
        self.pushButton_21.setText(_translate("Dialog", "Histogram for Cont.Var"))
        self.pushButton_22.setText(_translate("Dialog", "Dot Plot"))
        self.pushButton_23.setText(_translate("Dialog", "Histogram for Cat.Var"))
        self.pushButton_24.setText(_translate("Dialog", "Density Plot"))
        self.pushButton_25.setText(_translate("Dialog", "Density Curves with Histogram"))
        self.pushButton_26.setText(_translate("Dialog", "Joy Plot"))
        self.pushButton_27.setText(_translate("Dialog", "Bar Chart"))
        self.pushButton_28.setText(_translate("Dialog", "Treemap"))
        self.pushButton_29.setText(_translate("Dialog", "Pie Chart"))
        self.pushButton_30.setText(_translate("Dialog", "Waffle Chart"))
        #self.pushButton_31.setText(_translate("Dialog", "Categorical Plots"))
        self.pushButton_32.setText(_translate("Dialog", "Population Pyramid"))
        self.pushButton_33.setText(_translate("Dialog", "Violin Plot"))
        self.pushButton_34.setText(_translate("Dialog", "Dot + Box Plot"))
        self.pushButton_35.setText(_translate("Dialog", "Box Plot"))
        self.pushButton_36.setText(_translate("Dialog", "Distributed Dot Plot"))
        self.label.setText(_translate("Dialog", " Correlation :"))
        self.label_2.setText(_translate("Dialog", "Deviation :"))
        self.label_3.setText(_translate("Dialog", "Distribution :"))
        self.label_4.setText(_translate("Dialog", "Ranking :"))
        self.label_5.setText(_translate("Dialog", "Change :"))
        self.label_6.setText(_translate("Dialog", "Groups :"))
        self.label_7.setText(_translate("Dialog", "Composition :"))
        self.pushButton_41.setText(_translate("Dialog", "Stacked Area Chart"))
        self.pushButton_56.setText(_translate("Dialog", "Time Decomposition Plot"))
        self.pushButton_52.setText(_translate("Dialog", "Time Series with Peaks"))
        self.pushButton_38.setText(_translate("Dialog", "Plotting with different "))
        #self.pushButton_37.setText(_translate("Dialog", "Multiple Time Series"))
        self.pushButton_39.setText(_translate("Dialog", "Time Series with E.Bands"))
        self.pushButton_55.setText(_translate("Dialog", "Cross Correlation Plot"))
        self.pushButton_54.setText(_translate("Dialog", "Autocorrelation Plot"))
        self.pushButton_40.setText(_translate("Dialog", "Area Chart Unstacked"))
        self.pushButton_51.setText(_translate("Dialog", "Time Series Plot"))
        self.pushButton_53.setText(_translate("Dialog", "Seasonal Plot"))
        self.pushButton_42.setText(_translate("Dialog", "Calendar Heat Map"))
        self.pushButton_48.setText(_translate("Dialog", "Andrews Curve"))
        self.pushButton_47.setText(_translate("Dialog", "Parallel Coordinates"))
        self.pushButton_50.setText(_translate("Dialog", "Dendrogram"))
        self.pushButton_49.setText(_translate("Dialog", "Cluster Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Charts of Smart City"))
        self.pushButton_44.setText(_translate("Dialog", "Path 1"))
        self.pushButton_45.setText(_translate("Dialog", "Path 3"))
        self.pushButton_46.setText(_translate("Dialog", "Path 2"))
        self.pushButton_57.setText(_translate("Dialog", "Path 4"))
        self.pushButton_58.setText(_translate("Dialog", "Path 5"))
        self.pushButton_59.setText(_translate("Dialog", "Path 6"))
        #############################change################################
        self.pushButton_100.setText(_translate("Dialog", "Each regression line"))
        ###################################################################
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_62.setText(_translate("Dialog", "Show Way"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Best Path To Arrive"))


    def pushButtonsActions(self):
            #################Correlation###############
            self.pushButton_3.clicked.connect(co.Scatter_plot)
            self.pushButton_4.clicked.connect(co.Bubble_plot_with_Encircling)
            self.pushButton_5.clicked.connect(co.Scatter_plot_with_linear_regression_line_of_best_fit)
            self.pushButton_6.clicked.connect(co.Jittering_with_stripplot)
            self.pushButton_7.clicked.connect(co.Counts_Plot)
            self.pushButton_8.clicked.connect(co.Marginal_Histogram)
            self.pushButton_9.clicked.connect(co.Marginal_Boxplot)
            self.pushButton_10.clicked.connect(co.Correllogram)
            self.pushButton_11.clicked.connect(co.Pairwise_Plot)
            self.pushButton_100.clicked.connect(co.Each_regression_line_in_its_own_column)
            ###################################################################################
            #################Deviation###############
            self.pushButton_12.clicked.connect(de.DivergingTexts)
            self.pushButton_13.clicked.connect(de.DivergingBars)
            self.pushButton_14.clicked.connect(de.DivergingDotPlot)
            self.pushButton_15.clicked.connect(de.DivergingLollipopChartwithMarkers)
            self.pushButton_16.clicked.connect(de.AreaChart)
            ####################################################################333
            #################Distribution###############

            self.pushButton_21.clicked.connect(di.HistogramforContinuousVariable)
            self.pushButton_23.clicked.connect(di.HistogramforCategoricalVariable)
            self.pushButton_24.clicked.connect(di.DensityPlot)
            self.pushButton_25.clicked.connect(di.DensityCurveswithHistogram)
            self.pushButton_26.clicked.connect(di.JoyPlot)
            self.pushButton_36.clicked.connect(di.DistributedDotPlot)
            self.pushButton_35.clicked.connect(di.BoxPlot)
            self.pushButton_34.clicked.connect(di.DotPlusBoxPlot)
            self.pushButton_33.clicked.connect(di.ViolinPlot)
            self.pushButton_32.clicked.connect(di.PopulationPyramid)
            #self.pushButton_31.clicked.connect(Ditribution.CategoricalPlots)
            ####################################################
            #################Ranking###############
            self.pushButton_19.clicked.connect(ra.Ordered_Bar_Chart)
            self.pushButton_20.clicked.connect(ra.Lollipop_Chart)
            self.pushButton_22.clicked.connect(ra.Dot_Plot)
            self.pushButton_17.clicked.connect(ra.Slope_Chart)
            self.pushButton_18.clicked.connect(ra.Dumbbell_Plot)
            ####################################################
            #################Composition###############
            self.pushButton_30.clicked.connect(comp.Waffle_Chart)
            self.pushButton_29.clicked.connect(comp.Pie_Chart)
            self.pushButton_28.clicked.connect(comp.Treemap)
            self.pushButton_27.clicked.connect(comp.Bar_Chart)
            ####################################################
            #################Groups###############
            self.pushButton_50.clicked.connect(gro.Dendrogram)
            self.pushButton_49.clicked.connect(gro.ClusterPlot)
            self.pushButton_48.clicked.connect(gro.AndrewsCurve)
            self.pushButton_47.clicked.connect(gro.ParallelCoordinates)
            ####################################################
            #################Change###############
            self.pushButton_51.clicked.connect(cha.Time_Series_Plot)
            self.pushButton_52.clicked.connect(cha.Time_Series_with_Peaks_and_Troughs_Annotated)

            self.pushButton_54.clicked.connect(cha.Autocorrelation_ACF_and_Partial_Autocorrelation_PACF_Plot)
            self.pushButton_55.clicked.connect(cha.Cross_Correlation_plot)
            self.pushButton_56.clicked.connect(cha.Time_Series_Decomposition_Plot)
            self.pushButton_38.clicked.connect(cha.Plotting_with_different_scales_using_secondary_Y_axis)
            #self.pushButton_37.clicked.connect(Change.Multiple_Time_Series)
            self.pushButton_39.clicked.connect(cha.Time_Series_with_Error_Bands)
            self.pushButton_40.clicked.connect(cha.Area_Chart_UnStacked)
            self.pushButton_42.clicked.connect(cha.Calendar_Heat_Map)
            self.pushButton_53.clicked.connect(cha.Seasonal_Plot)
            self.pushButton_41.clicked.connect(cha.Stacked_Area_Chart)



    def Find_Path(self):
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_3)
        self.scrollArea.setGeometry(QtCore.QRect(0, 50, 745, 490))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidget(self.label_14)

        self.pushButton_44.clicked.connect(self.path1)
        self.pushButton_46.clicked.connect(self.path2)
        self.pushButton_45.clicked.connect(self.path3)
        self.pushButton_57.clicked.connect(self.path4)
        self.pushButton_58.clicked.connect(self.path5)
        self.pushButton_59.clicked.connect(self.path6)

        self.pushButton_62.clicked.connect(self.heavypath)

    def path1(self):
        self.pushButton_44.setObjectName("path1")
        self.pushButton_46.setObjectName("pushButton")
        self.pushButton_45.setObjectName("pushButton")
        self.pushButton_62.setObjectName("pushButton")
        self.pushButton_57.setObjectName("pushButton")
        self.pushButton_58.setObjectName("pushButton")
        self.pushButton_59.setObjectName("pushButton")
        pixmap1 = QtGui.QPixmap("dataset/sampleGraph1.jpg")
        self.pixmap = pixmap1.scaled(self.width(), self.height())
        self.label_14.setPixmap(self.pixmap)
        self.label_14.resize(self.width(), self.height())

    def path2(self):
        self.pushButton_46.setObjectName("path2")
        self.pushButton_44.setObjectName("pushButton")
        self.pushButton_62.setObjectName("pushButton")
        self.pushButton_57.setObjectName("pushButton")
        self.pushButton_45.setObjectName("pushButton")
        self.pushButton_58.setObjectName("pushButton")
        self.pushButton_59.setObjectName("pushButton")
        pixmap1 = QtGui.QPixmap("dataset/sampleGraph2.jpg")
        self.pixmap = pixmap1.scaled(self.width(), self.height())
        self.label_14.setPixmap(self.pixmap)
        self.label_14.resize(self.width(), self.height())

    def path3(self):
        self.pushButton_45.setObjectName("path3")
        self.pushButton_44.setObjectName("pushButton")
        self.pushButton_62.setObjectName("pushButton")
        self.pushButton_46.setObjectName("pushButton")
        self.pushButton_57.setObjectName("pushButton")
        self.pushButton_58.setObjectName("pushButton")
        self.pushButton_59.setObjectName("pushButton")
        pixmap1 = QtGui.QPixmap("dataset/sampleGraph3.jpg")
        self.pixmap = pixmap1.scaled(self.width(), self.height())
        self.label_14.setPixmap(self.pixmap)
        self.label_14.resize(self.width(), self.height())

    def path4(self):
        self.pushButton_57.setObjectName("path4")
        self.pushButton_46.setObjectName("pushButton")
        self.pushButton_62.setObjectName("pushButton")
        self.pushButton_45.setObjectName("pushButton")
        self.pushButton_44.setObjectName("pushButton")
        self.pushButton_58.setObjectName("pushButton")
        self.pushButton_59.setObjectName("pushButton")
        pixmap1 = QtGui.QPixmap("dataset/sampleGraph4.jpg")
        self.pixmap = pixmap1.scaled(self.width(), self.height())
        self.label_14.setPixmap(self.pixmap)
        self.label_14.resize(self.width(), self.height())

    def path5(self):
        self.pushButton_58.setObjectName("path5")
        self.pushButton_44.setObjectName("pushButton")
        self.pushButton_62.setObjectName("pushButton")
        self.pushButton_45.setObjectName("pushButton")
        self.pushButton_46.setObjectName("pushButton")
        self.pushButton_57.setObjectName("pushButton")
        self.pushButton_59.setObjectName("pushButton")
        pixmap1 = QtGui.QPixmap("dataset/sampleGraph5.jpg")
        self.pixmap = pixmap1.scaled(self.width(), self.height())
        self.label_14.setPixmap(self.pixmap)
        self.label_14.resize(self.width(), self.height())

    def path6(self):
        self.pushButton_59.setObjectName("path6")
        self.pushButton_44.setObjectName("pushButton")
        self.pushButton_62.setObjectName("pushButton")
        self.pushButton_45.setObjectName("pushButton")
        self.pushButton_46.setObjectName("pushButton")
        self.pushButton_57.setObjectName("pushButton")
        self.pushButton_58.setObjectName("pushButton")
        pixmap1 = QtGui.QPixmap("dataset/sampleGraph6.jpg")
        self.pixmap = pixmap1.scaled(self.width(), self.height())
        self.label_14.setPixmap(self.pixmap)
        self.label_14.resize(self.width(), self.height())

    def heavypath(self):
        if self.pushButton_44.objectName() == "path1":
                f = open('output/sampleGraph1.txt.result', 'r')
                data = f.read()
                f.close()
                self.label_14.setText(data)
        elif self.pushButton_46.objectName() == "path2":
                f = open('output/sampleGraph2.txt.result','r')
                data = f.read()
                f.close()
                self.label_14.setText(data)
        elif self.pushButton_45.objectName() == "path3":
                f = open('output/sampleGraph3.txt.result','r')
                data = f.read()
                f.close()
                self.label_14.setText(data)
        elif self.pushButton_57.objectName() == "path4":
                f = open('output/sampleGraph4.txt.result','r')
                data = f.read()
                f.close()
                self.label_14.setText(data)
        elif self.pushButton_58.objectName() == "path5":
                f = open('output/sampleGraph5.txt.result','r')
                data = f.read()
                f.close()
                self.label_14.setText(data)
        elif self.pushButton_59.objectName() == "path6":
                f = open('output/sampleGraph6.txt.result','r')
                data = f.read()
                f.close()
                self.label_14.setText(data)
        else:
                self.label_14.setText("Select path")









