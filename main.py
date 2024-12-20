import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtGui import QPainter, QColor, QMouseEvent
from PySide6.QtCore import Qt

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.last_point = None
        self.current_point = None
        self.lines = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(QColor(0, 0, 0))
        for line in self.lines:
            painter.drawLine(line[0], line[1])

        if self.last_point and self.current_point:
            painter.drawLine(self.last_point, self.current_point)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_point = event.position().toPoint()
            self.current_point = self.last_point
            

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.current_point = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.lines.append((self.last_point, self.current_point))
            self.last_point = None
            self.current_point = None
            self.update()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PaintZZZ")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            background-color: #fff;
            """)

        self.drawing_widget = DrawingWidget()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.drawing_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
