import window
import chat_logger_bot
import short_test


import sys
import threading
from PyQt6.QtWidgets import QApplication

def run_gui():
    app = short_test.QApplication(sys.argv)
    mainwindow = short_test.TransparentWindow()
    mainwindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    # Запускаем GUI в отдельном потоке
    #gui_thread = threading.Thread(target=run_gui, daemon=True)
    #gui_thread.start()
    
    # Основной код бота
    try:
        chat_logger_bot.main()
    except KeyboardInterrupt:
        # Нужно использовать сигналы Qt для безопасного обновления UI из другого потока
        window.PrintLogOut("Бот остановлен пользователем")
    except Exception as e:
        window.PrintLogOut(f"Фатальная ошибка: {e}")
    finally:
        window.PrintLogOut("Работа завершена")
    