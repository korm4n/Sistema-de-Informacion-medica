import mysql.connector
from mysql.connector import errorcode
from frames.db_config import DB_USER, DB_PASSWORD

class CrearBaseDatos:

    def __init__(self):
        self.connection = None
        self.usuario = DB_USER
        self.contrasena = DB_PASSWORD

    def crear_base_datos(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user=self.usuario,
                password=self.contrasena
            )
            cursor = self.connection.cursor()

            cursor.execute("SHOW DATABASES LIKE 'sistema_informacion_medica'")
            result = cursor.fetchone()
            if result:
                print("La base de datos 'sistema_informacion_medica' ya existe.")
                cursor.close()
                self.connection.close()
                return 0

            cursor.execute("CREATE DATABASE sistema_informacion_medica")
            cursor.execute("USE sistema_informacion_medica")

            # Crear tablas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Hospital (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    direccion VARCHAR(255) NOT NULL,
                    telefono VARCHAR(20) NOT NULL,
                    tipo VARCHAR(50) NOT NULL,
                    zona VARCHAR(50) NOT NULL
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Medico (
                    cedula VARCHAR(20) PRIMARY KEY,
                    nombres VARCHAR(255) NOT NULL,
                    apellidos VARCHAR(255) NOT NULL,
                    fecha_nacimiento DATE NOT NULL,
                    telefono VARCHAR(20) NOT NULL,
                    direccion VARCHAR(255) NOT NULL,
                    genero ENUM('Masculino', 'Femenino') NOT NULL,
                    estado_civil ENUM('Soltero', 'Casado', 'Viudo', 'Divorciado') NOT NULL,
                    numero_registro_medico VARCHAR(50) NOT NULL,
                    horario_guardia TEXT NOT NULL
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Paciente (
                    cedula VARCHAR(20) PRIMARY KEY,
                    nombres VARCHAR(255) NOT NULL,
                    apellidos VARCHAR(255) NOT NULL,
                    fecha_nacimiento DATE NOT NULL,
                    lugar_nacimiento VARCHAR(255) NOT NULL,
                    genero ENUM('Masculino', 'Femenino') NOT NULL,
                    estado_civil ENUM('Soltero', 'Casado', 'Viudo', 'Divorciado') NOT NULL,
                    direccion VARCHAR(255) NOT NULL,
                    nacionalidad VARCHAR(50) NOT NULL,
                    profesion_ocupacion VARCHAR(100) NOT NULL,
                    religion VARCHAR(50) NOT NULL,
                    contacto_emergencia VARCHAR(255) NOT NULL,
                    parentesco VARCHAR(50) NOT NULL,
                    motivo_consulta TEXT NOT NULL,
                    enfermedad_actual TEXT NOT NULL,
                    diagnostico_admision TEXT NOT NULL,
                    intervencion_tratamiento TEXT NOT NULL,
                    diagnostico_final TEXT NOT NULL,
                    estado_actual ENUM('Mejora', 'Muerte') NOT NULL,
                    fecha_alta DATE,
                    hora_alta TIME
                ) ENGINE=InnoDB
            ''')

            self.connection.commit()
            cursor.close()
            self.connection.close()
            print("Base de datos creada exitosamente.")
            return 0
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de acceso: nombre de usuario o contraseña incorrectos.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe.")
            else:
                print(err)
            return 1

if __name__ == "__main__":
    creador = CrearBaseDatos()
    exit(creador.crear_base_datos())