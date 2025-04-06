import sys
import os
import webbrowser
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QCompleter
from PyQt5.QtCore import Qt
from menu import Ui_MainWindow  # Importa la interfaz generada desde menu.py
from manual import ManualFunctions
from button_connections import setup_button_connections

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Configura la interfaz generada por menu.py
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Inicializa las funciones del manual
        self.manual_functions = ManualFunctions(self)
        self.manual_functions.setup_manual_buttons()

        # Oculta widgets o configura elementos si es necesario
        try:
            self.ui.Icon_Full_Widget.hide()  # Oculta el widget si existe
        except AttributeError:
            print("Advertencia: 'Icon_Full_Widget' no está definido en menu.py")

        # Configura el stackedWidget en la primera página
        self.ui.stackedWidget.setCurrentIndex(0)  # Cambia a la página que contiene Manual_Stacked_Widget
        self.ui.Manual_Stacked_Widget.setCurrentIndex(0)  # Cambia a la página 0 dentro de Manual_Stacked_Widget

        # Configura el autocompletado para el buscador
        self.setup_autocomplete()

        # Conecta los botones a sus respectivas funciones
        navigate_to_manual_page = {
            0: self.navigate_to_manual_page_0,
            1: self.navigate_to_manual_page_1,
            2: self.navigate_to_manual_page_2,
            3: self.navigate_to_manual_page_3,
            4: self.navigate_to_manual_page_4,
            5: self.navigate_to_manual_page_5,
            6: self.navigate_to_manual_page_6,
        }
        setup_button_connections(self.ui, self.open_pdf_at_page, navigate_to_manual_page)

    def setup_autocomplete(self):
        """
        Configura el autocompletado para el campo de búsqueda (TextEntryLine).
        Si el campo está vacío, muestra todas las opciones.
        """
        # Lista de palabras para autocompletar
        suggestions = ["Manual", "Combate", "Personajes", "Estadísticas", "Diario", "Dados", "Mercaderes"]

        # Configura el modelo de autocompletar
        completer = QCompleter(suggestions, self)
        completer.setCaseSensitivity(False)  # No distingue entre mayúsculas y minúsculas
        completer.setFilterMode(Qt.MatchContains)  # Sugerencias que contienen el texto
        completer.setCompletionMode(QCompleter.PopupCompletion)  # Muestra un popup con sugerencias

        # Asigna el autocompletado al campo de texto
        self.ui.TextEntryLine.setCompleter(completer)

        # Configura el comportamiento para mostrar todas las opciones si el campo está vacío
        def show_all_options():
            if not self.ui.TextEntryLine.text().strip():  # Si el campo está vacío
                completer.complete()  # Muestra todas las opciones

        # Conecta el evento de texto cambiado para verificar si el campo está vacío
        self.ui.TextEntryLine.textChanged.connect(show_all_options)

        # Configura el comportamiento del tabulador
        self.ui.TextEntryLine.returnPressed.connect(lambda: completer.complete())

    def navigate_to_manual_page_0(self):
        """
        Navega a la página 0 dentro del Manual_Stacked_Widget.
        """
        # Asegúrate de que la página que contiene Manual_Stacked_Widget esté activa
        self.ui.stackedWidget.setCurrentIndex(0)  # Cambia al índice de la página que contiene Manual_Stacked_Widget

        # Cambia a la página 0 dentro de Manual_Stacked_Widget
        self.ui.Manual_Stacked_Widget.setCurrentIndex(0)

    def navigate_to_manual_page_1(self):
        """
        Navega a la página 1 dentro del Manual_Stacked_Widget.
        """
        # Asegúrate de que la página que contiene Manual_Stacked_Widget esté activa
        self.ui.stackedWidget.setCurrentIndex(0)  # Cambia al índice de la página que contiene Manual_Stacked_Widget

        # Cambia a la página 1 dentro de Manual_Stacked_Widget
        self.ui.Manual_Stacked_Widget.setCurrentIndex(1)

    def navigate_to_manual_page_2(self):
        """
        Navega a la página 2 dentro del Manual_Stacked_Widget.
        """
        # Asegúrate de que la página que contiene Manual_Stacked_Widget esté activa
        self.ui.stackedWidget.setCurrentIndex(0)  # Cambia al índice de la página que contiene Manual_Stacked_Widget

        # Cambia a la página 2 dentro de Manual_Stacked_Widget
        self.ui.Manual_Stacked_Widget.setCurrentIndex(2)

    def navigate_to_manual_page_3(self):
        """
        Navega a la página 3 dentro del Manual_Stacked_Widget.
        """
        # Asegúrate de que la página que contiene Manual_Stacked_Widget esté activa
        self.ui.stackedWidget.setCurrentIndex(0)  # Cambia al índice de la página que contiene Manual_Stacked_Widget

        # Cambia a la página 3 dentro de Manual_Stacked_Widget
        self.ui.Manual_Stacked_Widget.setCurrentIndex(3)

    def navigate_to_manual_page_4(self):
        """
        Navega a la página 4 dentro del Manual_Stacked_Widget.
        """
        # Asegúrate de que la página que contiene Manual_Stacked_Widget esté activa
        self.ui.stackedWidget.setCurrentIndex(0)  # Cambia al índice de la página que contiene Manual_Stacked_Widget

        # Cambia a la página 4 dentro de Manual_Stacked_Widget
        self.ui.Manual_Stacked_Widget.setCurrentIndex(4)

    def navigate_to_manual_page_5(self):
        """
        Navega a la página 5 dentro del Manual_Stacked_Widget.
        """
        # Asegúrate de que la página que contiene Manual_Stacked_Widget esté activa
        self.ui.stackedWidget.setCurrentIndex(0)  # Cambia al índice de la página que contiene Manual_Stacked_Widget

        # Cambia a la página 5 dentro de Manual_Stacked_Widget
        self.ui.Manual_Stacked_Widget.setCurrentIndex(5)

    def navigate_to_manual_page_6(self):
        """
        Navega a la página 6 dentro del Manual_Stacked_Widget.
        """
        # Asegúrate de que la página que contiene Manual_Stacked_Widget esté activa
        self.ui.stackedWidget.setCurrentIndex(0)  # Cambia al índice de la página que contiene Manual_Stacked_Widget

        # Cambia a la página 6 dentro de Manual_Stacked_Widget
        self.ui.Manual_Stacked_Widget.setCurrentIndex(6)

    def handle_search(self):
        """
        Método que se ejecuta cuando se hace clic en el botón SearchButton.
        Redirige a una página específica del QStackedWidget según el texto ingresado.
        """
        # Obtén el texto ingresado en el campo de búsqueda
        search_text = self.ui.TextEntryLine.text().strip()

        # Diccionario que mapea textos a índices de páginas
        page_mapping = {
            "Manual": 0,
            "Personajes": 1,
            "Combate": 2,
            "Dados": 3,
            "Mercaderes": 4,
            "Diario": 5,
            "Estadísticas": 6
        }

        # Verifica si el texto ingresado coincide con alguna página
        if search_text in page_mapping:
            page_index = page_mapping[search_text]
            self.ui.stackedWidget.setCurrentIndex(page_index)
            QMessageBox.information(self, "Redirección", f"Redirigiendo a la página: {search_text.capitalize()}")
        else:
            QMessageBox.warning(self, "Error", "No se encontró una página para el texto ingresado.")

    def open_pdf_at_page(self, page):
        """
        Abre el archivo manual.pdf en una página específica.
        :param page: Número de página para abrir.
        """
        # Ruta del archivo PDF
        pdf_path = os.path.join(os.getcwd(), "resources/manual/Manual.pdf")

        # Verifica si el archivo existe
        if not os.path.exists(pdf_path):
            QMessageBox.critical(self, "Error", f"No se encontró el archivo PDF en: {pdf_path}")
            return

        # Abre el PDF en la página especificada
        try:
            webbrowser.open(f"file://{pdf_path}#page={page}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el archivo PDF: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Instancia la ventana principal
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())