from model import Task, Database

from styles import (
    style_button_primary,
    style_form,
    style_messagebox,
)

from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QMessageBox,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QDateEdit,
)




class AddTaskPage(QWidget):
    """Add task displayed in the content area."""

    def __init__(self, content):
        super().__init__()

        self.content = content
        self.db = Database()

        self.setStyleSheet(style_form)

        # Register page in the content navigation system
        self.content.register_content("AddTask", self)

        self._setup_ui()

    def _setup_ui(self):
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


        self.btn_save.clicked.connect(self._save_task)

        self.base_layout.setContentsMargins(20, 20, 20, 20)

    def _save_task(self):
        """Collect form data and save a new task to the database."""

        title = self.title_box.text().strip()
        description = self.description_box.toPlainText().strip()
        due_date = self.date_box.date().toString("yyyy-MM-dd")

        try:
            task = Task(
                title = title, 
                description = description, 
                due_date = due_date
            )

            self.db.add_task(task)

            self._show_message(
                "Success",
                "Task saved successfuly."
            )
            self._clear_form()

            task_page = self.content.content_views["Tasks"]
            task_page.load_tasks()

        except Exception as e:

            self._show_message(
                "Error",
                f"failed to save task:\n{str(e)}",
                QMessageBox.Icon.Warning
            )

    def _clear_form(self):
        """Reset form fields after successful save."""

        self.title_box.clear()
        self.description_box.clear()

    def _show_message(self, title: str, text: str, icon = QMessageBox.Icon.Information):

        message = QMessageBox(self)
        message.setWindowTitle(title)
        message.setText(text)
        message.setIcon(icon)
        message.setStyleSheet(style_messagebox)
        message.exec()
