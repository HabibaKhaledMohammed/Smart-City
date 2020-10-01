from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import QDialog, QApplication ,QMainWindow
from HelpWindow.InformationWindow import *
import HelpWindow.InformationWindow as helpwindow
from SmartCityGUI import *
import SmartCityGUI as smartcity
from MainWindow import *
import webbrowser
class main (QDialog ,smartcity.Ui_Dialog ):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(" Smart City Analysis & Find Best Path")
        self.pushButton.clicked.connect(self.FirstWindow)
        self.pushButton_2.clicked.connect(self.SearchIcon)
        self.pushButton_43.clicked.connect(self.HelpIcon)
    def FirstWindow(self):
        self.w = FirstMainWindow()
        self.w.show()
        self.close()

    def SearchIcon(self):
        webbrowser.open('https://github.com/AmiinaAhmed/SmartCity')


    def HelpIcon(self):
        self.w = Informationwindow()
        self.w.aboutUs()
        self.w.show()
class FirstMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Smart City Analysis & Find Best Path")
        self.pushButton_2.clicked.connect(self.mainWindow)

    def mainWindow(self):
        self.w = main()
        self.w.show()
        self.close()
class Informationwindow (QDialog , helpwindow.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(" Smart City Analysis & Find Best Path")

    def aboutUs(self):
        f = open('images/Report.txt', 'r')
        data = f.readlines()
        f.close()
        text = ""
        for x in data:
            text += x.strip() + "\n"
        self.label.setText(text)
        self.label.resize(self.width(), self.height())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/Image20190428005622.png"));
    window = FirstMainWindow()
    window.show()
    sys.exit(app.exec())

