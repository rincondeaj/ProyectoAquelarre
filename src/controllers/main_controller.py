class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.setup_connections()

    def setup_connections(self):
        # Connect UI signals to corresponding methods
        self.view.someButton.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        # Handle button click event
        data = self.model.get_data()
        self.view.update_display(data)

    def update_ui(self):
        # Update the UI based on model changes
        updated_data = self.model.get_data()
        self.view.update_display(updated_data)