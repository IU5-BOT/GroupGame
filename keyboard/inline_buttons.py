# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_users_inline = InlineKeyboardMarkup(resize_keyboard=True)
buttons = (
    ('🥇Главный игрок', 'main_person'),
    ('🥈Второстепенный', 'minor_player'),
)
button_users_inline.row(*(InlineKeyboardButton(text, callback_data=data) for text, data in buttons))
