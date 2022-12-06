# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from aiogram.types import ReplyKeyboardMarkup


# def get_data_for_button():
#     # users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
#     # buttons = (el[1] for el in get_all_users('data/users.db'))
#     # users_reply_buttons.row(*buttons)
#     return (el[1] for el in get_all_users('data/users.db'))


roles_for_user_button = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ('🥇Главный игрок',
           '🥈Второстепенный')
roles_for_user_button.row(*buttons)
