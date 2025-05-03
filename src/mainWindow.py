import sys
import os
import webbrowser
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QCompleter, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QWidget, QMenu, QAction
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from menu import Ui_MainWindow  # Importa la interfaz generada desde menu.py
from manual import ManualFunctions
from button_connections import setup_button_connections

def create_personaje_frame(file_name, number):
    """
    Crea un QFrame con una imagen pequeña a la izquierda, texto y un número a la derecha.
    Agrega un menú contextual con opciones al hacer clic derecho.
    :param file_name: Nombre del archivo (texto a mostrar).
    :param number: Número asociado al archivo.
    :return: Un QFrame con los elementos organizados.
    """
    # Crear el QFrame principal
    frame = QFrame()
    frame.setStyleSheet("background-color: #e0e0e0; border: 1px solid #000; border-radius: 5px;")
    frame.setMinimumSize(300, 100)  # Tamaño mínimo del rectángulo

    # Crear un diseño horizontal para el QFrame
    layout = QHBoxLayout(frame)

    # Crear un QLabel para la imagen
    image_label = QLabel()
    pixmap = QPixmap("resources/images/Adela.jpeg")  # Ruta de la imagen
    pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Escalar la imagen a un tamaño más pequeño
    image_label.setPixmap(pixmap)
    image_label.setFixedSize(60, 60)  # Tamaño fijo del contenedor de la imagen
    image_label.setAlignment(Qt.AlignCenter)

    # Crear un diseño vertical para el texto y el número
    text_layout = QVBoxLayout()

    # Crear un QLabel para el texto (nombre del archivo)
    text_label = QLabel(f"Ficha: {file_name}")
    text_label.setStyleSheet("font-size: 12px; color: #555;")
    text_label.setAlignment(Qt.AlignCenter)

    # Crear un QLabel para el número
    number_label = QLabel(f"PV : {number}")
    number_label.setStyleSheet("font-size: 12px; color: #555;")
    number_label.setAlignment(Qt.AlignCenter)

    # Agregar el texto y el número al diseño vertical
    text_layout.addWidget(text_label)
    text_layout.addWidget(number_label)

    # Crear un diseño vertical para Estado y Jugador
    state_layout = QVBoxLayout()

    # Crear un QLabel para el estado
    state_label = QLabel(f"Estado : Y")
    state_label.setStyleSheet("font-size: 12px; color: #555;")
    state_label.setAlignment(Qt.AlignCenter)

    # Crear un QLabel para el jugador
    player_label = QLabel(f"Jugador : Z")
    player_label.setStyleSheet("font-size: 12px; color: #555;")
    player_label.setAlignment(Qt.AlignCenter)

    # Agregar Estado y Jugador al diseño vertical
    state_layout.addWidget(state_label)
    state_layout.addWidget(player_label)

    # Agregar la imagen, el diseño de texto y el diseño de estado al diseño horizontal
    layout.addWidget(image_label)  # Imagen a la izquierda
    layout.addLayout(text_layout)  # Texto y número en el centro
    layout.addLayout(state_layout)  # Estado y jugador a la derecha

    # Agregar un menú contextual al QFrame
    def show_context_menu(pos):
        menu = QMenu()
        abrir_action = QAction("Abrir", frame)
        eliminar_action = QAction("Eliminar", frame)
        estadisticas_action = QAction("Estadísticas", frame)
        notas_action = QAction("Notas", frame)

        # Conectar las acciones a funciones (puedes definirlas según tu lógica)
        abrir_action.triggered.connect(lambda: print(f"Abrir {file_name}"))
        eliminar_action.triggered.connect(lambda: print(f"Eliminar {file_name}"))
        estadisticas_action.triggered.connect(lambda: print(f"Estadísticas de {file_name}"))
        notas_action.triggered.connect(lambda: print(f"Notas de {file_name}"))

        # Agregar las acciones al menú
        menu.addAction(abrir_action)
        menu.addAction(eliminar_action)
        menu.addAction(estadisticas_action)
        menu.addAction(notas_action)

        # Mostrar el menú en la posición del cursor
        menu.exec_(frame.mapToGlobal(pos))

    # Sobrescribir el evento de clic derecho
    frame.setContextMenuPolicy(Qt.CustomContextMenu)
    frame.customContextMenuRequested.connect(show_context_menu)

    return frame

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Configura la interfaz generada por menu.py
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Configura el QScrollArea para la página 2
        self.scroll_area = QScrollArea(self.ui.page_2)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setSpacing(5)  # Espaciado mínimo de 5 píxeles entre rectángulos
        self.scroll_area.setWidget(self.scroll_content)

        # Reemplaza el layout de la página 2 con el QScrollArea
        self.ui.verticalLayout_6.addWidget(self.scroll_area)

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

        # Conecta el evento de cambio de página
        self.ui.stackedWidget.currentChanged.connect(self.on_page_changed)

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

    def on_page_changed(self, index):
        """
        Maneja el evento de cambio de página en el stackedWidget.
        """
        if index == 2:  # Página 2
            self.show_personajes_files()

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

    def show_personajes_files(self):
        """
        Muestra un rectángulo por cada archivo .aq en la carpeta 'personajes' en la página 2 del stackedWidget.
        """
        # Ruta de la carpeta 'personajes'
        personajes_folder = os.path.join(os.getcwd(), "resources/personajes")

        # Verifica si la carpeta existe
        if not os.path.exists(personajes_folder):
            QMessageBox.warning(self, "Advertencia", f"No se encontró la carpeta: {personajes_folder}")
            return

        # Filtra los archivos que terminan en .aq
        archivos_aq = [f for f in os.listdir(personajes_folder) if f.endswith(".aq")]

        # Limpia el layout de la página 2 antes de agregar nuevos widgets
        for i in reversed(range(self.scroll_layout.count())):
            widget_to_remove = self.scroll_layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.deleteLater()

        # Crea un rectángulo para cada archivo
        for index, archivo in enumerate(archivos_aq, start=1):
            # Crea un QFrame utilizando la función create_personaje_frame
            frame = create_personaje_frame(archivo, index)

            # Agrega el QFrame al layout del scroll
            self.scroll_layout.addWidget(frame)

        # Agrega un espacio al final para mantener el diseño limpio
        self.scroll_layout.addStretch()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Instancia la ventana principal
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())