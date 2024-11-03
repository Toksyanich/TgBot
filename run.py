import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.commands import register_commands
from handlers.messages import register_messages

bot = Bot(token=TOKEN)
dp = Dispatcher()


register_commands(dp)
register_messages(dp)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
