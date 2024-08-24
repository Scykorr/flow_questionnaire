from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.main_page import Ui_MainWindow


class MainClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.choose_operator_1)
        self.pushButton_2.clicked.connect(self.choose_operator_2)
        self.pushButton_5.clicked.connect(self.get_new_task)

    def choose_operator_1(self):
        self.stackedWidget.setCurrentIndex(1)
        self.textBrowser.append(self.pushButton.text())

    def choose_operator_2(self):
        self.stackedWidget.setCurrentIndex(1)
        self.textBrowser.append(self.pushButton_2.text())

    def get_new_task(self):
        self.stackedWidget.setCurrentIndex(0)
        self.textBrowser.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = MainClass()
    w.show()

    sys.exit(app.exec_())
