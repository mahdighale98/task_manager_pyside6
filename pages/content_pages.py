from model import Task, Database

from styles import (
    style_content,
    style_label,
    style_button_primary,
    style_form,
    style_messagebox,
    style_table
)

from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QMessageBox,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QDateEdit,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
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
        self.db = Database()

        self.setStyleSheet(style_content)

        # Register page
        self.content.register_content("Tasks", self)

        self._build()

    def _build(self):
        """Create the page layout and load task data into the table."""

        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)
        
        self._create_table()
        self._setup_table_headers()
        self.load_tasks()


    def _create_table(self):
        """Initialize the QTableWidget used to display tasks."""

        self.tasks_table = QTableWidget()
        self.tasks_table.setStyleSheet(style_table)
        
        self.tasks_table.setShowGrid(False)
        self.tasks_table.setSortingEnabled(True)

        self.base_layout.addWidget(self.tasks_table)

    def _setup_table_headers(self):
        """Configure table headers, column sizing, and visibility settings."""

        self.tasks_table.setColumnCount(5)
        self.tasks_table.setHorizontalHeaderLabels(["ID", "Title", "Description", "Due date", "Status"])

        self.tasks_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tasks_table.verticalHeader().setDefaultSectionSize(50)
        self.tasks_table.setColumnHidden(0, True)

    def load_tasks(self):
        """Retrieve all tasks from the database and display them in the table."""

        self.tasks_table.setRowCount(0)
        
        tasks = self.db.show_tasks()

        for row, tasks in enumerate(tasks):

            self.tasks_table.insertRow(row)

            for column in range(4):

                self.tasks_table.setItem(row, column, self._create_item(tasks[column]))
                self.tasks_table.setItem(row, 4, self._create_status_item(tasks[4]))

        self.tasks_table.sortItems(3, Qt.AscendingOrder)

    def _create_item(self, status):
        """Return a centered table item for regular task fields."""

        item = QTableWidgetItem(status)
        item.setTextAlignment(Qt.AlignCenter)

        return item

    def _create_status_item (self, status):
        """Return a formatted status cell with colors based on task status."""

        status_item = QTableWidgetItem(status)
        status_item.setTextAlignment(Qt.AlignCenter)
        status_item.setForeground(QColor("#000000"))

        font = QFont()
        font.setPointSize(12)
        font.setBold(True)

        status_item.setFont(font)

        if status == "Not done":
            status_item.setBackground(QColor("#eab308"))
        elif status == "Done":
            status_item.setBackground(QColor("#16a34a"))
        else:
            status_item.setBackground(QColor("#dc2626"))

        return status_item



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
