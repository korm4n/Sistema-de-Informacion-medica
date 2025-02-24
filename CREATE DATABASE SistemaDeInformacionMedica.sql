delete DATABASE SistemadeInformacionMedica

CREATE DATABASE SistemaInformacionMedica
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;

USE SistemaInformacionMedica;

CREATE TABLE Hospital (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    zona VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE Medico (
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
) ENGINE=InnoDB;

CREATE TABLE Paciente (
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
) ENGINE=InnoDB;