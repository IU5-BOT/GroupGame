# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import asyncio
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as md
from create_bot import dp
from aiogram.types import ReplyKeyboardMarkup
from keyboard.reply_buttons import roles_for_user_button
from data.questions import get_random_questions_lst
from data.managment_db import *
import time

# bd = SQL('users', 'data/users.bd', score=True)
# bd_admin = SQL('admins', 'data/admins.bd')

ADMIN_CREATED: bool = False
ADMIN_FINISH_REPLY: bool = False
ADMIN_ID: int = -1
QUESTIONS = get_random_questions_lst()


class FSMUsers(StatesGroup):
    user_role = State()
    question1 = State()
    question2 = State()
    question3 = State()


async def handler_start(message: types.Message):
    create_user_data(message.chat.id, message.chat.first_name, 'users', 'data/users.db', score=True)
    await message.answer('Привет, это жёская игра!')
    while get_count_users('data/users.db') != 0:
        res = get_count_users('data/users.db')
        await asyncio.sleep(5)
        if res > 2:
            await message.answer(f'Обнаружено {res} чел.')
            break

    await FSMUsers.user_role.set()
    await message.answer("Выберите роль:", reply_markup=roles_for_user_button)


async def catch_user_role(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question1'] = message.text
        global ADMIN_CREATED, ADMIN_ID
        if message.text == '🥇Главный игрок' and not ADMIN_CREATED:
            ADMIN_CREATED = True
            ADMIN_ID = message.chat.id
            delete_person(message.chat.id, 'data/users.db')
            create_user_data(message.chat.id, message.chat.first_name, 'admin', 'data/admin.db')
            await message.answer('Вы главный игрок!')

        elif message.text == '🥇Главный игрок' and ADMIN_CREATED:
            await message.answer('Главный игрок уже есть. Вы второстепенный!')

        else:
            await message.answer('Вы второстепенный игрок!')

    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)

    if message.chat.id != ADMIN_ID and not ADMIN_FINISH_REPLY:
        await message.answer(
            'Главный игрок ещё не закончил отвечать на вопросы. Ждите, когда он закончит или появится!')
        # st = time.time()
        while not ADMIN_FINISH_REPLY:
            await asyncio.sleep(5)
            # ed = time.time()
            # msg = await message.answer(f'Прошла {ed - st} минута. Главный игрок ещё не закончил / или его ещё нет.')
            # await msg.delete()
        await message.answer('Главный игрок закончил отвечать на вопросы. Ваш черёд!')

    await FSMUsers.next()
    await message.answer(QUESTIONS[0], reply_markup=users_reply_buttons)


async def catch_question1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 1, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 1, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[1], reply_markup=users_reply_buttons)


async def catch_question2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 2, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 2, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[2], reply_markup=users_reply_buttons)


async def catch_question3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 3, 'admin', 'data/admin.db')
            global ADMIN_FINISH_REPLY
            ADMIN_FINISH_REPLY = True
            await state.finish()
            await message.answer(
                'Вопросы закончились. Сейчас будут отвечать второстепенные игроки.\n‼️Игра закончится, когда вы напишете "/stop"')
        else:
            add_answer(message.chat.id, answer, 3, 'users', 'data/users.db')
            



# @dp.callback_query_handler(text=['main_person', 'minor_player'])
# async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
#     answer_data = query.data
#
#     if answer_data == 'main_person':
#         text = 'В разработке!'
#         await query.message.answer(text)
#
#     elif answer_data == 'minor_player':
#         text = 'В разработке!'
#         await query.message.answer(text)
#
#     else:
#         text = f'Unexpected callback data {answer_data!r}!'
#         await query.message.answer(text)


def register_handlers(dp_main: Dispatcher):
    dp_main.register_message_handler(handler_start, commands=['start'])
    dp_main.register_message_handler(catch_user_role, state=FSMUsers.user_role)
    dp_main.register_message_handler(catch_question1, state=FSMUsers.question1)
    dp_main.register_message_handler(catch_question2, state=FSMUsers.question2)
    dp_main.register_message_handler(catch_question3, state=FSMUsers.question3)
    # dp_main.register_message_handler(catch_photo, content_types=['photo'], state=FSMUsers.photo)
    # dp_main.register_message_handler(all_msg_handler)
