import window
import chat_logger_bot


if __name__ == "__main__":
    try:
        chat_logger_bot.main()
    except KeyboardInterrupt:
        window.PrintLogOut("Бот остановлен пользователем")
    except Exception as e:
        window.PrintLogOut(f"Фатальная ошибка: {e}")
    finally:
        window.PrintLogOut("Работа завершена")