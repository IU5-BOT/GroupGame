# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as md
# from keyboards.menu_bts import start_markup
# from keyboards.search_ib import users_ib
from create_bot import dp
from data.managment_db import SQL
from keyboard.reply_buttons import users_reply_buttons, roles_for_user_button
import time

bd = SQL('users', 'data/users.bd')
bd_admin = SQL('admins', 'data/admins.bd')
ADMIN_CREATED: bool = False
ADMIN_FINISH_REPLY: bool = False
ADMIN_ID: int = -1


class FSMUsers(StatesGroup):
    user_role = State()
    question1 = State()
    question2 = State()
    question3 = State()


async def handler_start(message: types.Message):
    await message.answer('Привет, это жёская игра!')
    await FSMUsers.user_role.set()
    await message.answer("Выберите роль:", reply_markup=roles_for_user_button)


async def catch_user_role(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question1'] = message.text
        global ADMIN_CREATED, ADMIN_ID
        if message.text == '🥇Главный игрок' and not ADMIN_CREATED:
            ADMIN_CREATED = True
            ADMIN_ID = message.chat.id
            bd_admin.create_user_data(message.chat.id, message.chat.first_name)
            await message.answer('Вы главный игрок!')

        elif message.text == '🥇Главный игрок' and ADMIN_CREATED:
            bd.create_user_data(message.chat.id, message.chat.first_name)
            await message.answer('Главный игрок уже есть. Вы второстепенный!')

        else:
            bd.create_user_data(message.chat.id, message.chat.first_name)
            await message.answer('Вы второстепенный игрок!')
    if message.chat.id != ADMIN_ID and not ADMIN_FINISH_REPLY:
        await message.answer(
            'Главный игрок ещё не закончил отвечать на вопросы. Ждите, когда он закончит или появится!')
        st = time.time()
        await asyncio.sleep(3)
        while not ADMIN_FINISH_REPLY:
            ed = time.time()
            msg = await message.answer(f'Прошла {ed - st} минута. Главный игрок ещё не закончил / или его ещё нет.')
            await asyncio.sleep(3)
            await msg.delete()

    await FSMUsers.next()
    await message.answer('Вопрос один:', reply_markup=users_reply_buttons)


async def catch_question1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')

    await FSMUsers.next()
    await message.answer('Вопрос два:', reply_markup=users_reply_buttons)


@dp.callback_query_handler(text=['main_person', 'minor_player'])
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    if answer_data == 'main_person':
        text = 'В разработке!'
        await query.message.answer(text)

    elif answer_data == 'minor_player':
        text = 'В разработке!'
        await query.message.answer(text)

    else:
        text = f'Unexpected callback data {answer_data!r}!'
        await query.message.answer(text)


def register_handlers(dp_main: Dispatcher):
    dp_main.register_message_handler(handler_start, commands=['start'])
    dp_main.register_message_handler(catch_user_role, state=FSMUsers.user_role)
    dp_main.register_message_handler(catch_question1, state=FSMUsers.question1)
    # dp_main.register_message_handler(catch_photo, content_types=['photo'], state=FSMUsers.photo)
    # dp_main.register_message_handler(all_msg_handler)
