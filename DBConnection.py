import mysql.connector


class RegistroDatos:
    # Esto es para crear la conexion a la base de datos
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost', database="productosBD", user='josef7',
                                                password="Jose-072000")

    # Funcion para insertar productos
    def insertar_productos(self, codigo, nombre, modelo, precio, cantidad):
        cursor = self.conexion.cursor()
        sql = '''
        INSERT INTO productos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD)
        VALUES('{}', '{}', '{}', '{}', '{}')'''.format(codigo, nombre, modelo, precio, cantidad)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    # Funcion para buscar TODOS los productos
    def buscar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos"
        cursor.execute(sql)
        registro = cursor.fetchall()
        cursor.close()
        return registro

    # Funcion para buscar un solo producto especifico
    def buscar_producto(self, nombre_producto):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_producto)
        cursor.execute(sql)
        registro = cursor.fetchall()
        cursor.close()
        return registro

    # Funcion para buscar un solo producto especifico por el codigo
    def buscar_id_producto(self, codigo_producto):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE CODIGO = {}".format(codigo_producto)
        cursor.execute(sql)
        registro = cursor.fetchall()
        cursor.close()
        return registro

    # Funcion para eliminar productos
    def eliminar_productos(self, codigo_producto):
        cursor = self.conexion.cursor()
        sql = "DELETE FROM productos WHERE CODIGO = {}".format(codigo_producto)
        cursor.execute(sql)
        registro = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return registro

    # Funcion para actualizar los productos
    def actualizar_productos(self, codigo, nombre, modelo, precio, cantidad):
        cursor = self.conexion.cursor()
        sql = '''
        UPDATE productos SET NOMBRE="{}", MODELO="{}", PRECIO="{}", CANTIDAD="{}"
        WHERE CODIGO="{}"'''.format(nombre, modelo, precio, cantidad, codigo)
        cursor.execute(sql)
        registro = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return registro
