from styles import (
    style_sidebar,
    style_topic_label,
    style_footer_label,
    style_button,
)

from content_pages import (
    DashboardPage,
    TasksPage,
    AddTaskPage,
    EditTaskPage
)

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QStackedWidget,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
)


class HomePage(QWidget):
    """Home screen of the application where users can navigate to main features."""

    def __init__(self, app):
        super().__init__()
        self.app = app

        self.app.register("Homepage", self)

        self._build()

    def _build(self):
        """Build and arrange all UI components of the homepage."""

        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)

        # Header
        label_topic = QLabel("Task Manager")
        label_topic.setStyleSheet(style_topic_label)
        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)
        label_topic.setContentsMargins(20, 20, 20, 20)

        # Workspace     
        self.workspace_layout = QHBoxLayout()
        self.base_layout.addLayout(self.workspace_layout)

        self.sidebar = SideBar(self)
        self.content = Content(self)

        # Footer       
        label_footer = QLabel("Task manager | V1.0.0")
        label_footer.setStyleSheet(style_footer_label)
        self.base_layout.addWidget(label_footer, alignment = Qt.AlignLeft | Qt.AlignBottom)



class SideBar(QWidget):
    """Navigation sidebar used to switch between content pages."""

    def __init__(self, page: HomePage):
        super().__init__()
        self.page = page

        self.setStyleSheet(style_sidebar)
        self.setFixedWidth(250)

        # Add sidebar to the workspace area
        self.page.workspace_layout.addWidget(self)
        
        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)
        
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

        self.base_layout.addStretch()
        self.base_layout.setSpacing(10)
        self.base_layout.setContentsMargins(12, 12, 12, 12)



class Content(QStackedWidget):
    """Manages all content pages displayed in the workspace area."""

    def __init__(self, page: HomePage):
        super().__init__()
        self.page = page
        self.page.workspace_layout.addWidget(self)

        self.content_views = {}

        # Register all available content pages
        DashboardPage(self)
        TasksPage(self)
        AddTaskPage(self)
        EditTaskPage(self)

    def register_content(self, name: str, content: QWidget):
        """Register a content page and add it to the stack."""

        self.content_views[name] = content
        self.addWidget(content)

    def go_content(self, name: str):
        """Switch to a registered content page."""

        content = self.content_views.get(name)
        self.setCurrentWidget(content)