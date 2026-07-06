DARK_THEME = """
/* ===================== Base ===================== */

QMainWindow,
#mainArea {
    background-color: #0F172A;
}

QWidget {
    background: transparent;
    color: #E2E8F0;
    font-family: "Segoe UI";
    font-size: 14px;
}

/* ===================== Containers ===================== */

#sidebar {
    background: #111827;
    border: 1px solid #334155;
    border-radius: 16px;
}

#content {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 16px;
}

/* ===================== Labels ===================== */

QLabel {
    color: #E2E8F0;
    border: none;
}

QLabel#title {
    font-size: 34px;
    font-weight: 700;
    color: #FFFFFF;
}

QLabel#footer {
    font-size: 11px;
    color: #94A3B8;
}

QLabel#datetime {
    background: #111827;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 6px 12px;
    font-weight: 600;
}

QLabel#datetime:hover {
    border-color: #6366F1;
}

/* ===================== Menu ===================== */

QMenuBar {
    background: #111827;
    border-bottom: 1px solid #334155;
}

QMenuBar::item {
    padding: 8px 12px;
    border-radius: 6px;
}

QMenuBar::item:selected {
    background: #1E293B;
}

QMenu {
    background: #111827;
    border: 1px solid #334155;
    border-radius: 10px;
}

QMenu::item {
    padding: 8px 20px;
    border-radius: 6px;
}

QMenu::item:selected {
    background: #6366F1;
    color: white;
}

/* ===================== Buttons ===================== */

QPushButton {
    background: #1E293B;
    color: #E2E8F0;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 10px 16px;
    font-weight: 600;
}

QPushButton:hover {
    background: #273449;
    border-color: #475569;
}

QPushButton:pressed {
    background: #172033;
}

QPushButton#primary {
    background: #6366F1;
    color: white;
    border: none;
}

QPushButton#primary:hover {
    background: #4F46E5;
}

QPushButton#primary:pressed {
    background: #4338CA;
}

/* ===================== Inputs ===================== */

QLineEdit,
QTextEdit,
QDateEdit,
QComboBox {
    background: #111827;
    color: #F8FAFC;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 10px 12px;
}

QLineEdit:hover,
QTextEdit:hover,
QDateEdit:hover,
QComboBox:hover {
    border-color: #475569;
}

QLineEdit:focus,
QTextEdit:focus,
QDateEdit:focus,
QComboBox:focus {
    border: 1px solid #6366F1;
}

/* ===================== Table ===================== */

QTableWidget {
    background: #111827;
    color: #E2E8F0;
    border: 1px solid #334155;
    border-radius: 12px;
    gridline-color: transparent;
    selection-background-color: #6366F1;
}

QHeaderView::section {
    background: #1E293B;
    color: #F8FAFC;
    border: none;
    border-bottom: 1px solid #334155;
    padding: 10px;
    font-weight: 600;
}

QTableCornerButton::section {
    background: #1E293B;
    border: none;
}

/* ===================== ScrollBar ===================== */

QScrollBar:vertical {
    background: transparent;
    width: 10px;
}

QScrollBar:horizontal {
    background: transparent;
    height: 10px;
}

QScrollBar::handle {
    background: #475569;
    border-radius: 5px;
}

QScrollBar::handle:hover {
    background: #64748B;
}

QScrollBar::add-line,
QScrollBar::sub-line,
QScrollBar::add-page,
QScrollBar::sub-page {
    background: none;
    border: none;
}

/* ===================== MessageBox ===================== */

QMessageBox {
    background: #0F172A;
}

QMessageBox QLabel {
    color: #E2E8F0;
}

QMessageBox QPushButton {
    min-width: 90px;
}
"""


LIGHT_THEME = """
/* ===================== Base ===================== */

QMainWindow,
#mainArea {
    background-color: #F8FAFC;
}

QWidget {
    background: transparent;
    color: #0F172A;
    font-family: "Segoe UI";
    font-size: 14px;
}

/* ===================== Containers ===================== */

#sidebar {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
}

#content {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
}

/* ===================== Labels ===================== */

QLabel {
    color: #0F172A;
    border: none;
}

QLabel#title {
    font-size: 34px;
    font-weight: 700;
    color: #0F172A;
}

QLabel#footer {
    font-size: 11px;
    color: #64748B;
}

QLabel#datetime {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 6px 12px;
    font-weight: 600;
}

QLabel#datetime:hover {
    border-color: #6366F1;
}

/* ===================== Menu ===================== */

QMenuBar {
    background: #FFFFFF;
    border-bottom: 1px solid #E2E8F0;
}

QMenuBar::item {
    padding: 8px 12px;
    border-radius: 6px;
}

QMenuBar::item:selected {
    background: #EEF2FF;
}

QMenu {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
}

QMenu::item {
    padding: 8px 20px;
    border-radius: 6px;
}

QMenu::item:selected {
    background: #6366F1;
    color: white;
}

/* ===================== Buttons ===================== */

QPushButton {
    background: white;
    color: #334155;
    border: 1px solid #CBD5E1;
    border-radius: 10px;
    padding: 10px 16px;
    font-weight: 600;
}

QPushButton:hover {
    background: #F8FAFC;
    border-color: #94A3B8;
}

QPushButton:pressed {
    background: #F1F5F9;
}

QPushButton#primary {
    background: #6366F1;
    color: white;
    border: none;
}

QPushButton#primary:hover {
    background: #4F46E5;
}

QPushButton#primary:pressed {
    background: #4338CA;
}

/* ===================== Inputs ===================== */

QLineEdit,
QTextEdit,
QDateEdit,
QComboBox {
    background: white;
    color: #0F172A;
    border: 1px solid #CBD5E1;
    border-radius: 10px;
    padding: 10px 12px;
}

QLineEdit:hover,
QTextEdit:hover,
QDateEdit:hover,
QComboBox:hover {
    border-color: #94A3B8;
}

QLineEdit:focus,
QTextEdit:focus,
QDateEdit:focus,
QComboBox:focus {
    border: 1px solid #6366F1;
}

/* ===================== Table ===================== */

QTableWidget {
    background: white;
    color: #0F172A;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    gridline-color: transparent;
    selection-background-color: #6366F1;
}

QHeaderView::section {
    background: #F8FAFC;
    color: #0F172A;
    border: none;
    border-bottom: 1px solid #E2E8F0;
    padding: 10px;
    font-weight: 600;
}

QTableCornerButton::section {
    background: #F8FAFC;
    border: none;
}

/* ===================== ScrollBar ===================== */

QScrollBar:vertical {
    background: transparent;
    width: 10px;
}

QScrollBar:horizontal {
    background: transparent;
    height: 10px;
}

QScrollBar::handle {
    background: #CBD5E1;
    border-radius: 5px;
}

QScrollBar::handle:hover {
    background: #94A3B8;
}

QScrollBar::add-line,
QScrollBar::sub-line,
QScrollBar::add-page,
QScrollBar::sub-page {
    background: none;
    border: none;
}

/* ===================== MessageBox ===================== */

QMessageBox {
    background: #F8FAFC;
}

QMessageBox QLabel {
    color: #0F172A;
}

QMessageBox QPushButton {
    min-width: 90px;
}
"""