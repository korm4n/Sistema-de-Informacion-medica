import mysql.connector
from mysql.connector import Error

class ServicioDB:
    def __init__(self):
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='sistema_informacion_medica',
                user='tu_usuario',
                password='tu_contraseña'
            )
            if self.connection.is_connected():
                return True
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return False

    def desconectar(self):
        if self.connection.is_connected():
            self.connection.close()
            return True
        return False

    def estado_conexion(self):
        if self.connection and self.connection.is_connected():
            return "Conectado"
        return "Desconectado"