from aiogram import types
from database.models import Sections, Files


async def get_manual_keyboard():
    manual_keyboard = types.InlineKeyboardMarkup()
    sections = await Sections.all()
    for section in sections:
        manual_keyboard.add(
            types.InlineKeyboardButton(
                text=section.name,
                callback_data=section.dir_name
            )
        )
    return manual_keyboard


async def get_files_by_section_id(sect_id):
    files_keyboard = types.InlineKeyboardMarkup()
    files = await Files.filter(section_id=sect_id)
    for file in files:
        files_keyboard.add(
            types.InlineKeyboardButton(
                text=file.name,
                callback_data=file.file_name
            )
        )
    return files_keyboard
