from model import Task, Database

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)






class TasksPage(QWidget):
    """Task list view displayed in the content area."""

    def __init__(self, content):
        super().__init__()

        self.content = content
        self.db = Database()

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