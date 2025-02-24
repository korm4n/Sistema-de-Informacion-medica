from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class SimpleVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Simple")
        self.setGeometry(100, 100, 800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = SimpleVentana()
    ventana.show()
    print("Ventana mostrada")  # Mensaje de depuración
    sys.exit(app.exec_())