# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.managment_db import *
import os

TOKEN = '5835174677:AAHYiuY8ElaECg7iOtVJePH1rM_-INSZ0qg'


async def on_startup(_):
    create_table('users', 'data/users.db')
    create_table('admin', 'data/admin.db')
    print('The bot was included.')


async def on_shutdown(dp):
    print('Удаляю базу данных')
    os.remove("data/admin.db")
    os.remove("data/users.db")
    await bot.close()
    await storage.close()


bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())
