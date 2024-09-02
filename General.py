import asyncio
import logging
import sys
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot
import TOKEN
from Config import dp

async def on_startup(_):
    print('БОТ запущен!')

from Handlers import user

user.register_handler_user(dp)


async def main() -> None:
    bot = Bot(token=TOKEN.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())