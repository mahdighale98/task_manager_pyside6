import sys 

from styles import (
    style_window,
    style_content,
    style_sidebar,
    style_topic_label,
    style_label,
    style_footer_label,
    style_button,
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
    QPushButton
)

class MainWindow:
    """Main application controller and navigation manager."""

    def __init__(self):

        self.app = QApplication(sys.argv)
        self.window = QMainWindow()

        self.page_stack = QStackedWidget()
        self.window.setCentralWidget(self.page_stack)

        # Stores registered application pages
        self.pages = {}

        HomePage(self)

        self._setup_ui()
        self._setup_shortcuts()
        self._menubar()

    # Window Configuration
    def _setup_ui(self):
        """Configure main window properties and appearance."""

        self.window.setWindowTitle("Task Manager")
        self.window.setWindowIcon(QIcon("resources/icones/TK_icon.ico"))
        self.window.setStyleSheet(style_window)

        self.window.showFullScreen()

    # Keyboard Shortcuts
    def _setup_shortcuts(self):
        """Initialize all global keyboard shortcuts."""

        self._create_fullscreen_shortcut()
        self._create_escape_shortcut()

    def _create_fullscreen_shortcut(self):
        """Bind F11 key to toggle fullscreen mode."""

        shortcut = QShortcut(QKeySequence("F11"), self.window)
        shortcut.activated.connect(self._toggle_fullscreen)

    def _create_escape_shortcut(self):
        """Bind ESC key to exit fullscreen mode."""

        shortcut = QShortcut(QKeySequence(Qt.Key_Escape), self.window)
        shortcut.activated.connect(self._exit_fullscreen)

    # Shortcut Handlers
    def _toggle_fullscreen(self):
        """Toggle between fullscreen and normal window mode."""

        if self.window.isFullScreen():
            self.window.showNormal()
        else:
            self.window.showFullScreen()

    def _exit_fullscreen(self):
        """Exit fullscreen mode and restore maximized window state."""

        if self.window.isFullScreen():
            self.window.showMaximized()

    # Menu Bar
    def _menubar(self):
        """Create application menu."""

        menu = self.window.menuBar()

        action_info = menu.addAction("Info")
        action_info.triggered.connect(self._show_info_dialog)

        action_exit = menu.addAction("Exit")
        action_exit.triggered.connect(self._show_exit_dialog)

    def _show_info_dialog(self):
        """Display application information."""

        message = QMessageBox(self.window)

        message.setWindowTitle("Info")
        message.setText(
            "Task Manager V1.0.0\n" \
            "Developed by MahdiGhale98"
        )
        
        message.setStyleSheet(style_messagebox)
        message.setStandardButtons(QMessageBox.Ok)

        message.exec()

    def _show_exit_dialog(self):
        """Display exit confirmation dialog."""

        message = QMessageBox(self.window)
        message.setWindowTitle("Exit")
        message.setText("Are you sure you want to exit?")
        
        message.setStyleSheet(style_messagebox)

        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setDefaultButton(QMessageBox.No)

        if message.exec()  == QMessageBox.Yes:
            self.app.quit()

    # Page Navigation
    def register(self, name: str, page: QWidget):
        """Register a new page and add it to the stacked widget system."""

        self.pages[name] = page
        self.page_stack.addWidget(page)

    def go(self, name: str):
        """Switch to a registered page by its name."""

        page = self.pages.get(name)
        self.page_stack.setCurrentWidget(page)

    def run(self):
        """Start the Qt application event loop and display the main window."""

        self.app.exec()



class HomePage:
    """Home screen of the application where users can navigate to main features."""

    def __init__(self, app: MainWindow):

        self.app = app
        self.page = QWidget()

        self.app.register("Homepage", self.page)

        self._build()

    def _build(self):
        """Build and arrange all UI components of the homepage."""

        self.base_layout = QVBoxLayout()
        self.page.setLayout(self.base_layout)

        # Header
        label_topic = QLabel("Task Manager")
        label_topic.setStyleSheet(style_topic_label)
        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)

        # Workspace     
        self.workspace_layout = QHBoxLayout()
        self.base_layout.addLayout(self.workspace_layout)

        self.sidebar = SideBar(self)
        self.content = Content(self)

        # Footer       
        label_footer = QLabel("Task manager | V1.0.0")
        label_footer.setStyleSheet(style_footer_label)
        self.base_layout.addWidget(label_footer, alignment = Qt.AlignLeft | Qt.AlignBottom)


