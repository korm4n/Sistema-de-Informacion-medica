import mysql.connector
from mysql.connector import Error
import time

class CreateConnection:
    def __init__(self):
        self.usuario = 'SIMV'
        self.contrasena = 'TAcuato+-14'

    def create_connection(self):
        """Create a database connection to the MySQL database"""
        try:
            connection = mysql.connector.connect(
               host='localhost',
               database='sistema_informacion_medica',
               user=self.usuario,
               password=self.contrasena
             )
            if connection.is_connected():
               return connection
        except Error:
            pass
        except Exception:
            pass
        return None

    def check_connection(self, connection):
        """Check if the connection to the database is still active and return the result"""
        try:
            if connection.is_connected():
                return "Conectado"
            else:
                return "Desconectado"
        except Error:
            return "Desconectado"
        except Exception:
            return "Desconectado"

if __name__ == '__main__':
    db = CreateConnection()
    connection = db.create_connection()
    while True:
        estado = db.check_connection(connection)
        print(f"Estado de la conexión: {estado}")
        time.sleep(5)