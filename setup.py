from os import environ
from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tortoise import run_async
from database import init
from handlers import register_all_handlers


# from bot.database.models import register_models


async def __on_start_up(dp: Dispatcher) -> None:
    # register_all_filters(dp)
    await register_all_handlers(dp)
    # await init()
    # register_models()


TOKEN = environ.get("TOKEN")


def start_bot():
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    run_async(init())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
