from aiogram import types
from keyboards import start_keyboard

async def cmd_start(message: types.Message):
    await message.reply("Здесь будет какое-то стартовое описание возможностей бота", reply_markup=start_keyboard)

async def cmd_help(message: types.Message):
    await message.reply("Здесь будет инструкция для общения с ботом если у пользователя возникли проблемы", reply_markup=start_keyboard)