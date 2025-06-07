'''

import debug
import subjection
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

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = subjection.bot_token
LOG_FILE = subjection.log_file_name

def ensure_log_file():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("=== Telegram Chat Bot ===\n\n")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await debug.PrintLogOut("Бот запущен и готов записывать сообщения!")

async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.effective_user
        chat = update.effective_chat
        message = update.message
        

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
                
            debug.PrintLogOut(f"New Message  -  {log_entry[:100]}")

    except Exception as e:
        debug.PrintLogOut(f"Ошибка: {e}")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    debug.PrintLogOut(f"Ошибка в обработчике: {context.error}")

def main():
    ensure_log_file()

    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL, log_message))
    application.add_error_handler(error_handler)

    debug.PrintLogOut("Бот запускается...")
    application.run_polling(
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES,
        close_loop=False
    )
'''
import debug
import subjection
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
import threading
os.environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = subjection.bot_token
LOG_FILE = subjection.log_file_name

def ensure_log_file():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("=== Telegram Chat Bot ===\n\n")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await debug.PrintLogOut("Бот запущен и готов записывать сообщения!")

async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.effective_user
        chat = update.effective_chat
        message = update.message
        
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
                
            debug.PrintLogOut(f"New Message  -  {log_entry[:100]}")

    except Exception as e:
        debug.PrintLogOut(f"Ошибка: {e}")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    debug.PrintLogOut(f"Ошибка в обработчике: {context.error}")

def run_bot():
    ensure_log_file()

    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL, log_message))
    application.add_error_handler(error_handler)

    debug.PrintLogOut("Бот запускается...")
    application.run_polling(
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES,
        close_loop=False
    )

def main():
    # Создаем и запускаем поток с ботом
    run_bot()
    
    # Здесь можно добавить другой код, который будет выполняться параллельно с ботом
    
    # Ждем завершения потока с ботом (если нужно)

if __name__ == "__main__":
    main()