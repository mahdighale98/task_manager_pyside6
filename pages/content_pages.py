from model import Task, Database

from styles import (
    style_content,
    style_label,
    style_button_primary,
    style_form
)

from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QDateEdit
)



class DashboardPage(QWidget):
    """Dashboard view displayed in the content area."""

    def __init__(self, content):
        super().__init__()
        self.content = content

        self.setStyleSheet(style_content)

        # Register page
        self.content.register_content("Dashboard", self)

        self._build()

    def _build(self):
        """Dashboard UI components."""

        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)

        label_topic = QLabel("DashBoard")
        label_topic.setStyleSheet(style_label)

        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)



class TasksPage(QWidget):
    """Task list view displayed in the content area."""

    def __init__(self, content):
        super().__init__()
        self.content = content

        self.setStyleSheet(style_content)

        # Register page
        self.content.register_content("Tasks", self)

        self._build()

    def _build(self):
        """Show tasks page UI components."""

        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)

        label_topic = QLabel("Tasks")
        label_topic.setStyleSheet(style_label)

        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)



class AddTaskPage(QWidget):
    """Add task displayed in the content area."""

    def __init__(self, content):
        super().__init__()

        self.content = content
        self.db = Database()

        self.setStyleSheet(style_form)

        # Register page in the content navigation system
        self.content.register_content("AddTask", self)

        self._build()

    def _build(self):
        """Create task page UI components."""

        # Main layout
        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)

        #Form layout
        self.form_layout = QFormLayout()
        self.base_layout.addLayout(self.form_layout)

        # Form field
        self.title_box = QLineEdit()
        self.description_box = QTextEdit()
        self.date_box = QDateEdit()

        self.date_box.setDisplayFormat("yyyy-MM-dd")
        self.date_box.setFixedWidth(150)
        
        # Prevent selecting dates earlier than today
        self.date_box.setDate(QDate.currentDate())
        self.date_box.setMinimumDate(QDate.currentDate())

        # Add fields to form
        self.form_layout.addRow("Title:", self.title_box)
        self.form_layout.addRow("Description:", self.description_box)
        self.form_layout.addRow("Due date:", self.date_box)

        # Save button
        self.btn_save = QPushButton("Save")
        self.btn_save.setStyleSheet(style_button_primary)
        self.base_layout.addWidget(self.btn_save)


        self.btn_save.clicked.connect(self._save_task())

        self.base_layout.setContentsMargins(20, 20, 20, 20)

    def _save_task(self):
        """Collect form data and save a new task to the database."""

        title = self.title_box.text().strip()
        description = self.description_box.toPlainText().strip()
        due_date = self.date_box.date().toString("yyyy-MM-dd")

        task = Task(
            title = title, 
            description = description, 
            due_date = due_date
        )

        self.db.add_task(task)
        self._clear_form()

    def _clear_form(self):
        """Reset form fields after successful save."""

        self.title_box.clear()
        self.description_box.clear()
        self.date_box.clear()


class EditTaskPage(QWidget):
    """Edit task displayed in the content area."""

    def __init__(self, content):
        super().__init__()
        self.content = content
        
        self.setStyleSheet(style_content)

        # Register page
        self.content.register_content("EditTask", self)

        self._build()

    def _build(self):
        """Edit task page UI components."""

        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)

        label_topic = QLabel("Edit Task")
        label_topic.setStyleSheet(style_label)

        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)
