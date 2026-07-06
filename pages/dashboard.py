from model import Task, Database

from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QFrame,
    QVBoxLayout,
    QProgressBar,
    QLabel,
)



class DashboardPage(QWidget):
    """Dashboard view displayed in the content area."""

    def __init__(self, content):
        super().__init__()

        self.content = content
        self.db = Database()

        # Register page
        self.content.register_content("Dashboard", self)

        self._setup_layout()
        self._dashboard()

    def _setup_layout(self):

        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)

    def _today_task(self):

        self.db.cursor.execute("""SELECT id, title, due_date, status FROM tasks""")
        tasks = self.db.cursor.fetchall()

        total = 0
        done = 0

        today_date = date.today()
        today_tasks = []

        for task_id, title, due_date, status in tasks:

            due_date = date.fromisoformat(due_date)

            if due_date == today_date:

                total += 1
                today_tasks.append(title)

                if status == "Done":
                    done += 1

        return total, done, today_tasks
                
        
    def _dashboard(self):

        total, done, tasks = self._today_task()

        # ---------- Card 1: Progress ----------
        card1 = QFrame()
        card1.setObjectName("card")
        self.base_layout.addWidget(card1)

        layout1 = QVBoxLayout()
        card1.setLayout(layout1)

        title1 = QLabel("Today's Progress")
        title1.setObjectName("cardTitle")
        layout1.addWidget(title1, alignment = Qt.AlignCenter)

        value1 = QLabel(f"{done} / {total} Done")
        value1.setObjectName("cardValue")
        layout1.addWidget(value1, alignment = Qt.AlignCenter)

        # Progress Bar
        progress = QProgressBar()

        progress.setRange(0, total if total > 0 else 1)
        progress.setValue(done)
        
        layout1.addWidget(progress)

        # ---------- Card 2: Task List ----------
        card2 = QFrame()
        card2.setObjectName("card")
        self.base_layout.addWidget(card2)
        
        layout2 = QVBoxLayout()
        card2.setLayout(layout2)

        title2 = QLabel("Tasks List")
        title2.setObjectName("cardTitle")
        layout2.addWidget(title2, alignment = Qt.AlignCenter)

        if tasks:
            for t in tasks:
                item = QLabel("• " + t)
                item.setObjectName("taskItem")
                layout2.addWidget(item)
        else:
            empty = QLabel("No tasks for today")
            empty.setObjectName("taskItem")
            layout2.addWidget(empty)

        

        self.base_layout.setSpacing(20)
        