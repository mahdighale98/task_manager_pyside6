from styles import DARK_THEME, LIGHT_THEME

from PySide6.QtGui import QIcon, QShortcut, QKeySequence
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QWidget,
    QMessageBox,
)

from pages.home import HomePage



class MainWindow(QMainWindow):
    """Main application controller and navigation manager."""

    def __init__(self):
        super().__init__()

        self.page_stack = QStackedWidget()
        self.page_stack.setObjectName("mainArea")

        self.setCentralWidget(self.page_stack)

        self.dark_mode = True
        QApplication.instance().setStyleSheet(DARK_THEME)

        # Stores registered application pages
        self.pages = {}

        self.homepage = HomePage(self)

        self._setup_ui()
        self._setup_shortcuts()
        self._menubar()

    # Window Configuration
    def _setup_ui(self):
        """Configure main window properties and appearance."""

        self.setWindowTitle("Task Manager")
        self.setWindowIcon(QIcon("resources/icones/TK_icon.ico"))

    # Keyboard Shortcuts
    def _setup_shortcuts(self):
        """Initialize all global keyboard shortcuts."""

        self._create_fullscreen_shortcut()
        self._create_escape_shortcut()

    def _create_fullscreen_shortcut(self):
        """Bind F11 key to toggle fullscreen mode."""

        shortcut = QShortcut(QKeySequence("F11"), self)
        shortcut.activated.connect(self._toggle_fullscreen)

    def _create_escape_shortcut(self):
        """Bind ESC key to exit fullscreen mode."""

        shortcut = QShortcut(QKeySequence(Qt.Key_Escape), self)
        shortcut.activated.connect(self._exit_fullscreen)

    # Shortcut Handlers
    def _toggle_fullscreen(self):
        """Toggle between fullscreen and normal window mode."""

        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def _exit_fullscreen(self):
        """Exit fullscreen mode and restore maximized window state."""

        if self.isFullScreen():
            self.showMaximized()

    # Menu Bar
    def _menubar(self):
        """Create application menu."""

        menu = self.menuBar()

        action_theme = menu.addAction("Theme")
        action_theme.triggered.connect(self._toggle_theme)

        action_info = menu.addAction("Info")
        action_info.triggered.connect(self._show_info_dialog)

        action_exit = menu.addAction("Exit")
        action_exit.triggered.connect(self._show_exit_dialog)

    def _toggle_theme(self):
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            QApplication.instance().setStyleSheet(DARK_THEME)
        else:
            QApplication.instance().setStyleSheet(LIGHT_THEME)

    def _show_info_dialog(self):
        """Display application information."""

        message = QMessageBox(self)

        message.setWindowTitle("Info")
        message.setText(
            "Task Manager V1.0.0\n" \
            "Developed by MahdiGhale98"
        )
        
        message.setStandardButtons(QMessageBox.Ok)

        message.exec()

    def _show_exit_dialog(self):
        """Display exit confirmation dialog."""

        message = QMessageBox(self)
        message.setWindowTitle("Exit")
        message.setText("Are you sure you want to exit?")

        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setDefaultButton(QMessageBox.No)

        if message.exec()  == QMessageBox.Yes:
            QApplication.quit()

    # Page Navigation
    def register(self, name: str, page: QWidget):
        """Register a new page and add it to the stacked widget system."""

        self.pages[name] = page
        self.page_stack.addWidget(page)

    def go(self, name: str):
        """Switch to a registered page by its name."""

        page = self.pages.get(name)
        self.page_stack.setCurrentWidget(page)