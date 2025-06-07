import debug
import chat_logger_bot
import short_test


import sys
import threading
from PyQt6.QtWidgets import QApplication


if __name__ == "__main__":
    # Запускаем GUI в отдельном потоке
    #gui_thread = threading.Thread(target=run_gui, daemon=True)
    #gui_thread.start()
    
    # Основной код бота
    import threading



    # Создание и запуск потока
    thread = threading.Thread(target=chat_logger_bot.main)
    thread.start()

    # Основной поток продолжает работать
    print("Основной поток бота продолжает работу")
    app = short_test.QApplication(sys.argv)
    mainwindow = short_test.TransparentWindow()
    mainwindow.show()
    app.exec()

    # Ожидание завершения потока (опционально)
    thread.join()
    print("Поток бота завершил работу")
    