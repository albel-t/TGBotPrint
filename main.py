import debug
import chat_logger_bot
import short_test


import sys
import threading
from PyQt6.QtWidgets import QApplication


if __name__ == "__main__":



    chat_logger_bot.main()

    # Основной поток продолжает работать
    print("Основной поток бота продолжает работу")
    print("Поток бота завершил работу")
    