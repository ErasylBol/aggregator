from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import asyncio

TOKEN = "8334922229:AAGSpWC78kpfltiu0i9qVHq8jTNRBjXWe34"

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🚀 Запустить агрегатор",
                web_app=WebAppInfo(url="https://erasylbol.github.io/aggregator/")
            )
        ],
        [
            KeyboardButton(text="ℹ️ Помощь")
        ]
    ],
    resize_keyboard=True
)

@dp.message()
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Привет! Это агрегатор ликвидности.\n\n"
        "Нажми кнопку ниже, чтобы открыть Mini App ⬇️",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
