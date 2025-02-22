from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDateEdit, QListWidget, QMessageBox, QFormLayout, QMenuBar, QToolBar, QSizePolicy, QSpacerItem, QFrame, QColorDialog, QCheckBox, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QFileDialog, QTimeEdit, QTextEdit
from PyQt5.QtGui import QIntValidator, QRegExpValidator, QIcon, QPixmap
from PyQt5.QtCore import QDate, QRegExp, Qt, QSize, QTime
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SISTEMA DE INFORMACION MEDICA")
        self.setGeometry(100, 100, 1580, 780)
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
            button.setFixedHeight(100)  # Establecer altura fija para los botones
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Permitir que el ancho se ajuste al contenido
            button.setStyleSheet(button_style)
            button.clicked.connect(lambda checked, key=key: self.show_frame(key))
            button_layout.addWidget(button)

        # Create a frame for buttons with black background
        self.button_frame = QFrame()
        self.button_frame.setStyleSheet("background-color: black;")
        self.button_frame.setLayout(button_layout)

        content_layout.addWidget(self.button_frame)

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
        container.setStyleSheet("background-color: #C0C0C0;")  # Establecer fondo gris plateado
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
        layout.addWidget(QLabel("Dr. Juan Pérez - Cardiología (08:00 - 16:00)"))
        layout.addWidget(QLabel("Dra. Ana Gómez - Pediatría (16:00 - 00:00)"))
        layout.addWidget(QLabel("Dr. Luis Martínez - Neurología (00:00 - 08:00)"))

        # Image label
        self.image_label_inicio = QLabel()
        self.image_label_inicio.setFixedSize(400, 300)
        self.image_label_inicio.setStyleSheet("border: none;")
        self.image_label_inicio.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label_inicio)

        return frame

    def create_medicos_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        
        # Agrupar cédula, nombres, apellidos, fecha de nacimiento y edad en una fila
        row_layout1 = QHBoxLayout()
        row_layout1.setContentsMargins(0, 0, 0, 0)  # Ajustar márgenes
        self.cedula_entry_medico = QLineEdit()
        self.cedula_entry_medico.setValidator(QIntValidator(0, 99999999))
        self.cedula_entry_medico.setMaxLength(8)
        self.cedula_entry_medico.setFixedWidth(100)
        self.cedula_entry_medico.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Cédula:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.cedula_entry_medico)
        
        self.nombres_entry_medico = QLineEdit()
        self.nombres_entry_medico.setValidator(QRegExpValidator(QRegExp("[A-Za-z ]{1,50}")))
        self.nombres_entry_medico.setMaxLength(50)
        self.nombres_entry_medico.setFixedWidth(300)
        self.nombres_entry_medico.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Nombres:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.nombres_entry_medico)
        
        self.apellidos_entry_medico = QLineEdit()
        self.apellidos_entry_medico.setValidator(QRegExpValidator(QRegExp("[A-Za-z ]{1,50}")))
        self.apellidos_entry_medico.setMaxLength(50)
        self.apellidos_entry_medico.setFixedWidth(300)
        self.apellidos_entry_medico.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Apellidos:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.apellidos_entry_medico)
        
        self.birthdate_entry_medico = QDateEdit()
        self.birthdate_entry_medico.setCalendarPopup(True)
        self.birthdate_entry_medico.setFixedWidth(120)
        self.birthdate_entry_medico.setStyleSheet("background-color: white;")
        self.birthdate_entry_medico.dateChanged.connect(self.update_age_medico)
        row_layout1.addWidget(QLabel("Fecha de Nacimiento:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.birthdate_entry_medico)
        
        self.age_label_medico = QLabel("")
        self.age_label_medico.setFixedWidth(50)
        row_layout1.addWidget(QLabel("Edad:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.age_label_medico)
        
        layout.addRow(row_layout1)
        
        # Agrupar teléfono, género, estado civil y lugar de nacimiento en una fila (Médicos)
        row_layout2 = QHBoxLayout()
        self.telefono_entry_medico = QLineEdit()
        self.telefono_entry_medico.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_entry_medico.setMaxLength(15)
        self.telefono_entry_medico.setFixedWidth(150)
        self.telefono_entry_medico.setStyleSheet("background-color: white;")
        self.telefono_entry_medico.setCursorPosition(0)  # Posicionar el cursor al inicio
        row_layout2.addWidget(QLabel("Teléfono:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.telefono_entry_medico)

        self.genero_combobox_medico = QComboBox()
        self.genero_combobox_medico.addItems(["Masculino", "Femenino"])
        self.genero_combobox_medico.setFixedWidth(100)
        self.genero_combobox_medico.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Género:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.genero_combobox_medico)

        self.estado_civil_combobox_medico = QComboBox()
        self.estado_civil_combobox_medico.addItems(["Soltero", "Casado", "Viudo", "Divorciado"])
        self.estado_civil_combobox_medico.setFixedWidth(100)
        self.estado_civil_combobox_medico.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Estado Civil:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.estado_civil_combobox_medico)

        self.lugar_nacimiento_entry_medico = QLineEdit()
        self.lugar_nacimiento_entry_medico.setValidator(QRegExpValidator(QRegExp("[A-Za-z ]{1,50}")))
        self.lugar_nacimiento_entry_medico.setMaxLength(50)
        self.lugar_nacimiento_entry_medico.setFixedWidth(300)
        self.lugar_nacimiento_entry_medico.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Lugar de Nacimiento:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.lugar_nacimiento_entry_medico)

        layout.addRow(row_layout2)
        
        # Agrupar dirección y número de registro médico en una fila
        row_layout3 = QHBoxLayout()
        self.direccion_entry_medico = QLineEdit()
        self.direccion_entry_medico.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.direccion_entry_medico.setMaxLength(500)
        self.direccion_entry_medico.setFixedWidth(500)
        self.direccion_entry_medico.setStyleSheet("background-color: white;")
        row_layout3.addWidget(QLabel("Dirección:"))
        row_layout3.addWidget(self.direccion_entry_medico)
        
        self.numero_registro_medico_entry = QLineEdit()
        self.numero_registro_medico_entry.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.numero_registro_medico_entry.setMaxLength(500)
        self.numero_registro_medico_entry.setFixedWidth(500)
        self.numero_registro_medico_entry.setStyleSheet("background-color: white;")
        row_layout3.addWidget(QLabel("Número de Registro Médico:"))
        row_layout3.addWidget(self.numero_registro_medico_entry)
        
        layout.addRow(row_layout3)
        
        self.horario_guardia_entry = QLineEdit()
        self.horario_guardia_entry.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.horario_guardia_entry.setMaxLength(500)
        self.horario_guardia_entry.setFixedWidth(400)
        self.horario_guardia_entry.setStyleSheet("background-color: white;")
        layout.addRow(QLabel("Horario de Guardia:"), self.horario_guardia_entry)
        
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
        estado_civil = self.estado_civil_combobox_medico.currentText()
        numero_registro_medico = self.numero_registro_medico_entry.text()
        horario_guardia = self.horario_guardia_entry.text()

        if not cedula or not nombres or not apellidos or not numero_registro_medico or not horario_guardia:
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
        self.estado_civil_combobox_medico.setCurrentIndex(0)
        self.numero_registro_medico_entry.clear()
        self.horario_guardia_entry.clear()

    def create_paciente_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        
        # Agrupar cédula, nombres, apellidos, fecha de nacimiento y edad en una fila
        row_layout1 = QHBoxLayout()
        row_layout1.setContentsMargins(0, 0, 0, 0)  # Ajustar márgenes
        self.cedula_entry_paciente = QLineEdit()
        self.cedula_entry_paciente.setValidator(QIntValidator(0, 99999999))
        self.cedula_entry_paciente.setMaxLength(8)
        self.cedula_entry_paciente.setFixedWidth(100)
        self.cedula_entry_paciente.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Cédula:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.cedula_entry_paciente)
        
        self.nombres_entry_paciente = QLineEdit()
        self.nombres_entry_paciente.setValidator(QRegExpValidator(QRegExp("[A-Za-z ]{1,50}")))
        self.nombres_entry_paciente.setMaxLength(50)
        self.nombres_entry_paciente.setFixedWidth(300)
        self.nombres_entry_paciente.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Nombres:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.nombres_entry_paciente)
        
        self.apellidos_entry_paciente = QLineEdit()
        self.apellidos_entry_paciente.setValidator(QRegExpValidator(QRegExp("[A-Za-z ]{1,50}")))
        self.apellidos_entry_paciente.setMaxLength(50)
        self.apellidos_entry_paciente.setFixedWidth(300)
        self.apellidos_entry_paciente.setStyleSheet("background-color: white;")
        row_layout1.addWidget(QLabel("Apellidos:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.apellidos_entry_paciente)
        
        self.birthdate_entry_paciente = QDateEdit()
        self.birthdate_entry_paciente.setCalendarPopup(True)
        self.birthdate_entry_paciente.setFixedWidth(120)
        self.birthdate_entry_paciente.setStyleSheet("background-color: white;")
        self.birthdate_entry_paciente.dateChanged.connect(self.update_age_paciente)
        row_layout1.addWidget(QLabel("Fecha de Nacimiento:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.birthdate_entry_paciente)
        
        self.age_label_paciente = QLabel("")
        self.age_label_paciente.setFixedWidth(50)
        row_layout1.addWidget(QLabel("Edad:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout1.addWidget(self.age_label_paciente)
        
        layout.addRow(row_layout1)
        
        # Agrupar teléfono, género, estado civil y lugar de nacimiento en una fila (Pacientes)
        row_layout2 = QHBoxLayout()
        self.telefono_entry_paciente = QLineEdit()
        self.telefono_entry_paciente.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_entry_paciente.setMaxLength(12)
        self.telefono_entry_paciente.setFixedWidth(150)
        self.telefono_entry_paciente.setStyleSheet("background-color: white;")
        self.telefono_entry_paciente.setCursorPosition(0)  # Posicionar el cursor al inicio
        row_layout2.addWidget(QLabel("Teléfono:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.telefono_entry_paciente)

        self.genero_combobox_paciente = QComboBox()
        self.genero_combobox_paciente.addItems(["Masculino", "Femenino"])
        self.genero_combobox_paciente.setFixedWidth(100)
        self.genero_combobox_paciente.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Género:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.genero_combobox_paciente)

        self.estado_civil_combobox_paciente = QComboBox()
        self.estado_civil_combobox_paciente.addItems(["Soltero", "Casado", "Viudo", "Divorciado"])
        self.estado_civil_combobox_paciente.setFixedWidth(100)
        self.estado_civil_combobox_paciente.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Estado Civil:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.estado_civil_combobox_paciente)

        self.lugar_nacimiento_entry_paciente = QLineEdit()
        self.lugar_nacimiento_entry_paciente.setValidator(QRegExpValidator(QRegExp("[A-Za-z ]{1,50}")))
        self.lugar_nacimiento_entry_paciente.setMaxLength(50)
        self.lugar_nacimiento_entry_paciente.setFixedWidth(300)
        self.lugar_nacimiento_entry_paciente.setStyleSheet("background-color: white;")
        row_layout2.addWidget(QLabel("Lugar de Nacimiento:"))
        row_layout2.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout2.addWidget(self.lugar_nacimiento_entry_paciente)

        layout.addRow(row_layout2)
        
        # Agrupar dirección y otros campos en filas
        row_layout3 = QHBoxLayout()
        self.direccion_entry_paciente = QLineEdit()
        self.direccion_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.direccion_entry_paciente.setMaxLength(500)
        self.direccion_entry_paciente.setFixedWidth(400)
        self.direccion_entry_paciente.setStyleSheet("background-color: white;")
        row_layout3.addWidget(QLabel("Dirección:"))
        row_layout1.addSpacerItem(QSpacerItem(1, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        row_layout3.addWidget(self.direccion_entry_paciente)
        
        self.nacionalidad_entry_paciente = QLineEdit()
        self.nacionalidad_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.nacionalidad_entry_paciente.setMaxLength(500)
        self.nacionalidad_entry_paciente.setFixedWidth(400)
        self.nacionalidad_entry_paciente.setStyleSheet("background-color: white;")
        row_layout3.addWidget(QLabel("Nacionalidad:"))
        row_layout3.addWidget(self.nacionalidad_entry_paciente)
        
        layout.addRow(row_layout3)
        
        row_layout4 = QHBoxLayout()
        self.profesion_ocupacion_entry_paciente = QLineEdit()
        self.profesion_ocupacion_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.profesion_ocupacion_entry_paciente.setMaxLength(500)
        self.profesion_ocupacion_entry_paciente.setFixedWidth(400)
        self.profesion_ocupacion_entry_paciente.setStyleSheet("background-color: white;")
        row_layout4.addWidget(QLabel("Profesión/Ocupación:"))
        row_layout4.addWidget(self.profesion_ocupacion_entry_paciente)
        
        self.religion_entry_paciente = QLineEdit()
        self.religion_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.religion_entry_paciente.setMaxLength(500)
        self.religion_entry_paciente.setFixedWidth(400)
        self.religion_entry_paciente.setStyleSheet("background-color: white;")
        row_layout4.addWidget(QLabel("Religión:"))
        row_layout4.addWidget(self.religion_entry_paciente)
        
        layout.addRow(row_layout4)
        
        row_layout5 = QHBoxLayout()
        self.contacto_emergencia_entry_paciente = QLineEdit()
        self.contacto_emergencia_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,100}")))
        self.contacto_emergencia_entry_paciente.setMaxLength(500)
        self.contacto_emergencia_entry_paciente.setFixedWidth(300)
        self.contacto_emergencia_entry_paciente.setStyleSheet("background-color: white;")
        row_layout5.addWidget(QLabel("Contacto de Emergencia:"))
        row_layout5.addWidget(self.contacto_emergencia_entry_paciente)

        self.telefono_emergencia_entry_paciente = QLineEdit()
        self.telefono_emergencia_entry_paciente.setInputMask("0000-0000000")  # Máscara de entrada para el formato (0000-0000000)
        self.telefono_emergencia_entry_paciente.setMaxLength(12)
        self.telefono_emergencia_entry_paciente.setFixedWidth(120)
        self.telefono_emergencia_entry_paciente.setStyleSheet("background-color: white;")
        self.telefono_emergencia_entry_paciente.setCursorPosition(0)  # Posicionar el cursor al inicio
        row_layout5.addWidget(QLabel("Teléfono de Emergencia:"))
        row_layout5.addWidget(self.telefono_emergencia_entry_paciente)

        self.parentesco_entry_paciente = QLineEdit()
        self.parentesco_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.parentesco_entry_paciente.setMaxLength(500)
        self.parentesco_entry_paciente.setFixedWidth(400)
        self.parentesco_entry_paciente.setStyleSheet("background-color: white;")
        row_layout5.addWidget(QLabel("Parentesco:"))
        row_layout5.addWidget(self.parentesco_entry_paciente)

        layout.addRow(row_layout5)
        
        row_layout6 = QHBoxLayout()
        self.motivo_consulta_entry_paciente = QLineEdit()
        self.motivo_consulta_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.motivo_consulta_entry_paciente.setMaxLength(500)
        self.motivo_consulta_entry_paciente.setFixedWidth(400)
        self.motivo_consulta_entry_paciente.setStyleSheet("background-color: white;")
        row_layout6.addWidget(QLabel("Motivo de Consulta:"))
        row_layout6.addWidget(self.motivo_consulta_entry_paciente)
        
        self.enfermedad_actual_entry_paciente = QLineEdit()
        self.enfermedad_actual_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.enfermedad_actual_entry_paciente.setMaxLength(500)
        self.enfermedad_actual_entry_paciente.setFixedWidth(400)
        self.enfermedad_actual_entry_paciente.setStyleSheet("background-color: white;")
        row_layout6.addWidget(QLabel("Enfermedad Actual:"))
        row_layout6.addWidget(self.enfermedad_actual_entry_paciente)
        
        layout.addRow(row_layout6)
        
        row_layout7 = QHBoxLayout()
        self.diagnostico_admision_entry_paciente = QLineEdit()
        self.diagnostico_admision_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.diagnostico_admision_entry_paciente.setMaxLength(500)
        self.diagnostico_admision_entry_paciente.setFixedWidth(400)
        self.diagnostico_admision_entry_paciente.setStyleSheet("background-color: white;")
        row_layout7.addWidget(QLabel("Diagnóstico de Admisión:"))
        row_layout7.addWidget(self.diagnostico_admision_entry_paciente)
        
        self.intervencion_tratamiento_entry_paciente = QLineEdit()
        self.intervencion_tratamiento_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.intervencion_tratamiento_entry_paciente.setMaxLength(500)
        self.intervencion_tratamiento_entry_paciente.setFixedWidth(400)
        self.intervencion_tratamiento_entry_paciente.setStyleSheet("background-color: white;")
        row_layout7.addWidget(QLabel("Intervención/Tratamiento:"))
        row_layout7.addWidget(self.intervencion_tratamiento_entry_paciente)
        
        layout.addRow(row_layout7)
        
        row_layout8 = QHBoxLayout()
        self.diagnostico_final_entry_paciente = QLineEdit()
        self.diagnostico_final_entry_paciente.setValidator(QRegExpValidator(QRegExp(".{1,500}")))
        self.diagnostico_final_entry_paciente.setMaxLength(500)
        self.diagnostico_final_entry_paciente.setFixedWidth(400)
        self.diagnostico_final_entry_paciente.setStyleSheet("background-color: white;")
        row_layout8.addWidget(QLabel("Diagnóstico Final:"))
        row_layout8.addWidget(self.diagnostico_final_entry_paciente)

        layout.addRow(row_layout8)

        row_layout9 = QHBoxLayout()
        self.estado_actual_combobox_paciente = QComboBox()
        self.estado_actual_combobox_paciente.setStyleSheet("background-color: white;")
        self.estado_actual_combobox_paciente.addItems(["Mejora", "Muerte"])
        self.estado_actual_combobox_paciente.setFixedWidth(self.estado_actual_combobox_paciente.sizeHint().width())
        row_layout9.addWidget(QLabel("Estado Actual:"))
        row_layout9.addWidget(self.estado_actual_combobox_paciente)

        self.fecha_alta_entry_paciente = QDateEdit()
        self.fecha_alta_entry_paciente.setStyleSheet("background-color: white;")
        self.fecha_alta_entry_paciente.setCalendarPopup(True)
        self.fecha_alta_entry_paciente.setFixedWidth(120)
        row_layout9.addWidget(QLabel("Fecha de Alta:"))
        row_layout9.addWidget(self.fecha_alta_entry_paciente)

        self.hora_alta_entry_paciente = QTimeEdit()
        self.hora_alta_entry_paciente.setStyleSheet("background-color: white;")
        self.hora_alta_entry_paciente.setDisplayFormat("HH:mm")  # Formato de 24 horas
        self.hora_alta_entry_paciente.setFixedWidth(self.hora_alta_entry_paciente.sizeHint().width())
        row_layout9.addWidget(QLabel("Hora de Alta:"))
        row_layout9.addWidget(self.hora_alta_entry_paciente)

        layout.addRow(row_layout9)
        
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
            self.embarazada_checkbox_paciente.setVisible(True)
        else:
            self.embarazada_checkbox_paciente.setVisible(False)
            self.semanas_label_paciente.setVisible(False)
            self.semanas_combobox_paciente.setVisible(False)

    def toggle_semanas_field(self):
        if self.embarazada_checkbox_paciente.isChecked():
            self.semanas_label_paciente.setVisible(True)
            self.semanas_combobox_paciente.setVisible(True)
        else:
            self.semanas_label_paciente.setVisible(False)
            self.semanas_combobox_paciente.setVisible(False)

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
        nacionalidad = self.nacionalidad_entry_paciente.text()
        profesion_ocupacion = self.profesion_ocupacion_entry_paciente.text()
        religion = self.religion_entry_paciente.text()
        contacto_emergencia = self.contacto_emergencia_entry_paciente.text()
        parentesco = self.parentesco_entry_paciente.text()
        motivo_consulta = self.motivo_consulta_entry_paciente.text()
        enfermedad_actual = self.enfermedad_actual_entry_paciente.text()
        diagnostico_admision = self.diagnostico_admision_entry_paciente.text()
        intervencion_tratamiento = self.intervencion_tratamiento_entry_paciente.text()
        diagnostico_final = self.diagnostico_final_entry_paciente.text()
        estado_actual = self.estado_actual_combobox_paciente.currentText()
        fecha_alta = self.fecha_alta_entry_paciente.date().toPyDate()
        hora_alta = self.hora_alta_entry_paciente.time().toPyTime()

        if not cedula or not nombres or not apellidos or not lugar_nacimiento or not direccion or not motivo_consulta:
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
        self.nacionalidad_entry_paciente.clear()
        self.profesion_ocupacion_entry_paciente.clear()
        self.religion_entry_paciente.clear()
        self.contacto_emergencia_entry_paciente.clear()
        self.parentesco_entry_paciente.clear()
        self.motivo_consulta_entry_paciente.clear()
        self.enfermedad_actual_entry_paciente.clear()
        self.diagnostico_admision_entry_paciente.clear()
        self.intervencion_tratamiento_entry_paciente.clear()
        self.diagnostico_final_entry_paciente.clear()
        self.estado_actual_combobox_paciente.setCurrentIndex(0)
        self.fecha_alta_entry_paciente.setDate(QDate.currentDate())
        self.hora_alta_entry_paciente.setTime(QTime.currentTime())

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

        # Edad mínima y máxima en un QHBoxLayout
        edad_layout = QHBoxLayout()
        self.edad_min_combobox_consultas = QComboBox()
        self.edad_min_combobox_consultas.addItems([str(i) for i in range(101)])
        edad_layout.addWidget(QLabel("Edad Mínima:"))
        edad_layout.addWidget(self.edad_min_combobox_consultas)

        self.edad_max_combobox_consultas = QComboBox()
        self.edad_max_combobox_consultas.addItems([str(i) for i in range(101)])
        edad_layout.addWidget(QLabel("Edad Máxima:"))
        edad_layout.addWidget(self.edad_max_combobox_consultas)

        layout.addRow(edad_layout)

        self.direccion_entry_consultas = QLineEdit()
        self.direccion_entry_consultas.setStyleSheet("background-color: white;")
        layout.addRow(QLabel("Dirección:"), self.direccion_entry_consultas)

        self.tipo_enfermedad_entry_consultas = QLineEdit()
        self.tipo_enfermedad_entry_consultas.setStyleSheet("background-color: white;")
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
        edad_min = self.edad_min_combobox_consultas.currentText()
        edad_max = self.edad_max_combobox_consultas.currentText()
        direccion = self.direccion_entry_consultas.text()
        tipo_enfermedad = self.tipo_enfermedad_entry_consultas.text()
        embarazadas = self.embarazadas_combobox_consultas.currentText()

        # Aquí puedes agregar la lógica para realizar la búsqueda en la base de datos
        # y actualizar la lista de resultados (self.consultas_list)

        # Ejemplo de actualización de la lista de resultados
        self.consultas_list.clear()

        # Filtrar resultados según los criterios especificados
        results = self.filter_consultas(sexo, edad_min, edad_max, direccion, tipo_enfermedad, embarazadas)
        for result in results:
            self.consultas_list.addItem(result)

    def filter_consultas(self, sexo, edad_min, edad_max, direccion, tipo_enfermedad, embarazadas):
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
               (not edad_min or int(consulta["edad"]) >= int(edad_min)) and \
               (not edad_max or int(consulta["edad"]) <= int(edad_max)) and \
               (direccion in consulta["direccion"] or not direccion) and \
               (tipo_enfermedad in consulta["tipo_enfermedad"] or not tipo_enfermedad) and \
               (embarazadas == consulta["embarazadas"] or not embarazadas):
                filtered_consultas.append(f"Sexo: {consulta['sexo']}, Edad: {consulta['edad']}, Dirección: {consulta['direccion']}, Tipo de Enfermedad: {consulta['tipo_enfermedad']}, Embarazadas: {consulta['embarazadas']}")

        return filtered_consultas

    def create_farmacia_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        self.nombre_farmaco_entry = QLineEdit()
        self.nombre_farmaco_entry.setStyleSheet("background-color: white;")
        self.nombre_farmaco_entry.setMaxLength(200)  # Limitar a 200 caracteres
        self.nombre_farmaco_entry.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Nombre del Fármaco:"), self.nombre_farmaco_entry)

        self.fecha_elaboracion_entry = QDateEdit()
        self.fecha_elaboracion_entry.setStyleSheet("background-color: white;")
        layout.addRow(QLabel("Fecha de Elaboración:"), self.fecha_elaboracion_entry)
        self.fecha_elaboracion_entry.setCalendarPopup(True)

        self.lote_entry = QLineEdit()
        self.lote_entry.setStyleSheet("background-color: white;")
        self.lote_entry.setMaxLength(200)  # Limitar a 200 caracteres
        self.lote_entry.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Lote del Medicamento:"), self.lote_entry)

        self.fecha_caducidad_entry = QDateEdit()
        self.fecha_caducidad_entry.setStyleSheet("background-color: white;")
        layout.addRow(QLabel("Fecha de Caducidad:"), self.fecha_caducidad_entry)
        self.fecha_caducidad_entry.setCalendarPopup(True)

        self.cantidades_recibidas_entry = QLineEdit()
        self.cantidades_recibidas_entry.setStyleSheet("background-color: white;")
        self.cantidades_recibidas_entry.setMaxLength(200)  # Limitar a 200 caracteres
        self.cantidades_recibidas_entry.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Cantidades Recibidas:"), self.cantidades_recibidas_entry)

        self.cantidades_disponibles_entry = QLineEdit()
        self.cantidades_disponibles_entry.setStyleSheet("background-color: white;")
        self.cantidades_disponibles_entry.setMaxLength(200)  # Limitar a 200 caracteres
        self.cantidades_disponibles_entry.setFixedWidth(400)  # Ajustar tamaño del campo
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
        self.hospital_name_entry.setStyleSheet("background-color: white;")
        self.hospital_name_entry.setMaxLength(200)  # Limitar a 200 caracteres
        self.hospital_name_entry.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Nombre del Hospital:"), self.hospital_name_entry)
        self.direccion_entry_hospital = QLineEdit()
        self.direccion_entry_hospital.setStyleSheet("background-color: white;")
        self.direccion_entry_hospital.setMaxLength(200)  # Limitar a 200 caracteres
        self.direccion_entry_hospital.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Dirección:"), self.direccion_entry_hospital)
        self.telefono_entry_hospital = QLineEdit()
        self.telefono_entry_hospital.setStyleSheet("background-color: white;")
        self.telefono_entry_hospital.setMaxLength(200)  # Limitar a 200 caracteres
        self.telefono_entry_hospital.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Teléfono:"), self.telefono_entry_hospital)
        self.tipo_entry_hospital = QLineEdit()
        self.tipo_entry_hospital.setStyleSheet("background-color: white;")
        self.tipo_entry_hospital.setMaxLength(200)  # Limitar a 200 caracteres
        self.tipo_entry_hospital.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Tipo:"), self.tipo_entry_hospital)
        self.zona_entry_hospital = QLineEdit()
        self.zona_entry_hospital.setStyleSheet("background-color: white;")
        self.zona_entry_hospital.setMaxLength(200)  # Limitar a 200 caracteres
        self.zona_entry_hospital.setFixedWidth(400)  # Ajustar tamaño del campo
        layout.addRow(QLabel("Zona:"), self.zona_entry_hospital)

        self.save_button_configuracion = QPushButton("Guardar")
        self.save_button_configuracion.clicked.connect(self.save_configuracion)
        layout.addRow(self.save_button_configuracion)
        self.clear_button_configuracion = QPushButton("Limpiar Información")
        self.clear_button_configuracion.clicked.connect(self.clear_configuracion_form)
        layout.addRow(self.clear_button_configuracion)

        frame.setLayout(layout)
        return frame

    def save_configuracion(self):
        nombre_hospital = self.hospital_name_entry.text()
        direccion = self.direccion_entry_hospital.text()
        telefono = self.telefono_entry_hospital.text()
        tipo = self.tipo_entry_hospital.text()
        zona = self.zona_entry_hospital.text()

        if not nombre_hospital or not direccion or not telefono or not tipo or not zona:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        # Aquí puedes agregar la lógica para guardar los datos en la base de datos
        QMessageBox.information(self, "Guardado", "Datos del hospital guardados correctamente.")
        
        # Actualizar el nombre del hospital en la pantalla de inicio
        self.update_hospital_name()

    def clear_configuracion_form(self):
        self.hospital_name_entry.clear()
        self.direccion_entry_hospital.clear()
        self.telefono_entry_hospital.clear()
        self.tipo_entry_hospital.clear()
        self.zona_entry_hospital.clear()

    def update_hospital_name(self):
        self.hospital_name_label_inicio.setText(self.hospital_name_entry.text())

    def select_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if file_name:
            self.image_label_inicio.setPixmap(QPixmap(file_name).scaled(self.image_label_inicio.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def change_button_frame_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_frame.setStyleSheet(f"background-color: {color.name()};")

    def change_right_frames_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            for frame in self.frames.values():
                frame.setStyleSheet(f"background-color: {color.name()};")

    def change_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            for frame_name, frame in self.frames.items():
                if frame_name != "Configuracion":
                    for widget in frame.findChildren(QLabel):
                        if widget not in [self.hospital_name_label_inicio]:
                            widget.setStyleSheet(f"color: {color.name()};")
                if frame_name == "Inicio":
                    self.hospital_name_label_inicio.setStyleSheet(f"font-size: 40px; color: {color.name()};")
        
            # Cambiar el color de los textos en el frame de configuración
            for widget in self.findChildren(QLabel):
                if widget not in [self.date_label, self.hospital_name_label_inicio] and not isinstance(widget.parent(), QPushButton):
                    widget.setStyleSheet(f"color: {color.name()};")

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