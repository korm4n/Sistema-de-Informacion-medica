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
                    zona ENUM('Rural', 'Urbana', 'Mixta') NOT NULL
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Medico (
                    cedula VARCHAR(20) PRIMARY KEY,
                    primer_nombre VARCHAR(255) NOT NULL,
                    segundo_nombre VARCHAR(255),
                    primer_apellido VARCHAR(255) NOT NULL,
                    segundo_apellido VARCHAR(255),
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
                    primer_nombre VARCHAR(255) NOT NULL,
                    segundo_nombre VARCHAR(255),
                    primer_apellido VARCHAR(255) NOT NULL,
                    segundo_apellido VARCHAR(255),
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

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS HistoriaClinicaAntecedentesPersonales (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    adenitis TEXT NOT NULL,
                    alergia TEXT NOT NULL,
                    amigdalitis TEXT NOT NULL,
                    artritis TEXT NOT NULL,
                    asma TEXT NOT NULL,
                    Bilharziasis TEXT NOT NULL,
                    blenorragia TEXT NOT NULL,
                    bronquitis TEXT NOT NULL,
                    buba TEXT NOT NULL,
                    catarros TEXT NOT NULL,
                    chagas TEXT NOT NULL,
                    chancros TEXT NOT NULL,
                    difteria TEXT NOT NULL,
                    diarreas TEXT NOT NULL,
                    hansen TEXT NOT NULL,
                    influenzas TEXT NOT NULL,
                    lechina TEXT NOT NULL,
                    necatoriasis TEXT NOT NULL,
                    neumonia TEXT NOT NULL,
                    otitis TEXT NOT NULL,
                    paludismo TEXT NOT NULL,
                    parasitos TEXT NOT NULL,
                    parotiditis TEXT NOT NULL,
                    pleuresía TEXT NOT NULL,
                    quirurgicos TEXT NOT NULL,
                    rinolangititis TEXT NOT NULL,
                    rubeola TEXT NOT NULL,
                    sarampion TEXT NOT NULL,
                    sifilis TEXT NOT NULL,
                    sindrome_disentericos TEXT NOT NULL,
                    tuberculosis TEXT NOT NULL,
                    tifoidea TEXT NOT NULL,
                    traumatismos TEXT NOT NULL,
                    vacunaciones TEXT NOT NULL,
                    otros TEXT NOT NULL
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS HistoriaClinicaAntecedentesFamiliares (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    alergia TEXT NOT NULL,
                    artritis TEXT NOT NULL,
                    cancer TEXT NOT NULL,
                    cardio_vasculares TEXT NOT NULL,
                    diabetes TEXT NOT NULL,
                    enf_digestivas TEXT NOT NULL,
                    enf_renales TEXT NOT NULL,
                    intoxicaciones TEXT NOT NULL,
                    neuromentales TEXT NOT NULL,
                    sifilis TEXT NOT NULL,
                    tuberculosis TEXT NOT NULL,
                    otros_2_12 TEXT NOT NULL,
                    alcohol TEXT NOT NULL,
                    chimo TEXT NOT NULL,
                    deportes TEXT NOT NULL,
                    drogas TEXT NOT NULL,
                    ocupacion TEXT NOT NULL,
                    problemas_familiares TEXT NOT NULL,
                    rasgos_personales TEXT NOT NULL,
                    sexuales TEXT NOT NULL,
                    siesta TEXT NOT NULL,
                    sueño TEXT NOT NULL,
                    tabaco TEXT NOT NULL,
                    otros_3_12 TEXT NOT NULL,
                    aumento_de_peso TEXT NOT NULL,
                    fiebre TEXT NOT NULL,
                    nutricion TEXT NOT NULL,
                    perdida_de_peso TEXT NOT NULL,
                    sudores_nocturnos TEXT NOT NULL,
                    temblores TEXT NOT NULL,
                    otros_4_7 TEXT NOT NULL,
                    cianosis TEXT NOT NULL,
                    edemas TEXT NOT NULL,
                    erupciones TEXT NOT NULL,
                    pigmentacion TEXT NOT NULL,
                    pruritos TEXT NOT NULL,
                    otros_5_6 TEXT NOT NULL,
                    caida_del_cabello TEXT NOT NULL,
                    cefalea TEXT NOT NULL,
                    mareos TEXT NOT NULL,
                    sincope TEXT NOT NULL,
                    traumas TEXT NOT NULL,
                    otros_6_6 TEXT NOT NULL,
                    amaurosis TEXT NOT NULL,
                    anteojos TEXT NOT NULL,
                    cansancio_ocular TEXT NOT NULL,
                    diplopia TEXT NOT NULL,
                    dolor TEXT NOT NULL,
                    fotofobia TEXT NOT NULL,
                    lagrimeo TEXT NOT NULL,
                    otros_7_5 TEXT NOT NULL
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS HistoriaClinicaAntecedentesFamiliares2 (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    dolor_de_oidos TEXT NOT NULL,
                    secreciones TEXT NOT NULL,
                    sordera TEXT NOT NULL,
                    tinnitus TEXT NOT NULL,
                    vertigo TEXT NOT NULL,
                    otros_8_7 TEXT NOT NULL,
                    catarros TEXT NOT NULL,
                    epistaxis TEXT NOT NULL,
                    obstruciones TEXT NOT NULL,
                    secrecion_nasal TEXT NOT NULL,
                    sinusitis TEXT NOT NULL,
                    otros_9_6 TEXT NOT NULL,
                    dientes TEXT NOT NULL,
                    halitosis TEXT NOT NULL,
                    mucosas TEXT NOT NULL,
                    otros_10_4 TEXT NOT NULL,
                    disfagia TEXT NOT NULL,
                    dolor_de_garganta TEXT NOT NULL,
                    ronquera TEXT NOT NULL,
                    otros_11_4 TEXT NOT NULL,
                    disnea_respiratoria TEXT NOT NULL,
                    dolor_en_el_pecho TEXT NOT NULL,
                    esputos TEXT NOT NULL,
                    hemoptisis TEXT NOT NULL,
                    tos TEXT NOT NULL,
                    otros_12_6 TEXT NOT NULL,
                    artralgias TEXT NOT NULL,
                    debilidad TEXT NOT NULL,
                    dolores_oseos TEXT NOT NULL,
                    deformidades TEXT NOT NULL,
                    otros_13_5 TEXT NOT NULL,
                    angustias TEXT NOT NULL,
                    disnea_cardiovascular TEXT NOT NULL,
                    dolor_cardiovascular TEXT NOT NULL,
                    palpitaciones TEXT NOT NULL,
                    taquicardia TEXT NOT NULL,
                    vertigos TEXT NOT NULL,
                    claudicacion TEXT NOT NULL,
                    trastornos_parestesicos TEXT NOT NULL,
                    varicosidades TEXT NOT NULL,
                    otros_14_10 TEXT NOT NULL,
                    apetito TEXT NOT NULL,
                    constipacion TEXT NOT NULL,
                    diarrea TEXT NOT NULL,
                    dolor_gastroinstestinal TEXT NOT NULL,
                    heces_tipo_color_mucosidad_sangre TEXT NOT NULL,
                    eruptos TEXT NOT NULL,
                    flatulencias TEXT NOT NULL,
                    hemorroides TEXT NOT NULL,
                    hernias TEXT NOT NULL,
                    malestar TEXT NOT NULL,
                    nauseas TEXT NOT NULL,
                    parasitos TEXT NOT NULL,
                    pirosis TEXT NOT NULL,
                    vomitos TEXT NOT NULL,
                    otros_15_15 TEXT NOT NULL
                ) ENGINE=InnoDB
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS HistoriaClinicaAntecedentesFamiliares3 (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    dolor_genitourinario TEXT NOT NULL,
                    enuresis TEXT NOT NULL,
                    hematuria TEXT NOT NULL,
                    incontinencia TEXT NOT NULL,
                    micciones TEXT NOT NULL,
                    nicturia TEXT NOT NULL,
                    piuria TEXT NOT NULL,
                    secreciones TEXT NOT NULL,
                    ulceras TEXT NOT NULL,
                    otros_16_10 TEXT NOT NULL,
                    menarquia TEXT NOT NULL,
                    abortos TEXT NOT NULL,
                    partos TEXT NOT NULL,
                    dispareunia TEXT NOT NULL,
                    frigidez TEXT NOT NULL,
                    menopausia TEXT NOT NULL,
                    regla_tipo_cantidad_dolor_ultimaregla TEXT NOT NULL,
                    flujo TEXT NOT NULL,
                    otros_17_9 TEXT NOT NULL,
                    convulsiones TEXT NOT NULL,
                    estatica TEXT NOT NULL,
                    estado_emocional TEXT NOT NULL,
                    marcha TEXT NOT NULL,
                    paralisis TEXT NOT NULL,
                    temblor TEXT NOT NULL,
                    tics TEXT NOT NULL,
                    tipo_de_personalidad TEXT NOT NULL,
                    otros_18_9 TEXT NOT NULL,
                    tipo_de_vivienda TEXT NOT NULL,
                    techo_piso TEXT NOT NULL,
                    cuartos TEXT NOT NULL,
                    baños TEXT NOT NULL,
                    n_de_personas TEXT NOT NULL,
                    animales TEXT NOT NULL,
                    roedores TEXT NOT NULL,
                    servicios_publicos TEXT NOT NULL,
                    otros_19_9 TEXT NOT NULL
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