# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import asyncio
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as md
from create_bot import dp
from aiogram.types import ReplyKeyboardMarkup
from keyboard.reply_buttons import roles_for_user_button
from keyboard.inline_buttons import button_stop_inline
from data.questions import get_random_questions_lst
from data.managment_db import *
from create_bot import bot
import time

# bd = SQL('users', 'data/users.bd', score=True)
# bd_admin = SQL('admins', 'data/admins.bd')

ADMIN_CREATED: bool = False
ADMIN_FINISH_REPLY: bool = False
ADMIN_ID: int = -1
ADMIN_RES: list = []
QUESTIONS = get_random_questions_lst()
WINNER = (-1, -1, '')


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
            await asyncio.sleep(3)
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
            global ADMIN_FINISH_REPLY, ADMIN_RES
            ADMIN_FINISH_REPLY = True
            ADMIN_RES = get_score(message.chat.id, 'admin', 'data/admin.db')[0][2:]

            await state.finish()
            await message.answer(
                'Вопросы закончились. Сейчас будут отвечать второстепенные игроки.\n‼️Игра закончится, когда вы напишете "/stop"',
                reply_markup=types.ReplyKeyboardRemove())

        else:
            add_answer(message.chat.id, answer, 3, 'users', 'data/users.db')
            user = get_score(message.chat.id, 'users', 'data/users.db')[0][2:]

            try:
                res_score = sum(1 for i in range(len(user)) if ADMIN_RES[i] == user[i])
            except:
                print(' > ERROR')
                res_score = 0
            await message.answer(f'Супер, вы набрали {res_score}')
            global WINNER
            if res_score > WINNER[0]:
                WINNER = (res_score, message.chat.id, message.chat.first_name)
            await state.finish()


async def all_msg_handler(message: types.Message):
    button_text = message.text
    if button_text == '/stop':
        res = get_all_users('data/users.db')
        for el in res:
            await bot.send_message(el[0], f"Игра закончена! Победил - {WINNER[2]}. Совпало ответов: {WINNER[0]}",
                                   reply_markup=types.ReplyKeyboardRemove())
        await message.answer(f"Игра закончена! Победил - {WINNER[2]}. Совпало ответов: {WINNER[0]}",
                             reply_markup=types.ReplyKeyboardRemove())


# @dp.callback_query_handler(text=['stop'])
# async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
#     answer_data = query.data
#
#     if answer_data == 'stop':
#         await query.message.answer('Работает!')
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
    dp_main.register_message_handler(all_msg_handler)
