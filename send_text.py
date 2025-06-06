import mcrcon
import subjection

RCON_IP = "26.70.9.233"
RCON_PASSWORD = subjection.account_password
RCON_PORT = int(subjection.debug_port)

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QColor, QPainter, QPen, QBrush

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Настройки основного окна
        self.setWindowTitle("Прозрачное окно")
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Размеры и положение
        self.setGeometry(100, 100, 600, 20)
        
        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Вертикальный layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Добавляем элементы интерфейса
        self.label = QLabel("Это прозрачное окно!")
        self.label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 16px;
                background-color: rgba(50, 50, 50, 50);
                padding: 10px;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.label)
        
        # Кнопка закрытия
        close_btn = QPushButton("Закрыть")
        close_btn.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: rgba(100, 50, 50, 1);
                padding: 5px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: rgba(230, 70, 70, 1);
            }
        """)
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        
        # Для перемещения окна
        self.old_pos = None

    # Рисуем прозрачное окно с рамкой
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Полупрозрачный фон
        painter.setBrush(QBrush(QColor(30, 30, 30, 10)))
        painter.setPen(QPen(QColor(100, 100, 100, 1), 2))
        painter.drawRoundedRect(self.rect(), 10, 10)
        
    # Перемещение окна
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
            
    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()

if __name__ == "__main__":
    app = QApplication([])
    
    window = TransparentWindow()
    window.show()
    
    app.exec()