# from PyQt5 import uic
# from PyQt5.QtWidgets import QMainWindow
#
# class MainWindow(QMainWindow):
#    def __init__(self):
#       super(MainWindow, self).__init__()
#       uic.loadUi('mainwindow.ui', self)

from PyQt5 import QtCore, QtGui, QtWidgets
# from simple.gui import Ui_M
from simple import Ui_M  # у меня модуль simple.py в томже катклоге что и main.py


class MainClass(QtWidgets.QMainWindow, Ui_M):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(self.Push)

    def Push(self):
        self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = MainClass()  # <<<-----
    w.show()  # <<<-----

    #    Form = QtWidgets.QWidget()
    #    ui = Ui_M()
    #    ui.setupUi(Form)
    #    Form.show()

    sys.exit(app.exec_())
