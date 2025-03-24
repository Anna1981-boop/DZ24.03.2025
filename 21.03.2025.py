import logging
import asyncio
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters.command import Command
from pulse import pl
from sait import card
from random import randint
from aiogram import Bot, Dispatcher

API_TOKEN = '7966477536:AAFj6TCeCEmNSr87fPq2pfpzFVuIdWkO-50'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ EchoBot!", reply_markup=pl)

@dp.message(Command("info"))
async def send_info(message: types.Message):
    await message.reply_dice(emoji='🎲')

@dp.message(Command("user"))
async def send_user(message: types.Message):
    await message.reply("Случайности не случайны!😉")

@dp.message(Command("close"))
async def send_close(message: types.Message):
    await message.reply("До встречи!")

@dp.message(Command("stop"))
async def send_stop(message: types.Message):
    await message.reply("Стоп!")

@dp.message(Command("open"))
async def send_open(message: types.Message):
    img_card = card()
    await message.reply("выбирай карточку")
    await message.reply_photo(photo=img_card)

@dp.message(F.text == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}")
    

#Хендлер на сообщения
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'Привет' in msg_user:
        await message.reply("Хеллоу!")
    elif 'Пока' == msg_user:
        await message.reply("гудбай!")
    else:
        await message.reply("давай поговорим")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())