import mysql.connector
from mysql.connector import errorcode

# Configuración de la conexión
config = {
    'user': 'SIMV',
    'password': 'TAcuato+-14',
    'host': 'localhost'
}

# Conectar a MySQL
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Crear la base de datos si no existe
    cursor.execute("CREATE DATABASE IF NOT EXISTS simv")
    print("Base de datos 'simv' creada o ya existe.")

    # Conectar a la base de datos 'simv'
    cnx.database = 'simv'

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error en el nombre de usuario o contraseña")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe y no se pudo crear")
    else:
        print(err)
else:
    cursor.close()
    cnx.close()