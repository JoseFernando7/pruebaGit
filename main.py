import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class PruebaGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("prueba.ui", self)

        self.btn2.setEnabled(False)
        self.btn1.clicked.connect(self.fn_activar)
        self.btn2.clicked.connect(self.fn_desactivar)

    def fn_activar(self):
        self.btn2.setEnabled(True)
        self.btn1.setEnabled(False)
        self.et.setText("Equisdé :)")

    def fn_desactivar(self):
        self.btn2.setEnabled(False)
        self.btn1.setEnabled(True)
        self.et.setText(":(")

    def funcionInutil(self):
        print("Hola soy una funcion y no sirvo para nada, igual que el Manchester United :'v")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = PruebaGUI()
    GUI.show()
    sys.exit(app.exec_())
