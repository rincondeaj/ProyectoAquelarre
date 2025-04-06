import os
import webbrowser
from PyQt5.QtWidgets import QMessageBox

class ManualFunctions:
    def __init__(self, parent):
        """
        Inicializa las funciones del manual.
        :param parent: La ventana principal que contiene los botones y widgets.
        """
        self.parent = parent

    def open_pdf(self, page):
        """
        Abre el archivo PDF en la página especificada.
        :param page: Número de página para abrir.
        """
        # Ruta del archivo PDF
        pdf_path = os.path.join(os.getcwd(), "resources/manual/Manual.pdf")

        # Verifica si el archivo existe
        if not os.path.exists(pdf_path):
            QMessageBox.critical(self.parent, "Error", f"No se encontró el archivo PDF en: {pdf_path}")
            return

        # Abre el PDF en la página especificada
        try:
            webbrowser.open(f"file://{pdf_path}#page={page}")
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"No se pudo abrir el archivo PDF: {str(e)}")

    def setup_manual_buttons(self):
        """
        Conecta los botones de la página Manual a sus respectivas funciones.
        """