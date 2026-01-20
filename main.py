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
        "New members are onboarded individually. This allows us to maintain a high "
        "standard of quality, a personal approach, and a comfortable format for every participant.\n\n"
        "As soon as a spot becomes available, I will send you a personal instruction.\n\n"
        "If joining without waiting is important to you, feel free to message me directly.\n\n"
        "We will briefly discuss your goals and see whether the private channel format "
        "is a good fit for you."
    )

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
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

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
