from aiogram import types


button1 = types.KeyboardButton(text = '/start')
button2 = types.KeyboardButton(text = '/info')
button3 = types.KeyboardButton(text = '/stop')
button4 = types.KeyboardButton(text = '/close')
button5 = types.KeyboardButton(text = '/open')
button6 = types.KeyboardButton(text = '/num')

keyboard1 = [
    [button1, button2, button3],
    [button4, button5, button6],
]

pl = types.ReplyKeyboardMarkup(keyboard = keyboard1, resize_keyboard=True)