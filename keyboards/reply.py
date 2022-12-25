from aiogram import types

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["Все разделы", "Пробные тесты"]
start_keyboard.add(*buttons)
buttons = ["Словарь терминов", "Документация по практике"]
start_keyboard.add(*buttons)