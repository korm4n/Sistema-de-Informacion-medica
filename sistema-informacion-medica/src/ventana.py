from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QHBoxLayout, QSizePolicy, QFrame, QMenuBar, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
import sys
from frames.inicio import Inicio
from frames.medicos_enfermeras import MedicosEnfermeras
from frames.pacientes import Pacientes
from frames.historial_medico import HistorialMedico
from frames.consultas import Consultas
from frames.farmacia import Farmacia
from frames.configuracion import Configuracion
from servicios import ServicioDB

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Información Médica")
        self.setGeometry(100, 100, 1260, 780)  # Establece la posición y el tamaño de la ventana
        self.setWindowIcon(QIcon("sistema-informacion-medica/src/iconos/SIMV.png"))  # Cambiar el icono de la ventana
        self.servicio_db = ServicioDB()
        self.init_ui()

    def init_ui(self):
        # Crear un widget central
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: silver;")  # Establecer color de fondo a gris plateado
        self.setCentralWidget(central_widget)

        # Crear un layout horizontal
        layout = QHBoxLayout()
        # Crear un frame para los botones y establecer su color de fondo a negro
        botones_frame = QFrame()
        botones_frame.setStyleSheet("background-color: black;")

        # Crear un layout vertical para los botones
        botones_layout = QVBoxLayout()
        botones_layout.setAlignment(Qt.AlignTop)  # Alinear los botones en la parte superior

        # Crear botones y conectar sus señales
        botones = ["Inicio", "Médicos/Enfermeras", "Pacientes", "Historial Médico", "Consultas", "Farmacia", "Configuración"]
        iconos = ["sistema-informacion-medica/src/iconos/inicio.png", "sistema-informacion-medica/src/iconos/medicos.png", "sistema-informacion-medica/src/iconos/pacientes.png", "sistema-informacion-medica/src/iconos/historial.png", "sistema-informacion-medica/src/iconos/consultas.png", "sistema-informacion-medica/src/iconos/farmacia.png", "sistema-informacion-medica/src/iconos/config.png"]
        self.buttons = {}
        max_width = 320
        for nombre, icono in zip(botones, iconos):
            boton = QPushButton(nombre)
            boton.setIcon(QIcon(icono))  # Establecer el icono del botón
            boton.setFixedWidth(boton.sizeHint().width())  # Ajustar la longitud del botón al texto
            max_width = max(max_width, boton.sizeHint().width())  # Encontrar el ancho máximo
            boton.setCheckable(True)  # Hacer el botón checkable
            boton.clicked.connect(lambda checked, n=nombre: self.cambiar_frame(n.replace("<br>", " ")))
            boton.clicked.connect(self.actualizar_botones)  # Conectar la señal para actualizar el estado de los botones
            botones_layout.addWidget(boton)
            self.buttons[nombre] = boton

        # Ajustar todos los botones al ancho máximo
        for boton in self.buttons.values():
            boton.setFixedWidth(max_width)

        # Aplicar estilos a los botones
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
                background-color: silver;  /* Color de fondo al pasar el mouse */
                color: white;  /* Color del texto al pasar el mouse */
            }
            QPushButton:checked {
                background-color: silver;  /* Color de fondo cuando está seleccionado */
                color: white;  /* Color del texto cuando está seleccionado */
            }
        """

        for key, button in self.buttons.items():
            button.setIconSize(QSize(64, 64))  # Establecer tamaño del icono
            button.setFixedHeight(80)  # Establecer altura fija para los botones
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Permitir que el ancho se ajuste al contenido
            button.setStyleSheet(button_style)

        # Agregar el layout de los botones al frame
        botones_frame.setLayout(botones_layout)

        # Crear un QStackedWidget para cambiar entre los frames
        self.stacked_widget = QStackedWidget()

        # Agregar los layouts al layout principal
        layout.addWidget(botones_frame)
        layout.addWidget(self.stacked_widget)

        # Asignar el layout al widget central
        central_widget.setLayout(layout)

        # Agregar los frames al QStackedWidget
        self.frames = {
            "Inicio": Inicio(),
            "Médicos/Enfermeras": MedicosEnfermeras(),
            "Pacientes": Pacientes(),
            "Historial Médico": HistorialMedico(),
            "Consultas": Consultas(),
            "Farmacia": Farmacia(),
            "Configuración": Configuracion(),
        }
        for frame in self.frames.values():
            self.stacked_widget.addWidget(frame)

        # Mostrar el frame "Inicio" al iniciar la aplicación
        self.cambiar_frame("Inicio")
        self.buttons["Inicio"].setChecked(True)  # Marcar el botón "Inicio" como seleccionado al inicio

        # Crear la barra de menú
        self.menu_bar = self.menuBar()
        self.estado_conexion_label = QLabel(self.servicio_db.estado_conexion())
        self.menu_bar.setCornerWidget(self.estado_conexion_label, Qt.TopLeftCorner)

        # Intentar conectar a la base de datos
        if self.servicio_db.conectar():
            self.estado_conexion_label.setText("Conectado")
        else:
            self.estado_conexion_label.setText("Desconectado")

    def cambiar_frame(self, nombre):
        frame = self.frames.get(nombre)
        if frame:
            self.stacked_widget.setCurrentWidget(frame)

    def actualizar_botones(self):
        # Desmarcar todos los botones excepto el que fue clicado
        for button in self.buttons.values():
            if button.isChecked():
                button.setChecked(False)
        sender = self.sender()
        if sender:
            sender.setChecked(True)

    def closeEvent(self, event):
        # Manejo del evento de cierre de la ventana
        self.servicio_db.desconectar()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())