import time
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class SplashScreen(QSplashScreen):
    def __init__(self, image_path):
        # Cargar la imagen de la pantalla de carga
        splash_pix = QPixmap(image_path)
        if splash_pix.isNull():
            raise FileNotFoundError(f"No se pudo cargar la imagen: {image_path}")
        
        super().__init__(splash_pix, Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Estilo CSS para el texto
        self.text_style = """
            color: #FFD700; /* Color dorado */
            font-size: 16px;
            font-weight: bold;
            font-family: Arial, Helvetica, sans-serif;
        """

    def show_loading_message(self, app, steps=10, delay=0.3):
        """
        Muestra mensajes de carga en la pantalla de carga.
        :param app: Instancia de QApplication.
        :param steps: Número de pasos de carga.
        :param delay: Tiempo de espera entre pasos (en segundos).
        """
        for i in range(1, steps + 1):
            # Aplicar el estilo al texto
            self.setStyleSheet(self.text_style)
            self.showMessage(f"Cargando... {i * (100 // steps)}%", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
            app.processEvents()
            time.sleep(delay)