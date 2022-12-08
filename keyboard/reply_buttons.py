# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from aiogram.types import ReplyKeyboardMarkup


roles_for_user_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons = ('🥇Главный игрок',
           '🥈Второстепенный')
roles_for_user_button.row(*buttons)
