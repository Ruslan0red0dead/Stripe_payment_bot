from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pay_method import payment_details
from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from config import TOKEN
import logging
import asyncio
import sys

dp = Dispatcher()

# card: https://docs.stripe.com/testing#cards

@dp.message(Command('start'))
async def start_bot(message: Message):
    await message.reply("Please enter /pay")

@dp.message(Command('pay'))
async def process_payment(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Payment.", url=payment_details())]
        ])

    try:
        await message.reply(f"Click the button to proceed to payment",reply_markup=keyboard)
    except Exception as e:
        await message.reply(f"Error creating a session")
        # await message.reply(f"Error creating a session: {str(e)}")

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())