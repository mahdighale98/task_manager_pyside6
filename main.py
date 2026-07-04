from PySide6.QtWidgets import QApplication
from core.main_window import MainWindow
import logging_config


if __name__ == "__main__":

    app = QApplication()

    window = MainWindow()
    window.showFullScreen()

    app.exec()