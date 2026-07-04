from model import Task, Database

from styles import (
    style_content,
    style_label,
)

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
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
