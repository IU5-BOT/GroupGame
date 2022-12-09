# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_stop_inline = InlineKeyboardMarkup(resize_keyboard=True)
button_stop_inline.row(InlineKeyboardButton('✋Stop', callback_data='stop'))

new_game = InlineKeyboardMarkup(resize_keyboard=True)
new_game.row(InlineKeyboardButton('🆕Новая игра', callback_data='/new_game'))
