from aiogram.dispatcher.filters import Text
from database.models import Sections, Files
from handlers.command_handlers import cmd_start, cmd_help
from handlers.manual_handlers import get_manual, get_section, get_file
from aiogram import Dispatcher


async def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(cmd_help, commands="help")

    dp.register_message_handler(get_manual, Text(equals="Все разделы"))

    for section in await Sections.all():
        dp.register_callback_query_handler(get_section, Text(equals=section.dir_name))

    for file in await Files.all():
        dp.register_callback_query_handler(get_file, Text(equals=file.file_name))