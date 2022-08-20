import sys
from gui import *
from DBConnection import *
from PyQt5.QtWidgets import QTableWidgetItem


class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.datosTotal = RegistroDatos()
        self.ui.bRefrescar.clicked.connect(self.mProductos)
        self.ui.bAgrProducto.clicked.connect(self.insertProductos)
        self.ui.bBuscar.clicked.connect(self.buscarProducto)
        self.ui.bBorrar.clicked.connect(self.eliminarProducto)
        self.ui.bActualizar.clicked.connect(self.modificarProductos)

        self.ui.tProductos.setColumnWidth(0, 170)
        self.ui.tProductos.setColumnWidth(1, 170)
        self.ui.tProductos.setColumnWidth(2, 170)
        self.ui.tProductos.setColumnWidth(3, 170)
        self.ui.tProductos.setColumnWidth(4, 170)

        self.ui.tProductosB.setColumnWidth(0, 170)
        self.ui.tProductosB.setColumnWidth(1, 170)
        self.ui.tProductosB.setColumnWidth(2, 170)
        self.ui.tProductosB.setColumnWidth(3, 170)
        self.ui.tProductosB.setColumnWidth(4, 170)

        self.ui.tProductosDlt.setColumnWidth(0, 170)
        self.ui.tProductosDlt.setColumnWidth(1, 170)
        self.ui.tProductosDlt.setColumnWidth(2, 170)
        self.ui.tProductosDlt.setColumnWidth(3, 170)
        self.ui.tProductosDlt.setColumnWidth(4, 170)

    def mProductos(self):
        datos = self.datosTotal.buscar_productos()
        i = len(datos)

        self.ui.tProductos.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.ui.tProductos.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tProductos.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tProductos.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tProductos.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tProductos.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1

    def insertProductos(self):
        codigo = self.ui.inputACodigo.text()
        nombre = self.ui.inputANombre.text()
        modelo = self.ui.inputAModelo.text()
        precio = self.ui.inputAPrecio.text()
        cantidad = self.ui.inputACantidad.text()

        self.datosTotal.insertar_productos(codigo, nombre, modelo, precio, cantidad)
        self.ui.inputACodigo.clear()
        self.ui.inputANombre.clear()
        self.ui.inputAModelo.clear()
        self.ui.inputAPrecio.clear()
        self.ui.inputACantidad.clear()

    def modificarProductos(self):
        id_producto = self.ui.idProducto.text()
        id_producto = str("'" + id_producto + "'")
        nombreX = self.datosTotal.buscar_producto(id_producto)
        print(nombreX)

        if nombreX:
            self.ui.bBuscarAct.setText("ACTUALIZAR")

            codigoM = self.ui.actCodigo.text()
            nombreM = self.ui.actNombre.text()
            modeloM = self.ui.actModelo.text()
            precioM = self.ui.acrPrecio.text()
            cantidadM = self.ui.actCantidad.text()

            act = self.datosTotal.actualizar_productos(codigoM, nombreM, modeloM, precioM, cantidadM)
            if act == 1:
                self.ui.bBuscarAct.setText("ACTUALIZADO")
                self.ui.actCodigo.clear()
                self.ui.actNombre.clear()
                self.ui.actModelo.clear()
                self.ui.acrPrecio.clear()
                self.ui.actCantidad.clear()
                self.ui.bBuscarAct.setText("Buscar")
            elif act == 0:
                self.ui.bBuscarAct.setText("ERROR")
            else:
                self.ui.bBuscarAct.setText("INCORRECTO")
        else:
            self.ui.bBuscarAct.setText("NO EXISTE")

    def buscarProducto(self):
        nombreProducto = self.ui.inputBuscar.text()
        nombreProducto = str("'" + nombreProducto + "'")

        datosB = self.datosTotal.buscar_producto(nombreProducto)
        i = len(datosB)

        self.ui.tProductosB.setRowCount(i)
        tablerow = 0
        for row in datosB:
            self.ui.tProductosB.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tProductosB.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tProductosB.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tProductosB.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tProductosB.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1

    def eliminarProducto(self):
        eliminar = self.ui.inputBuscarDlt.text()
        eliminar = str("'" + eliminar + "'")

        respuesta = (self.datosTotal.eliminar_productos(eliminar))
        datos = self.datosTotal.buscar_productos()
        i = len(datos)

        self.ui.tProductosDlt.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tProductosDlt.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tProductosDlt.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tProductosDlt.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tProductosDlt.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tProductosDlt.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1

        if not respuesta:
            self.ui.bOkDlt.setText("NO EXISTE")
        elif respuesta == 0:
            self.ui.bOkDlt.setText("NO EXISTE")
        else:
            self.ui.bOkDlt.setText("ELIMINADO CORRECTAMENTE")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    miApp = MiApp()
    miApp.show()
    sys.exit(app.exec_())
