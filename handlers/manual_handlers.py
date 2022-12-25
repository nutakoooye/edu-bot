from pathlib import Path

from aiogram import types
import aiofiles
from keyboards import get_manual_keyboard, get_files_by_section_id
from database.models import Sections, Files


async def get_manual(message: types.Message):
    markup = await get_manual_keyboard()
    await message.answer("Содержание по разделам:", reply_markup=markup)


async def get_section(call: types.CallbackQuery):
    section = await Sections.get(dir_name=call.data)
    files_keyboard = await get_files_by_section_id(section.id)
    await call.message.answer(section.name, reply_markup=files_keyboard)


async def get_file(call: types.CallbackQuery):
    file = await Files.get(file_name=call.data).prefetch_related('section')
    section_dir_name = file.section.dir_name
    path = Path("static", "manual", section_dir_name, file.file_name)
    async with aiofiles.open(path, mode='rb') as f:
        await call.message.answer_document(f)
