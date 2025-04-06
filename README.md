# PyQt5 Desktop Application

This project is a desktop application built using PyQt5. It serves as a template for developing GUI applications with a structured approach, separating the UI, controllers, and models.

## Project Structure

```
pyqt5-desktop-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── ui
│   │   └── main_window.ui     # UI layout designed with Qt Designer
│   ├── controllers
│   │   └── main_controller.py  # Manages interactions between UI and data model
│   ├── models
│   │   └── data_model.py      # Represents the data structure used in the application
│   └── resources
│       └── styles.qss         # Stylesheet for the application
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd pyqt5-desktop-app
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Execute the following command to start the application:
   ```
   python src/main.py
   ```

## Usage Guidelines

- The main window of the application is defined in `src/ui/main_window.ui`. You can modify this file using Qt Designer to change the layout and elements.
- The `MainController` class in `src/controllers/main_controller.py` handles user interactions and updates the UI. You can add more methods to handle additional functionality.
- The `DataModel` class in `src/models/data_model.py` is responsible for data manipulation. You can extend this class to include more data handling methods as needed.
- The visual styles for the application can be customized in `src/resources/styles.qss`.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.