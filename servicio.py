import mysql.connector
from mysql.connector import Error
import time

class EstadoConexion():
    def create_connection(self):
        """Create a database connection to the MySQL database"""
        try:
            connection = mysql.connector.connect(
               host='localhost',
               database='sistema_informacion_medica',
               user='SIMV',
               password='TAcuato+-14'
             )
            if connection.is_connected():
               print("Conectado")
            return connection
        except Error:
            pass
        except Exception:
            pass
        print("Desconectado")
        return None

    def check_connection(self, connection):
        """Check if the connection to the database is still active and return the result"""
        try:
            if connection.is_connected():
                print("Conectado")
                return "Conectado"
            else:
                print("Desconectado")
                return "Desconectado"
        except Error:
            print("Desconectado")
            return "Desconectado"
        except Exception:
            print("Desconectado")
            return "Desconectado"

if __name__ == '__main__':
    db = EstadoConexion()
    connection = db.create_connection()
    while True:
        estado = db.check_connection(connection)
        print(f"Estado de la conexión: {estado}")
        time.sleep(5)