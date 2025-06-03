import asyncio
import window
import subjection
import random
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    filters,
    ContextTypes,
    CommandHandler,
)
import datetime
import os
import logging

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = subjection.bot_token  # Ваш токен
LOG_FILE = subjection.log_file_name

def ensure_log_file():
    """Создает файл лога при первом запуске"""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("=== Telegram Chat Bot ===\n\n")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    await window.PrintLogOut("Бот запущен и готов записывать сообщения!")

async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Записывает все сообщения в лог-файл"""
    try:
        user = update.effective_user
        chat = update.effective_chat
        message = update.message
        

        #window.PrintLogOut(f"Получено сообщение в чате {chat.id} от {user.first_name}")

        # Записываем разные типы сообщений
        if message.text:
            content = message.text
        elif message.caption:
            content = f"[MEDIA] {message.caption}"
        else:
            content = "[NON-TEXT CONTENT]"
        if (content[0] != ".") and ((chat.title or 'private') in subjection.active_chats):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp[11:16]}] {subjection.names[user.first_name]}: {content}\n"

            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_entry)
                
            window.PrintLogOut(f"New Message  -  {log_entry[:100]}")

    except Exception as e:
        window.PrintLogOut(f"Ошибка: {e}")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик ошибок"""
    window.PrintLogOut(f"Ошибка в обработчике: {context.error}")

def main():
    ensure_log_file()

    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL, log_message))
    application.add_error_handler(error_handler)

    window.PrintLogOut("Бот запускается...")
    application.run_polling(
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES,
        close_loop=False
    )

