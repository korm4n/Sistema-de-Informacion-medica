from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox, QFileDialog, QColorDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Configuracion(QWidget):
    def __init__(self):
        super().__init__()
        self.config_frame = self.create_configuracion_frame()  # Crear el frame de configuración
        layout = QVBoxLayout()
        layout.addWidget(self.config_frame)
        self.setLayout(layout)
        
    def create_configuracion_frame(self):
        frame = QWidget()
        layout = QFormLayout(frame)
        
        self.hospital_name_entry = QLineEdit()
        self.hospital_name_entry.setStyleSheet("background-color: white;")
        self.hospital_name_entry.setMaxLength(200)
        self.hospital_name_entry.setFixedWidth(400)
        layout.addRow(QLabel("Nombre del Hospital:"), self.hospital_name_entry)
        
        self.direccion_entry_hospital = QLineEdit()
        self.direccion_entry_hospital.setStyleSheet("background-color: white;")
        self.direccion_entry_hospital.setMaxLength(200)
        self.direccion_entry_hospital.setFixedWidth(400)
        layout.addRow(QLabel("Dirección:"), self.direccion_entry_hospital)
        
        self.telefono_entry_hospital = QLineEdit()
        self.telefono_entry_hospital.setStyleSheet("background-color: white;")
        self.telefono_entry_hospital.setMaxLength(200)
        self.telefono_entry_hospital.setFixedWidth(400)
        layout.addRow(QLabel("Teléfono:"), self.telefono_entry_hospital)
        
        self.tipo_entry_hospital = QLineEdit()
        self.tipo_entry_hospital.setStyleSheet("background-color: white;")
        self.tipo_entry_hospital.setMaxLength(200)
        self.tipo_entry_hospital.setFixedWidth(400)
        layout.addRow(QLabel("Tipo:"), self.tipo_entry_hospital)
        
        self.zona_entry_hospital = QLineEdit()
        self.zona_entry_hospital.setStyleSheet("background-color: white;")
        self.zona_entry_hospital.setMaxLength(200)
        self.zona_entry_hospital.setFixedWidth(400)
        layout.addRow(QLabel("Zona:"), self.zona_entry_hospital)
        
        self.save_button_configuracion = QPushButton("Guardar")
        self.save_button_configuracion.clicked.connect(self.save_configuracion)
        layout.addRow(self.save_button_configuracion)
        
        self.clear_button_configuracion = QPushButton("Limpiar Información")
        self.clear_button_configuracion.clicked.connect(self.clear_configuracion_form)
        layout.addRow(self.clear_button_configuracion)
        
        frame.setLayout(layout)
        return frame

    def show_configuracion_frame(self):
        self.config_frame.show()
        self.config_frame.raise_()

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