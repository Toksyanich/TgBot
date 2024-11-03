from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


async def cmd_start(message: Message):
    await message.answer("Вдоль ночных дорог")


async def cmd_help(message: Message):
    await message.answer("Помощи не будет")


def register_commands(dp: Dispatcher):
    dp.message.register(cmd_start, CommandStart())
    dp.message.register(cmd_help, Command('help'))
