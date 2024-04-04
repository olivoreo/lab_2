from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

import sys
from UI import Ui_MainWindow

if __name__ == "__main__":
    #application()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())