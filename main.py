import debug
import chat_logger_bot
import short_test
import chat_sercher
import subjection
import sys
from PyQt6.QtWidgets import QApplication
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Глобальные переменные
translate_to_app = False
app, overlay = chat_sercher.init()

API_TOKEN = subjection.bot_token
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def run_external_function(message: types.Message):
    global translate_to_app, app, overlay
    
    # Запуск приложения (если ещё не запущено)
    if not app:
        app = QApplication(sys.argv)
        overlay = chat_sercher.OverlayApp()
        overlay.show()
    
    translate_to_app = True
    await message.answer("Запущена трансляция в приложение")

@dp.message()
async def echo(message: types.Message):
    global translate_to_app, overlay
    
    if translate_to_app and overlay:
        overlay.add_message(message.text)  # Передача сообщения в приложение
    else:
        await message.answer(message.text)

if __name__ == '__main__':
    dp.run_polling(bot)