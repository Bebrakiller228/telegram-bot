from aiogram import Bot, Dispatcher, executor

API_TOKEN = '5980545857:AAG_72PB4c19KBLYkp6h58v7_ZC0irpYUJU'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def echo_handler(message):
    await message.answer(message.text)

async def start_handler(message):
    await message.answer('Привет, я люблю сосать..... чупачупс')


dp.register_message_handler(start_handler, commands=['start'])
dp.register_message_handler(echo_handler)

executor.start_polling(dp, skip_updates=True)



