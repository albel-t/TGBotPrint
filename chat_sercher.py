import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QPoint, QEvent
from PyQt6.QtGui import QColor, QPainter, QFont, QCursor

class OverlayApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.add_message("init")
        self.add_message("init")
        self.add_message("init")
        self.drag_pos = None  # Для перемещения окна

    def setup_ui(self):
        # Настройка окна
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(100, 100, 300, 500)

        # Стиль и прозрачность
        self.setStyleSheet("""
            background-color: rgba(80, 80, 80, 180); 
            border-radius: 10px;
        """)

        # Основной layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.setLayout(layout)

        # Кнопка закрытия
        self.close_btn = QPushButton("×")
        self.close_btn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 18px;
                border: none;
                background-color: transparent;
            }
            QPushButton:hover { color: red; }
        """)
        self.close_btn.setFixedSize(30, 30)
        self.close_btn.clicked.connect(self.close)
        layout.addWidget(self.close_btn, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        self.message_layout = layout

    def mousePressEvent(self, event):
        """Захват позиции при нажатии мыши"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()
            self.setCursor(QCursor(Qt.CursorShape.ClosedHandCursor))
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """Перемещение окна"""
        if self.drag_pos:
            delta = event.globalPosition().toPoint() - self.drag_pos
            self.move(self.pos() + delta)
            self.drag_pos = event.globalPosition().toPoint()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """Сброс при отпускании мыши"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = None
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        super().mouseReleaseEvent(event)

    def add_message(self, text: str):
        label = QLabel(text)
        label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: rgba(0, 0, 0, 100);
                padding: 8px;
                border-radius: 5px;
                margin: 5px;
            }
        """)
        label.setWordWrap(True)
        label.setFont(QFont("Arial", 10))
        self.message_layout.insertWidget(1, label)
        QTimer.singleShot(20, lambda: self.fade_out(label))

    def fade_out(self, widget):
        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(10)
        animation.setStartValue(1.0)
        animation.setEndValue(0.0)
        animation.finished.connect(widget.deleteLater)
        animation.start()

def init():
    app = QApplication(sys.argv)
    overlay = OverlayApp()
    return app, overlay

if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = OverlayApp()
    overlay.show()
    sys.exit(app.exec())