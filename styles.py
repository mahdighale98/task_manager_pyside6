# =========================
# App Background
# =========================
style_window = """
QMainWindow {
    background-color: #0a0f1f;
    color: #e5e7eb;
}

QWidget {
    color: #e5e7eb;
    background-color: transparent;
    font-family: "Segoe UI";
}

QMenuBar {
    background-color: #111827;
    color: #f9fafb;
    border-bottom: 1px solid #1f2937;
}

QMenuBar::item {
    background: transparent;
    padding: 8px 14px;
    margin: 2px;
    border-radius: 6px;
}

QMenuBar::item:selected {
    background-color: #1f2937;
}

QMenuBar::item:pressed {
    background-color: #2563eb;
}

QMenu {
    background-color: #111827;
    color: #f9fafb;

    border: 1px solid #1f2937;
    border-radius: 8px;

    padding: 4px;
}

QMenu::item {
    padding: 8px 24px;
    border-radius: 6px;
}

QMenu::item:selected {
    background-color: #2563eb;
    color: white;
}

QMenu::separator {
    height: 1px;
    background: #1f2937;
    margin: 4px 8px;
}

QToolTip {
    background-color: #111827;
    color: #f9fafb;
    border: 1px solid #1f2937;
    padding: 6px;
}

QScrollBar:vertical {
    background: #0b1220;
    width: 12px;
    border: none;
}

QScrollBar::handle:vertical {
    background: #374151;
    border-radius: 6px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: #4b5563;
}

QScrollBar:horizontal {
    background: #0b1220;
    height: 12px;
    border: none;
}

QScrollBar::handle:horizontal {
    background: #374151;
    border-radius: 6px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background: #4b5563;
}

QScrollBar::add-line,
QScrollBar::sub-line,
QScrollBar::add-page,
QScrollBar::sub-page {
    background: none;
    border: none;
}
"""

# =========================
# Widget style
# =========================
style_sidebar = """
QWidget {
    background-color: #0d1324;

    border: 1px solid #1a2235;
    border-radius: 14px;
}
"""
style_content = """
QWidget {
    background-color: #0e1528;

    border: 1px solid #1a2235;
    border-radius: 14px;
}
"""

# =========================
# Topic label
# =========================
style_topic_label = """
QLabel {
    font-family: "Segoe UI";
    font-size: 46px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.5px;
}
"""

# =========================
# Label
# =========================
style_label = """
QLabel {
    border: none;
    font-family: "Segoe UI";
    font-size: 16px;
    font-weight: 500;
    color: #e5e7eb;
}
"""

# =========================
# Footer label
# =========================
style_footer_label = """
QLabel {
    font-family: "Segoe UI";
    font-size: 11px;
    color: #6b7280;
}
"""

# =========================
# Qmessage
# =========================
style_messagebox = """
QMessageBox {
    background-color: #0a0f1f;
    border: 1px solid #1f2937;
    border-radius: 12px;
}

QMessageBox QLabel {
    color: #e5e7eb;
    font-family: "Segoe UI";
    font-size: 14px;

    padding: 8px 12px;
    min-width: 260px;
}

QMessageBox QPushButton {
    font-family: "Segoe UI";
    font-size: 13px;
    font-weight: 600;

    color: #d1d5db;
    background-color: #111827;

    border: 1px solid #1f2937;
    border-radius: 8px;

    min-width: 90px;
    padding: 8px 14px;
}

QMessageBox QPushButton:hover {
    background-color: #1f2937;
}

QMessageBox QPushButton:pressed {
    background-color: #0b1220;
}

QMessageBox QPushButton:focus {
    border: 1px solid #3b82f6;
}

QMessageBox QLabel#qt_msgbox_label {
    color: #e5e7eb;
}
"""
# =========================
# Primary Button
# =========================
style_button_primary = """
QPushButton {
    font-family: "Segoe UI";
    font-size: 15px;
    font-weight: 700;

    color: #ffffff;
    background-color: #2563eb;

    padding: 12px 18px;
    border-radius: 10px;
    border: none;
}

QPushButton:hover {
    background-color: #3b82f6;
}

QPushButton:pressed {
    background-color: #1d4ed8;
}

QPushButton:disabled {
    opacity: 0.4;
}
"""

# =========================
# Base Button
# =========================
style_button = """
QPushButton {
    font-family: "Segoe UI";
    font-size: 14px;
    font-weight: 600;

    color: #d1d5db;
    background-color: #111827;

    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid #1f2937;
}
QPushButton:hover {
    background-color: #1f2937;
}
QPushButton:pressed {
    background-color: #0b1220;
}
QPushButton:disabled {
    color: #6b7280;
}
"""

# =========================
# Form Layout
# =========================
style_form = """
QLabel {
    background: transparent;
    border: none;

    color: #e2e8f0;

    font-size: 14px;
    font-weight: 600;
}

/* Inputs */

QLineEdit,
QDateEdit,
QTextEdit {
    background-color: #131b2e;

    color: #f8fafc;

    border: 1px solid #25324a;
    border-radius: 12px;

    padding: 10px 14px;

    font-size: 14px;
}

/* Hover */

QLineEdit:hover,
QDateEdit:hover,
QTextEdit:hover {
    border: 1px solid #334155;
}

/* Focus */

QLineEdit:focus,
QDateEdit:focus,
QTextEdit:focus {
    border: 1px solid #3b82f6;
    background-color: #17233c;
}

/* Description */

QTextEdit {
    min-height: 120px;
}

/* Date */

QDateEdit {
    min-width: 140px;
}

/* Date buttons */

QDateEdit::up-button,
QDateEdit::down-button {
    width: 18px;

    background-color: #e2e8f0;

    border-left: 1px solid #25324a;
}

QDateEdit::up-button:hover,
QDateEdit::down-button:hover {
    background-color: #2563eb;
}
"""