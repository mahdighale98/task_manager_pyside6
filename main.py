import sys 

from styles import (
    style_window,
    style_topic_label,
    style_footer_label,
    style_messagebox
)

from PySide6.QtGui import QIcon, QShortcut, QKeySequence
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox,
    QLabel,
)

class Main:
    """Main application controller responsible for managing the UI, pages."""

    def __init__(self):

        self.app = QApplication(sys.argv)
        self.window = QMainWindow()

        self.stack = QStackedWidget()
        self.window.setCentralWidget(self.stack)

        self.pages = {}

        Homepage(self)

        self._setup_ui()
        self._setup_shortcut()
        self._menubar()

    # ==================================================
    # Window Setup
    # ==================================================

    def _setup_ui(self):
        """Configure main window properties and appearance."""

        self.window.setWindowTitle("Task Manager")
        self.window.setWindowIcon(QIcon("resources/icones/TK_icon.ico"))
        self.window.setStyleSheet(style_window)

        self.window.showFullScreen()

    # ==================================================
    # Shortcuts
    # ==================================================

    def _setup_shortcut(self):
        """Initialize all global keyboard shortcuts."""

        self._fullscreen_shortcut()
        self._escape_shortcut()

    def _fullscreen_shortcut(self):
        """Bind F11 key to toggle fullscreen mode."""

        shortcut = QShortcut(QKeySequence("F11"), self.window)
        shortcut.activated.connect(self._def_fullscreen_shortcut)

    def _escape_shortcut(self):
        """Bind ESC key to exit fullscreen mode."""

        shortcut = QShortcut(QKeySequence(Qt.Key_Escape), self.window)
        shortcut.activated.connect(self._def_escape_shortcut)

    # ==================================================
    # Shortcut Actions
    # ==================================================
    def _def_fullscreen_shortcut(self):
        """Toggle between fullscreen and normal window mode."""

        if self.window.isFullScreen():
            self.window.showNormal()
        else:
            self.window.showFullScreen()

    def _def_escape_shortcut(self):
        """Exit fullscreen mode and restore maximized window state."""

        if self.window.isFullScreen():
            self.window.showMaximized()

    # ==================================================
    # Menu Bar
    # ==================================================
    def _menubar(self):

        menu = self.window.menuBar()

        action_info = menu.addAction("Info")
        action_info.triggered.connect(self._def_info_action)

        action_exit = menu.addAction("Exit")
        action_exit.triggered.connect(self._def_exit_action)

    def _def_info_action(self):

        msg = QMessageBox(self.window)
        msg.setWindowTitle("Info")
        msg.setText("Task Manager V1.0.0\nDeveloped by MahdiGhale98")
        
        msg.setStyleSheet(style_messagebox)

        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec()

    def _def_exit_action(self):
        
        msg = QMessageBox(self.window)
        msg.setWindowTitle("Exit")
        msg.setText("Are you sure you want to exit?")
        
        msg.setStyleSheet(style_messagebox)

        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)

        if msg.exec()  == QMessageBox.Yes:
            self.app.quit()

    # ==================================================
    # Navigation System
    # ==================================================
    def register(self, name: str, page: QWidget):
        """Register a new page and add it to the stacked widget system."""

        self.pages[name] = page
        self.stack.addWidget(page)

    def go(self, name: str):
        """Switch to a registered page by its name."""

        page = self.pages.get(name)
        self.stack.setCurrentWidget(page)

    def run(self):
        """Start the Qt application event loop and display the main window."""

        self.app.exec()



class Homepage:
    """Home screen of the application where users can navigate to main features."""

    def __init__(self, app: Main):
        """
        Create homepage UI and register it inside the main application stack.
        Args:
            app (Main): Reference to the main application controller.
        """

        self.app = app
        self.page = QWidget()

        self.app.register("Homepage", self.page)

        self._build()

    def _build(self):
        """Build and arrange all UI components of the homepage."""

        self.base_layout = QVBoxLayout()
        self.page.setLayout(self.base_layout)

        # ==================================================
        # Header
        # ==================================================
        label_topic = QLabel("Task Manager")
        label_topic.setStyleSheet(style_topic_label)
        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)

        # ==================================================
        # Workspace
        # ==================================================        
        self.middle_layout = QHBoxLayout()
        self.base_layout.addLayout(self.middle_layout)

        # Navigation panel
        self.sidebar_widget = QWidget()
        self.vsidebar_layout = QVBoxLayout()

        self.sidebar_widget.setFixedWidth(250)

        self.sidebar_widget.setLayout(self.vsidebar_layout)
        self.middle_layout.addWidget(self.sidebar_widget)

        # Main content area
        self.content_widget = QWidget()
        self.vcontent_layout = QVBoxLayout()

        self.content_widget.setLayout(self.vcontent_layout)
        self.middle_layout.addWidget(self.content_widget, stretch = 1)

        # ==================================================
        # Footer
        # ==================================================         
        label_footer = QLabel("Task manager | V1.0.0")
        label_footer.setStyleSheet(style_footer_label)
        self.base_layout.addWidget(label_footer, alignment = Qt.AlignLeft | Qt.AlignBottom)

if __name__ == "__main__":
    app = Main()
    app.run()