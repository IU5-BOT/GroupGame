# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

from aiogram.utils import executor
from create_bot import dp, on_startup, on_shutdown
from aiogram import types


async def handler_start(message: types.Message):
    await message.answer('Привет!')


if __name__ == '__main__':
    from handlers import operations

    operations.register_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
