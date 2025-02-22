from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QHBoxLayout, QLineEdit, QComboBox, QDateEdit, QTimeEdit, QPushButton, QMessageBox, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp, QDate, QTime

from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

class Pacientes(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.paciente_frame = self.create_paciente_frame()  # Guardar el frame en una variable de instancia
        layout.addWidget(self.paciente_frame)
    
    def show_paciente_frame(self):
        self.paciente_frame.setVisible(True)  # Hacer visible el frame de paciente

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
        self.birthdate_entry_paciente.setStyleSheet("""
            QDateEdit {
                background-color: white;
            }
            QCalendarWidget QToolButton {
                color: white;
                background-color: #2c3e50;
            }
            QCalendarWidget QMenu {
                color: white;
                background-color: #2c3e50;
            }
            QCalendarWidget QSpinBox {
                color: white;
                background-color: #2c3e50;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #2c3e50;
            }
            QCalendarWidget QAbstractItemView:enabled {
                color: white;
                background-color: #34495e;
                selection-background-color: #1abc9c;
                selection-color: black;
            }
        """)
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