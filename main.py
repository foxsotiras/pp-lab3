import sys
from PySide6.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PaintZZZ")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            background-color: #fff;
            """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
