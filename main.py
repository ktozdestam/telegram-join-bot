import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.chat_join_request_handler()
async def on_join_request(join_request: types.ChatJoinRequest):
    user = join_request.from_user

    message_text = (
        "Hello!\n\n"
        "Thank you for your interest in the private channel *Satoshi Insights*.\n\n"
        "New members are onboarded individually.\n\n"
        "I will contact you personally."
    )

    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="💬 Message directly",
            url="https://t.me/InsightsBySatoshi"
        )
    )

    try:
        await bot.send_message(
            user.id,
            message_text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )
    except Exception as e:
        print(e)

if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
