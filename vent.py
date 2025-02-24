from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QStatusBar, QHBoxLayout, QMainWindow, QMenuBar, QMenu, QPushButton, QWidgetAction
from PySide6.QtCore import QTimer, Qt, QPoint
from PySide6.QtGui import QIcon, QAction
from servicios import CreateConnection
import sys
from datetime import datetime

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initTimer()

    def initUI(self):
        self.setWindowTitle("Resultado de la Conexión")
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QHBoxLayout()
        
        self.menu_layout = QVBoxLayout()
        self.content_layout = QVBoxLayout()
        
        self.etiqueta = QLabel("", self)
        self.content_layout.addWidget(self.etiqueta)
            
        self.status_label = QLabel("", self)
        self.menu_layout.addWidget(self.status_label)
        
        self.main_layout.addLayout(self.menu_layout)
        self.main_layout.addLayout(self.content_layout)
        
        self.central_widget.setLayout(self.main_layout)
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        self.status_label = QLabel("", self)
        self.status_bar.addPermanentWidget(self.status_label)
        
        self.setFixedSize(800, 600)  # Establecer un tamaño fijo para la ventana

        self.menu_bar = self.menuBar()

        # Agregar el ícono de hamburguesa a la barra de menú izquierda
        self.hamburger_action = QLabel()
        self.hamburger_action.setPixmap(QIcon("sistema-informacion-medica/src/iconos/ih2.png").pixmap(18, 18))
        self.hamburger_action.mousePressEvent = self.mostrar_menu_hamburguesa
        self.menu_bar.setCornerWidget(self.hamburger_action, Qt.TopLeftCorner)

        # Crear un espacio antes de la fecha y hora
        espacio_antes_fecha_hora = QWidget()
        espacio_antes_fecha_hora.setFixedWidth(10)  # Ajusta el ancho del espacio según sea necesario
        self.menu_bar.setCornerWidget(espacio_antes_fecha_hora, Qt.TopRightCorner)

        # Crear un QLabel para la fecha y hora
        self.fecha_hora_label = QLabel()
        self.fecha_hora_label.setStyleSheet("font-size: 18px;")  # Incrementar el tamaño de la fuente a 24
        self.menu_bar.setCornerWidget(self.fecha_hora_label, Qt.TopRightCorner)

        # Actualizar la fecha y hora periódicamente
        self.actualizar_fecha_hora()
        self.fecha_hora_timer = QTimer(self)
        self.fecha_hora_timer.timeout.connect(self.actualizar_fecha_hora)
        self.fecha_hora_timer.start(1000)  # Actualizar cada segundo

        # Establecer el fondo blanco para la ventana
        self.setStyleSheet("background-color: black;")

        # Crear el menú desplegable
        self.menu_hamburguesa = QMenu(self)
        self.boton = QPushButton("Botón de ejemplo", self)
        self.boton.clicked.connect(self.boton_click)
        action = QWidgetAction(self.menu_hamburguesa)
        action.setDefaultWidget(self.boton)
        self.menu_hamburguesa.addAction(action)

    def mostrar_menu_hamburguesa(self, event):
        if self.menu_hamburguesa.isVisible():
            self.menu_hamburguesa.hide()
        else:
            self.menu_hamburguesa.exec(self.hamburger_action.mapToGlobal(QPoint(0, self.hamburger_action.height())))

    def boton_click(self):
        print("Botón presionado")

    def initTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_resultado)
        self.timer.start(5000)  # 5000 ms = 5 segundos

    def actualizar_resultado(self):
        createconnection = CreateConnection()
        connection = createconnection.create_connection()
        estado = createconnection.check_connection(connection)
        mensaje = "Conexión exitosa" if estado == "Conectado" else "Conexión fallida"
        self.status_label.setText(mensaje)

    def actualizar_fecha_hora(self):
        now = datetime.now()
        self.fecha_hora_label.setText(now.strftime("%Y-%m-%d %H:%M:%S  "))

def mostrar_resultado():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    mostrar_resultado()