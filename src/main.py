import sys
from PyQt5.QtWidgets import QApplication
from loadingScreem import SplashScreen
from mainWindow import MainWindow  # Importa la clase MainWindow desde mainwindow.py

def main():
    app = QApplication(sys.argv)

    # Crear la pantalla de carga
    splash = SplashScreen("resources/images/aquelarre.png")
    splash.show()

    # Mostrar mensajes de carga
    splash.show_loading_message(app)

    # Cargar el archivo de estilos
    with open("resources/styles.qss", "r") as f:
        app.setStyleSheet(f.read())
        
    # Crear la ventana principal desde mainwindow.py
    main_window = MainWindow()
    main_window.show()

    # Cerrar la pantalla de carga
    splash.finish(main_window)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()