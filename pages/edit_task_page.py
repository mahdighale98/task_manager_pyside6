from model import Task, Database

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)



class EditTaskPage(QWidget):
    """Edit task displayed in the content area."""

    def __init__(self, content):
        super().__init__()
        self.content = content

        # Register page
        self.content.register_content("EditTask", self)

        self._build()

    def _build(self):
        """Edit task page UI components."""

        self.base_layout = QVBoxLayout()
        self.setLayout(self.base_layout)

        label_topic = QLabel("Edit Task")

        self.base_layout.addWidget(label_topic, alignment = Qt.AlignCenter)
