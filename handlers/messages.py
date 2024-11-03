from aiogram import Dispatcher, F
# from aiogram.filters import F
from aiogram.types import Message


async def hay_bro(message: Message):
    await message.answer("loh")


def register_messages(dp: Dispatcher):
    dp.message.register(hay_bro, F.text == 'Как дела?')
