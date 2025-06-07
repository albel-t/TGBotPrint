import debug
import chat_logger_bot
import short_test
import subjection

from PyQt6.QtWidgets import QApplication
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


translate_to_app = False

API_TOKEN = subjection.bot_token
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def run_external_function(message: types.Message):
    global translate_to_app
    # запуск приложения
    translate_to_app = True
    await message.answer("запущена трансляция")     

@dp.message()
async def echo(message: types.Message):
    global translate_to_app
    if translate_to_app:
        #вывод в приложение
    else:
        await message.answer(message.text)

if __name__ == '__main__':
    dp.run_polling(bot)
