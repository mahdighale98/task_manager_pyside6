from datetime import datetime

from pages.dashboard import DashboardPage
from pages.add_task_page import AddTaskPage
from pages.tasks_page import TasksPage
from pages.edit_task_page import EditTaskPage

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

        self._setup_layout()
        self._create_header()
        self._create_workspace()
        self._create_footer()

    def _setup_layout(self):
        """Build and arrange all UI components of the homepage."""

        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)

    def _create_header(self):
        "Create the page header containing the title and current date/time."

        self.header_layout = QHBoxLayout()
        self.header_layout.setSpacing(20)

        self.base_layout.addLayout(self.header_layout)

        self._create_datetime_section()
        self._label_title_label()
        
    def _create_datetime_section(self):
        """Create the date and time display section."""

        date_widget = QWidget()
        date_widget.setFixedWidth(250)

        date_layout = QVBoxLayout()
        date_widget.setLayout(date_layout)

        label_date = QLabel(datetime.now().strftime("%Y-%m-%d   %A"))
        label_time = QLabel(datetime.now().strftime("%H:%M"))

        label_date.setObjectName("datetime")
        label_time.setObjectName("datetime")

        date_layout.addWidget(label_date, alignment = Qt.AlignCenter)
        date_layout.addWidget(label_time, alignment = Qt.AlignCenter)

        self.header_layout.addWidget(date_widget)

    def _label_title_label(self):
        """Create and display the application title."""

        label_topic = QLabel("Task Manager")
        label_topic.setObjectName("title")

        label_topic.setContentsMargins(20, 20, 20, 20)

        self.header_layout.addWidget(label_topic, alignment = Qt.AlignCenter)

    def _create_workspace(self):
        "Create the central workspace containing the sidebar and the main content area."

        self.workspace_layout = QHBoxLayout()
        self.base_layout.addLayout(self.workspace_layout)

        self.sidebar = SideBar(self)
        self.content = Content(self)

    def _create_footer(self):
        "Create and display application information in the footer."

        label_footer = QLabel("Task manager | V1.0.0")
        label_footer.setObjectName("footer")

        self.base_layout.addWidget(label_footer, alignment = Qt.AlignLeft | Qt.AlignBottom)



class SideBar(QWidget):
    """Navigation sidebar used to switch between content pages."""

    def __init__(self, page: HomePage):
        super().__init__()

        self.setObjectName("sidebar")
        self.page = page

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

        self.base_layout.addStretch()
        self.base_layout.setSpacing(10)
        self.base_layout.setContentsMargins(12, 12, 12, 12)



class Content(QStackedWidget):
    """Manages all content pages displayed in the workspace area."""

    def __init__(self, page: HomePage):
        super().__init__()

        self.setObjectName("content")
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