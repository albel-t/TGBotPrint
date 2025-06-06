import mcrcon
import subjection
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, 
                            QWidget, QPushButton, QScrollArea, QSpacerItem,
                            QSizePolicy)
from PyQt6.QtCore import Qt, QPoint, QTimer
from PyQt6.QtGui import QColor, QPainter, QPen, QBrush
import os
'''
RCON_IP = "26.70.9.233"
RCON_PASSWORD = subjection.account_password
RCON_PORT = int(subjection.debug_port)

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Window settings
        self.setWindowTitle("Text Display")
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(100, 100, 600, 100)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)
        
        # Scroll area for messages
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background: transparent; border: none;")
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Add spacer to push messages to bottom
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.scroll_layout.addItem(self.spacer)
        
        scroll.setWidget(scroll_content)
        self.main_layout.addWidget(scroll)
        
        # Close button
        close_btn = QPushButton("Close")
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
        self.main_layout.addWidget(close_btn)
        
        # File monitoring
        self.messages = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_file)
        self.timer.start(1000)  # Check every second
        
        # For window movement
        self.old_pos = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(30, 30, 30, 100)))
        painter.setPen(QPen(QColor(100, 100, 100, 1), 2))
        painter.drawRoundedRect(self.rect(), 10, 10)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
            
    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()

    def check_file(self):
        try:
            # Read from file
            with open('telegram_chat_log.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # If file has content
            if lines:
                # Clear the file
                with open('telegram_chat_log.txt', 'w', encoding='utf-8') as f:
                    pass
                
                # Add new messages
                for line in lines:
                    line = line.strip()
                    if line:  # Only process non-empty lines
                        self.add_message(line)
        except FileNotFoundError:
            print("Messages file not found")
        except Exception as e:
            print(f"Error reading file: {e}")

    def add_message(self, text):
        # Create message label
        label = QLabel(text)
        label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;
                background-color: rgba(50, 50, 50, 60);
                padding: 8px;
                margin: 2px;
                border-radius: 5px;
            }
        """)
        label.setWordWrap(True)
        
        # Insert new message above the spacer (at the bottom of existing messages)
        self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, label)
        self.messages.append(label)
        
        # Set timer to remove after 30 seconds
        QTimer.singleShot(10000, lambda: self.remove_message(label))
        
        # Limit number of messages (optional)
        if len(self.messages) > 10:  # Keep last 10 messages
            old_label = self.messages.pop(0)
            old_label.deleteLater()

    def remove_message(self, label):
        if label in self.messages:
            self.messages.remove(label)
            label.deleteLater()




if __name__ == "__main__":
    app = QApplication([])
    
    window = TransparentWindow()
    window.show()
    
    app.exec()
'''

import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, 
                            QWidget, QPushButton, QScrollArea, QSpacerItem,
                            QSizePolicy)
from PyQt6.QtCore import Qt, QPoint, QTimer, QThread, pyqtSignal
from PyQt6.QtGui import QColor, QPainter, QPen, QBrush
import os

# Ваши импорты (замените на реальные)
import mcrcon
import subjection

RCON_IP = "26.70.9.233"
RCON_PASSWORD = subjection.account_password
RCON_PORT = int(subjection.debug_port)

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
            
        # Window settings
        self.setWindowTitle("Text Display")
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(100, 100, 600, 100)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)
        
        # Scroll area for messages
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background: transparent; border: none;")
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Add spacer to push messages to bottom
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.scroll_layout.addItem(self.spacer)
        
        scroll.setWidget(scroll_content)
        self.main_layout.addWidget(scroll)
        
        # Close button
        close_btn = QPushButton("Close")
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
        self.main_layout.addWidget(close_btn)
        
        # File monitoring
        self.messages = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_file)
        self.timer.start(1000)  # Check every second
        
        # For window movement
        self.old_pos = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(30, 30, 30, 100)))
        painter.setPen(QPen(QColor(100, 100, 100, 1), 2))
        painter.drawRoundedRect(self.rect(), 10, 10)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
            
    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()

    def check_file(self):
        try:
            # Read from file
            with open('telegram_chat_log.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # If file has content
            if lines:
                # Clear the file
                with open('telegram_chat_log.txt', 'w', encoding='utf-8') as f:
                    pass
                
                # Add new messages
                for line in lines:
                    line = line.strip()
                    if line:  # Only process non-empty lines
                        self.add_message(line)
        except FileNotFoundError:
            print("Messages file not found")
        except Exception as e:
            print(f"Error reading file: {e}")

    def add_message(self, text):
        # Create message label
        label = QLabel(text)
        label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;
                background-color: rgba(50, 50, 50, 60);
                padding: 8px;
                margin: 2px;
                border-radius: 5px;
            }
        """)
        label.setWordWrap(True)
        
        # Insert new message above the spacer (at the bottom of existing messages)
        self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, label)
        self.messages.append(label)
        
        # Set timer to remove after 30 seconds
        QTimer.singleShot(10000, lambda: self.remove_message(label))
        
        # Limit number of messages (optional)
        if len(self.messages) > 10:  # Keep last 10 messages
            old_label = self.messages.pop(0)
            old_label.deleteLater()

    def remove_message(self, label):
        if label in self.messages:
            self.messages.remove(label)
            label.deleteLater()

class WindowThread(QThread):
    # Сигнал для создания окна (должен выполняться в основном потоке)
    create_window_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.window = None
        self.create_window_signal.connect(self.create_window)

    def run(self):
        print("[Поток] Запуск потока с окном")
        self.create_window_signal.emit()  # Создаем окно через сигнал
        self.exec()  # Запускаем цикл событий потока

    def create_window(self):
        # Этот метод вызывается в основном потоке
        self.window = TransparentWindow()
        self.window.show()
        print("[Поток] Окно создано")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Запускаем окно в отдельном потоке
    thread = WindowThread()
    thread.start()
    app.exec()
    # Основной код выполняется сразу после запуска потока
    print("Привет, консоль! Основной код работает параллельно с окном.")
    i = 1
    while i < 2:
        print("Работаю...")
        QTimer.singleShot(1000, lambda: None)  # Не блокировать цикл событий

   