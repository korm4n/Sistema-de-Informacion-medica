from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDateEdit, QListWidget, QMessageBox, QFormLayout, QMenuBar, QToolBar, QSizePolicy, QSpacerItem, QFrame
from PyQt5.QtGui import QIntValidator, QRegExpValidator, QIcon
from PyQt5.QtCore import QDate, QRegExp, Qt, QSize
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SISTEMA DE INFORMACION MEDICA")
        self.setGeometry(100, 100, 1200, 780)
        self.setWindowIcon(QIcon("C:/Users/kervinfb/OneDrive/Documents/base de datos hospitalaria/iconos/simv.png"))  # Cambiar la imagen de la ventana

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()
        content_layout = QHBoxLayout()

        # Create toolbar for date display
        self.toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.date_label = QLabel(f"Fecha: {datetime.now().strftime('%d-%m-%Y')}")
        self.date_label.setStyleSheet("font-size: 18px;")
        self.toolbar.setMovable(False)

        # Align date label to the right
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.toolbar.addWidget(spacer)
        self.toolbar.addWidget(self.date_label)

        # Left side buttons
        button_layout = QVBoxLayout()
        self.buttons = {
            "Inicio": QPushButton("Inicio"),
            "Medicos": QPushButton("Médicos"),
            "Paciente": QPushButton("Paciente"),
            "HistoriaMedica": QPushButton("Historia Médica"),
            "Consultas": QPushButton("Consultas"),
            "Farmacia": QPushButton("Farmacia"),
            "Configuracion": QPushButton("Configuración")
        }

        # Set icons for buttons
        self.buttons["Inicio"].setIcon(QIcon("C:/Users/kervinfb/OneDrive/Documents/base de datos hospitalaria/iconos/inicio.png"))
        self.buttons["Medicos"].setIcon(QIcon("C:/Users/kervinfb/OneDrive/Documents/base de datos hospitalaria/iconos/medicos.png"))
        self.buttons["Paciente"].setIcon(QIcon("C:/Users/kervinfb/OneDrive/Documents/base de datos hospitalaria/iconos/paciente.png"))
        self.buttons["HistoriaMedica"].setIcon(QIcon("C:/Users/kervinfb/OneDrive/Documents/base de datos hospitalaria/iconos/historial.png"))
        self.buttons["Consultas"].setIcon(QIcon("C:/Users/kervinfb/OneDrive/Documents/base de datos hospitalaria/iconos/consultas.png"))
        self.buttons["Farmacia"].setIcon(QIcon("C:/Users/kervinfb/OneDrive/Documents/base de datos hospitalaria/iconos/farmacia.png"))
        self.buttons["Configuracion"].setIcon(QIcon("C:/Users/kervinfb/OneDrive/Documents/base de datos hospitalaria/iconos/config.png"))

        # Apply styles to buttons
        button_style = """
            QPushButton {
                text-align: left;
                padding: 15px;
                font-size: 24px;  /* Tamaño de fuente más grande */
                color: blue;
                border-radius: 15px;  /* Esquinas redondeadas */
                background-color: #f0f0f0;  /* Color de fondo */
            }
            QPushButton::icon {
                width: 64px;  /* Ancho del icono */
                height: 64px;  /* Altura del icono */
            }
            QPushButton:hover {
                background-color:rgb(20, 19, 19);  /* Color de fondo al pasar el mouse */
                color: white;  /* Color del texto al pasar el mouse */
            }
        """

        for key, button in self.buttons.items():
            button.setIconSize(QSize(64, 64))  # Establecer tamaño del icono
            button.setFixedSize(300, 100)  # Establecer tamaño fijo para los botones
            button.setStyleSheet(button_style)
            button.clicked.connect(lambda checked, key=key: self.show_frame(key))
            button_layout.addWidget(button)

        # Create a frame for buttons with black background
        button_frame = QFrame()
        button_frame.setStyleSheet("background-color: black;")
        button_frame.setLayout(button_layout)

        content_layout.addWidget(button_frame)

        # Add a vertical line separator
        separator = QFrame()
        separator.setFrameShape(QFrame.VLine)
        separator.setFrameShadow(QFrame.Sunken)
        content_layout.addWidget(separator)

        # Right side frames
        self.frames = {
            "Inicio": self.create_inicio_frame(),
            "Medicos": self.create_medicos_frame(),
            "Paciente": self.create_paciente_frame(),
            "HistoriaMedica": self.create_historia_medica_frame(),
            "Consultas": self.create_consultas_frame(),
            "Farmacia": self.create_farmacia_frame(),
            "Configuracion": self.create_configuracion_frame()
        }

        self.stacked_widget = QWidget()
        self.stacked_layout = QVBoxLayout(self.stacked_widget)
        for frame in self.frames.values():
            self.stacked_layout.addWidget(frame)
        content_layout.addWidget(self.stacked_widget)

        main_layout.addLayout(content_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.show_frame("Inicio")

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.hide()
        self.frames[frame_name].show()

    def create_inicio_frame(self):
        frame = QWidget()
        layout = QVBoxLayout(frame)
        layout.setAlignment(Qt.AlignTop)

        # Hospital name label
        hospital_name_layout = QHBoxLayout()
        hospital_name_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.hospital_name_label_inicio = QLabel("Ambulatorio Rural Tipo III Carmen Isidra Bracho")
        self.hospital_name_label_inicio.setStyleSheet("font-size: 40px; color: Blue;")
        hospital_name_layout.addWidget(self.hospital_name_label_inicio)
        hospital_name_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(hospital_name_layout)

        layout.addWidget(QLabel("Médicos de Guardia:"))
        layout.addWidget(QLabel("Dr. Juan Pérez - Cardiología"))
        layout.addWidget(QLabel("Dra. Ana Gómez - Pediatría"))
        return frame

    def create_medicos_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        self.cedula_entry_medico = QLineEdit()
        layout.addRow(QLabel("Cédula:"), self.cedula_entry_medico)
        self.cedula_entry_medico.setValidator(QIntValidator())
        self.nombres_entry_medico = QLineEdit()
        layout.addRow(QLabel("Nombres:"), self.nombres_entry_medico)
        self.nombres_entry_medico.setValidator(QRegExpValidator(QRegExp("[A-Za-z ]+")))
        self.apellidos_entry_medico = QLineEdit()
        layout.addRow(QLabel("Apellidos:"), self.apellidos_entry_medico)
        self.apellidos_entry_medico.setValidator(QRegExpValidator(QRegExp("[A-Za-z ]+")))
        self.birthdate_entry_medico = QDateEdit()
        layout.addRow(QLabel("Fecha de Nacimiento:"), self.birthdate_entry_medico)
        self.birthdate_entry_medico.setCalendarPopup(True)
        self.birthdate_entry_medico.dateChanged.connect(self.update_age_medico)  # Conectar la señal dateChanged
        self.age_label_medico = QLabel("")
        layout.addRow(QLabel("Edad:"), self.age_label_medico)
        self.genero_combobox_medico = QComboBox()
        layout.addRow(QLabel("Género:"), self.genero_combobox_medico)
        self.genero_combobox_medico.addItems(["Masculino", "Femenino"])
        self.especialidad_entry_medico = QLineEdit()
        layout.addRow(QLabel("Especialidad:"), self.especialidad_entry_medico)
        self.save_button_medico = QPushButton("Guardar")
        self.save_button_medico.clicked.connect(self.save_medico)
        layout.addRow(self.save_button_medico)
        self.clear_button_medico = QPushButton("Limpiar Información")
        self.clear_button_medico.clicked.connect(self.clear_medico_form)
        layout.addRow(self.clear_button_medico)
        frame.setLayout(layout)
        return frame

    def update_age_medico(self):
        birthdate = self.birthdate_entry_medico.date().toPyDate()
        age = calculate_age(birthdate)
        self.age_label_medico.setText(str(age))

    def save_medico(self):
        cedula = self.cedula_entry_medico.text()
        nombres = self.nombres_entry_medico.text()
        apellidos = self.apellidos_entry_medico.text()
        birthdate = self.birthdate_entry_medico.date().toPyDate()
        genero = self.genero_combobox_medico.currentText()
        especialidad = self.especialidad_entry_medico.text()
        age = self.age_label_medico.text()

        if not cedula or not nombres or not apellidos or not especialidad:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Aquí puedes agregar la lógica para guardar los datos en la base de datos
        QMessageBox.information(self, "Guardado", "Datos del médico guardados correctamente.")

    def clear_medico_form(self):
        self.cedula_entry_medico.clear()
        self.nombres_entry_medico.clear()
        self.apellidos_entry_medico.clear()
        self.birthdate_entry_medico.setDate(QDate.currentDate())
        self.age_label_medico.clear()
        self.genero_combobox_medico.setCurrentIndex(0)
        self.especialidad_entry_medico.clear()

    def create_paciente_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        self.cedula_entry_paciente = QLineEdit()
        layout.addRow(QLabel("Cédula:"), self.cedula_entry_paciente)
        self.cedula_entry_paciente.setValidator(QIntValidator())
        self.nombres_entry_paciente = QLineEdit()
        layout.addRow(QLabel("Nombres:"), self.nombres_entry_paciente)
        self.nombres_entry_paciente.setValidator(QRegExpValidator(QRegExp("[A-Za-z ]+")))
        self.apellidos_entry_paciente = QLineEdit()
        layout.addRow(QLabel("Apellidos:"), self.apellidos_entry_paciente)
        self.apellidos_entry_paciente.setValidator(QRegExpValidator(QRegExp("[A-Za-z ]+")))
        self.birthdate_entry_paciente = QDateEdit()
        layout.addRow(QLabel("Fecha de Nacimiento:"), self.birthdate_entry_paciente)
        self.birthdate_entry_paciente.setCalendarPopup(True)
        self.birthdate_entry_paciente.dateChanged.connect(self.update_age_paciente)  # Conectar la señal dateChanged
        self.age_label_paciente = QLabel("")
        layout.addRow(QLabel("Edad:"), self.age_label_paciente)
        self.genero_combobox_paciente = QComboBox()
        layout.addRow(QLabel("Género:"), self.genero_combobox_paciente)
        self.genero_combobox_paciente.addItems(["Masculino", "Femenino"])
        self.genero_combobox_paciente.currentTextChanged.connect(self.toggle_embarazo_fields)  # Conectar la señal currentTextChanged
        self.estado_civil_combobox_paciente = QComboBox()
        layout.addRow(QLabel("Estado Civil:"), self.estado_civil_combobox_paciente)
        self.estado_civil_combobox_paciente.addItems(["Soltero", "Casado", "Divorciado", "Viudo"])
        self.lugar_nacimiento_entry_paciente = QLineEdit()
        layout.addRow(QLabel("Lugar de Nacimiento:"), self.lugar_nacimiento_entry_paciente)
        self.direccion_entry_paciente = QLineEdit()
        layout.addRow(QLabel("Dirección de Habitación:"), self.direccion_entry_paciente)
        self.diagnostico_entry_paciente = QLineEdit()
        layout.addRow(QLabel("Diagnóstico:"), self.diagnostico_entry_paciente)
        
        # Embarazo fields
        self.embarazada_combobox_paciente = QComboBox()
        self.embarazada_combobox_paciente.addItems(["No", "Sí"])
        self.embarazada_combobox_paciente.currentTextChanged.connect(self.toggle_semanas_field)
        layout.addRow(QLabel("¿Está embarazada?"), self.embarazada_combobox_paciente)
        self.semanas_entry_paciente = QLineEdit()
        self.semanas_entry_paciente.setValidator(QIntValidator())
        layout.addRow(QLabel("Cantidad de semanas:"), self.semanas_entry_paciente)
        self.semanas_entry_paciente.setVisible(False)  # Ocultar por defecto

        self.save_button_paciente = QPushButton("Guardar")
        self.save_button_paciente.clicked.connect(self.save_paciente)
        layout.addRow(self.save_button_paciente)
        self.clear_button_paciente = QPushButton("Limpiar Información")
        self.clear_button_paciente.clicked.connect(self.clear_paciente_form)
        layout.addRow(self.clear_button_paciente)
        frame.setLayout(layout)
        return frame

    def toggle_embarazo_fields(self):
        if self.genero_combobox_paciente.currentText() == "Femenino":
            self.embarazada_combobox_paciente.setVisible(True)
        else:
            self.embarazada_combobox_paciente.setVisible(False)
            self.semanas_entry_paciente.setVisible(False)

    def toggle_semanas_field(self):
        if self.embarazada_combobox_paciente.currentText() == "Sí":
            self.semanas_entry_paciente.setVisible(True)
        else:
            self.semanas_entry_paciente.setVisible(False)

    def update_age_paciente(self):
        birthdate = self.birthdate_entry_paciente.date().toPyDate()
        age = calculate_age(birthdate)
        self.age_label_paciente.setText(str(age))

    def save_paciente(self):
        cedula = self.cedula_entry_paciente.text()
        nombres = self.nombres_entry_paciente.text()
        apellidos = self.apellidos_entry_paciente.text()
        birthdate = self.birthdate_entry_paciente.date().toPyDate()
        genero = self.genero_combobox_paciente.currentText()
        estado_civil = self.estado_civil_combobox_paciente.currentText()
        lugar_nacimiento = self.lugar_nacimiento_entry_paciente.text()
        direccion = self.direccion_entry_paciente.text()
        diagnostico = self.diagnostico_entry_paciente.text()
        age = self.age_label_paciente.text()
        embarazada = self.embarazada_combobox_paciente.currentText()
        semanas = self.semanas_entry_paciente.text() if embarazada == "Sí" else ""

        if not cedula or not nombres or not apellidos or not lugar_nacimiento or not direccion or not diagnostico:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Aquí puedes agregar la lógica para guardar los datos en la base de datos
        QMessageBox.information(self, "Guardado", "Datos del paciente guardados correctamente.")

    def clear_paciente_form(self):
        self.cedula_entry_paciente.clear()
        self.nombres_entry_paciente.clear()
        self.apellidos_entry_paciente.clear()
        self.birthdate_entry_paciente.setDate(QDate.currentDate())
        self.age_label_paciente.clear()
        self.genero_combobox_paciente.setCurrentIndex(0)
        self.estado_civil_combobox_paciente.setCurrentIndex(0)
        self.lugar_nacimiento_entry_paciente.clear()
        self.direccion_entry_paciente.clear()
        self.diagnostico_entry_paciente.clear()
        self.embarazada_combobox_paciente.setCurrentIndex(0)
        self.semanas_entry_paciente.clear()
        self.semanas_entry_paciente.setVisible(False)

    def create_historia_medica_frame(self):
        frame = QWidget()
        layout = QVBoxLayout(frame)
        layout.addWidget(QLabel("Historia Médica del Paciente"))
        self.paciente_list = QListWidget()
        layout.addWidget(self.paciente_list)
        frame.setLayout(layout)
        return frame
  
    def create_consultas_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)

        # Sexo
        self.sexo_combobox_consultas = QComboBox()
        self.sexo_combobox_consultas.addItems(["Masculino", "Femenino"])
        layout.addRow(QLabel("Sexo:"), self.sexo_combobox_consultas)

        # Edad
        self.edad_entry_consultas = QLineEdit()
        self.edad_entry_consultas.setValidator(QIntValidator())
        layout.addRow(QLabel("Edad:"), self.edad_entry_consultas)

        # Dirección
        self.direccion_entry_consultas = QLineEdit()
        layout.addRow(QLabel("Dirección:"), self.direccion_entry_consultas)

        # Tipo de Enfermedad
        self.tipo_enfermedad_entry_consultas = QLineEdit()
        layout.addRow(QLabel("Tipo de Enfermedad:"), self.tipo_enfermedad_entry_consultas)

        # Embarazadas
        self.embarazadas_combobox_consultas = QComboBox()
        self.embarazadas_combobox_consultas.addItems(["Sí", "No"])
        layout.addRow(QLabel("Embarazadas:"), self.embarazadas_combobox_consultas)

        # Botón de búsqueda
        self.search_button_consultas = QPushButton("Buscar")
        self.search_button_consultas.clicked.connect(self.search_consultas)
        layout.addRow(self.search_button_consultas)

        # Lista de resultados
        self.consultas_list = QListWidget()
        layout.addRow(QLabel("Resultados de Consultas:"), self.consultas_list)

        frame.setLayout(layout)
        return frame

    def search_consultas(self):
        sexo = self.sexo_combobox_consultas.currentText()
        edad = self.edad_entry_consultas.text()
        direccion = self.direccion_entry_consultas.text()
        tipo_enfermedad = self.tipo_enfermedad_entry_consultas.text()
        embarazadas = self.embarazadas_combobox_consultas.currentText()

        # Aquí puedes agregar la lógica para realizar la búsqueda en la base de datos
        # y actualizar la lista de resultados (self.consultas_list)

        # Ejemplo de actualización de la lista de resultados
        self.consultas_list.clear()

        # Filtrar resultados según los criterios especificados
        results = self.filter_consultas(sexo, edad, direccion, tipo_enfermedad, embarazadas)
        for result in results:
            self.consultas_list.addItem(result)

    def filter_consultas(self, sexo, edad, direccion, tipo_enfermedad, embarazadas):
        # Aquí puedes agregar la lógica para filtrar los resultados de la base de datos
        # Este es un ejemplo de cómo podrías hacerlo con datos ficticios
        all_consultas = [
            {"sexo": "Masculino", "edad": "30", "direccion": "Calle 1", "tipo_enfermedad": "Gripe", "embarazadas": "No"},
            {"sexo": "Femenino", "edad": "25", "direccion": "Calle 2", "tipo_enfermedad": "Covid-19", "embarazadas": "Sí"},
            # Agrega más datos ficticios aquí
        ]

        filtered_consultas = []
        for consulta in all_consultas:
            if (sexo == consulta["sexo"] or not sexo) and \
               (edad == consulta["edad"] or not edad) and \
               (direccion in consulta["direccion"] or not direccion) and \
               (tipo_enfermedad in consulta["tipo_enfermedad"] or not tipo_enfermedad) and \
               (embarazadas == consulta["embarazadas"] or not embarazadas):
                filtered_consultas.append(f"Sexo: {consulta['sexo']}, Edad: {consulta['edad']}, Dirección: {consulta['direccion']}, Tipo de Enfermedad: {consulta['tipo_enfermedad']}, Embarazadas: {consulta['embarazadas']}")

        return filtered_consultas

    def create_farmacia_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        self.nombre_farmaco_entry = QLineEdit()
        layout.addRow(QLabel("Nombre del Fármaco:"), self.nombre_farmaco_entry)
        self.fecha_elaboracion_entry = QDateEdit()
        layout.addRow(QLabel("Fecha de Elaboración:"), self.fecha_elaboracion_entry)
        self.fecha_elaboracion_entry.setCalendarPopup(True)
        self.lote_entry = QLineEdit()
        layout.addRow(QLabel("Lote del Medicamento:"), self.lote_entry)
        self.fecha_caducidad_entry = QDateEdit()
        layout.addRow(QLabel("Fecha de Caducidad:"), self.fecha_caducidad_entry)
        self.fecha_caducidad_entry.setCalendarPopup(True)
        self.cantidades_recibidas_entry = QLineEdit()
        layout.addRow(QLabel("Cantidades Recibidas:"), self.cantidades_recibidas_entry)
        self.cantidades_disponibles_entry = QLineEdit()
        layout.addRow(QLabel("Cantidades Disponibles:"), self.cantidades_disponibles_entry)
        self.save_button_farmacia = QPushButton("Guardar")
        self.save_button_farmacia.clicked.connect(self.save_farmacia)
        layout.addRow(self.save_button_farmacia)
        self.clear_button_farmacia = QPushButton("Limpiar Información")
        self.clear_button_farmacia.clicked.connect(self.clear_farmacia_form)
        layout.addRow(self.clear_button_farmacia)
        frame.setLayout(layout)
        return frame

    def save_farmacia(self):
        nombre_farmaco = self.nombre_farmaco_entry.text()
        fecha_elaboracion = self.fecha_elaboracion_entry.date().toPyDate()
        lote = self.lote_entry.text()
        fecha_caducidad = self.fecha_caducidad_entry.date().toPyDate()
        cantidades_recibidas = self.cantidades_recibidas_entry.text()
        cantidades_disponibles = self.cantidades_disponibles_entry.text()

        if not nombre_farmaco or not lote or not cantidades_recibidas or not cantidades_disponibles:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Aquí puedes agregar la lógica para guardar los datos en la base de datos
        QMessageBox.information(self, "Guardado", "Datos del fármaco guardados correctamente.")

    def clear_farmacia_form(self):
        self.nombre_farmaco_entry.clear()
        self.fecha_elaboracion_entry.setDate(QDate.currentDate())
        self.lote_entry.clear()
        self.fecha_caducidad_entry.setDate(QDate.currentDate())
        self.cantidades_recibidas_entry.clear()
        self.cantidades_disponibles_entry.clear()

    def create_configuracion_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        layout.addRow(QLabel("Configuración del Sistema"))
        self.hospital_name_entry = QLineEdit()
        layout.addRow(QLabel("Nombre del Hospital o Ambulatorio:"), self.hospital_name_entry)
        self.save_button_configuracion = QPushButton("Guardar")
        self.save_button_configuracion.clicked.connect(self.update_hospital_name)
        layout.addRow(self.save_button_configuracion)
        self.clear_button_configuracion = QPushButton("Limpiar Información")
        self.clear_button_configuracion.clicked.connect(self.clear_configuracion_form)
        layout.addRow(self.clear_button_configuracion)
        frame.setLayout(layout)
        return frame

    def update_hospital_name(self):
        self.hospital_name_label_inicio.setText(self.hospital_name_entry.text())

    def clear_configuracion_form(self):
        self.hospital_name_entry.clear()

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())