class SideBar:
    """Navigation sidebar used to switch between content pages."""

    def __init__(self, page: HomePage):

        self.page = page
        
        self.sidebar_widget = QWidget()

        self.sidebar_widget.setStyleSheet(style_sidebar)
        self.sidebar_widget.setFixedWidth(250)

        # Add sidebar to the workspace area
        self.page.workspace_layout.addWidget(self.sidebar_widget)
        
        self.base_layout = QVBoxLayout()
        self.sidebar_widget.setLayout(self.base_layout)
        
        # Navigation buttons
        btn_dashboard = QPushButton("Dashboard")
        self.base_layout.addWidget(btn_dashboard)
        btn_dashboard.clicked.connect(
            lambda: self.page.content.go_content("Dashboard")
        )

        btn_tasks = QPushButton("Tasks")
        self.base_layout.addWidget(btn_tasks)
        btn_tasks.clicked.connect(
            lambda: self.page.content.go_content("Tasks")
        )

        btn_add_task= QPushButton("Add task")
        self.base_layout.addWidget(btn_add_task)
        btn_add_task.clicked.connect(
            lambda: self.page.content.go_content("AddTask")
        )

        btn_edit_task = QPushButton("Edit task")
        self.base_layout.addWidget(btn_edit_task)
        btn_edit_task.clicked.connect(
            lambda: self.page.content.go_content("EditTask")
        )

        # Apply a unified style to all sidebar buttons
        btn_dashboard.setStyleSheet(style_button)
        btn_tasks.setStyleSheet(style_button)
        btn_add_task.setStyleSheet(style_button)
        btn_edit_task.setStyleSheet(style_button)



class Content:
    """Manages all content pages displayed in the workspace area."""

    def __init__(self, page: HomePage):

        self.page = page

        self.stack_content = QStackedWidget()
        self.page.workspace_layout.addWidget(self.stack_content)

        self.content_views = {}

        # Register all available content pages
        DashboardPage(self)
        TasksPage(self)
        AddTaskPage(self)
        EditTaskPage(self)

    def register_content(self, name: str, content: QWidget):
        """Register a content page and add it to the stack."""

        self.content_views[name] = content
        self.stack_content.addWidget(content)

    def go_content(self, name: str):
        """Switch to a registered content page."""

        content = self.content_views.get(name)
        self.stack_content.setCurrentWidget(content)



class DashboardPage:
    """Dashboard view displayed in the content area."""

    def __init__(self, content: Content):

        self.content = content

        self.page = QWidget()
        self.page.setStyleSheet(style_content)

        # Register page
        self.content.register_content("Dashboard", self.page)

        self._build()

    def _build(self):
        """Dashboard UI components."""

        self.base_layout = QVBoxLayout()
        self.page.setLayout(self.base_layout)

        label_topic = QLabel("DashBoard")
        label_topic.setStyleSheet(style_label)

        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)



class TasksPage:
    """Task list view displayed in the content area."""

    def __init__(self, content: Content):

        self.content = content

        self.page = QWidget()
        self.page.setStyleSheet(style_content)

        # Register page
        self.content.register_content("Tasks", self.page)

        self._build()

    def _build(self):
        """Show tasks page UI components."""

        self.base_layout = QVBoxLayout()
        self.page.setLayout(self.base_layout)

        label_topic = QLabel("Tasks")
        label_topic.setStyleSheet(style_label)

        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)



class AddTaskPage:
    """Add task displayed in the content area."""

    def __init__(self, content: Content):

        self.content = content

        self.page = QWidget()
        self.page.setStyleSheet(style_content)

        # Register page
        self.content.register_content("AddTask", self.page)

        self._build()

    def _build(self):
        """Create task page UI components."""

        self.base_layout = QVBoxLayout()
        self.page.setLayout(self.base_layout)

        label_topic = QLabel("Add Task")
        label_topic.setStyleSheet(style_label)

        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)



class EditTaskPage:
    """Edit task displayed in the content area."""

    def __init__(self, content: Content):

        self.content = content

        self.page = QWidget()
        self.page.setStyleSheet(style_content)

        # Register page
        self.content.register_content("EditTask", self.page)

        self._build()

    def _build(self):
        """Edit task page UI components."""

        self.base_layout = QVBoxLayout()
        self.page.setLayout(self.base_layout)

        label_topic = QLabel("Edit Task")
        label_topic.setStyleSheet(style_label)

        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)



if __name__ == "__main__":
    app = MainWindow()
    app.run()