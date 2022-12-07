# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import asyncio
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from keyboard.reply_buttons import roles_for_user_button
from data.questions import get_random_questions_lst
from data.managment_db import *
from create_bot import bot
import aiogram.utils.markdown as md
import time

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
    question4 = State()
    question5 = State()
    question6 = State()
    question7 = State()
    question8 = State()
    question9 = State()
    question10 = State()
    question11 = State()
    question12 = State()
    question13 = State()
    question14 = State()
    question15 = State()
    question16 = State()
    question17 = State()
    question18 = State()
    question19 = State()
    question20 = State()


async def handler_start(message: types.Message):
    create_user_data(message.chat.id, message.chat.first_name, 'users', 'data/users.db')
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
        else:
            add_answer(message.chat.id, answer, 3, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[3], reply_markup=users_reply_buttons)


async def catch_question4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 4, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 4, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[4], reply_markup=users_reply_buttons)


async def catch_question5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 5, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 5, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[5], reply_markup=users_reply_buttons)


async def catch_question6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 6, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 6, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[6], reply_markup=users_reply_buttons)


async def catch_question7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 7, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 7, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[7], reply_markup=users_reply_buttons)


async def catch_question8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 8, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 8, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[8], reply_markup=users_reply_buttons)


async def catch_question9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 9, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 9, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[9], reply_markup=users_reply_buttons)


async def catch_question10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 10, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 10, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[10], reply_markup=users_reply_buttons)


async def catch_question11(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 11, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 11, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[11], reply_markup=users_reply_buttons)


async def catch_question12(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 12, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 12, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[12], reply_markup=users_reply_buttons)


async def catch_question13(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 13, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 13, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[13], reply_markup=users_reply_buttons)


async def catch_question14(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 14, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 14, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[14], reply_markup=users_reply_buttons)


async def catch_question15(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 15, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 15, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[15], reply_markup=users_reply_buttons)


async def catch_question16(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 16, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 16, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[16], reply_markup=users_reply_buttons)


async def catch_question17(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 17, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 17, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[17], reply_markup=users_reply_buttons)


async def catch_question18(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 18, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 18, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[18], reply_markup=users_reply_buttons)


async def catch_question19(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 19, 'admin', 'data/admin.db')
        else:
            add_answer(message.chat.id, answer, 19, 'users', 'data/users.db')

    await FSMUsers.next()
    users_reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = (el[1] for el in get_all_users('data/users.db'))
    users_reply_buttons.row(*buttons)
    await message.answer(QUESTIONS[19], reply_markup=users_reply_buttons)


async def catch_question20(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        data['question1'] = answer
        await message.answer(f'Ваш ответ: {answer}')
        # Добавляем ответ в таблицу SQL.
        if message.chat.id == ADMIN_ID:
            add_answer(message.chat.id, answer, 20, 'admin', 'data/admin.db')
            global ADMIN_FINISH_REPLY, ADMIN_RES
            ADMIN_FINISH_REPLY = True
            ADMIN_RES = get_score(message.chat.id, 'admin', 'data/admin.db')[0][2:]

            await state.finish()
            await message.answer(
                'Вопросы закончились. Сейчас будут отвечать второстепенные игроки.\n‼️Игра закончится, когда вы напишете "/stop"',
                reply_markup=types.ReplyKeyboardRemove())

        else:
            add_answer(message.chat.id, answer, 20, 'users', 'data/users.db')
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
    dp_main.register_message_handler(catch_question4, state=FSMUsers.question4)
    dp_main.register_message_handler(catch_question5, state=FSMUsers.question5)
    dp_main.register_message_handler(catch_question6, state=FSMUsers.question6)
    dp_main.register_message_handler(catch_question7, state=FSMUsers.question7)
    dp_main.register_message_handler(catch_question8, state=FSMUsers.question8)
    dp_main.register_message_handler(catch_question9, state=FSMUsers.question9)
    dp_main.register_message_handler(catch_question10, state=FSMUsers.question10)
    dp_main.register_message_handler(catch_question11, state=FSMUsers.question11)
    dp_main.register_message_handler(catch_question12, state=FSMUsers.question12)
    dp_main.register_message_handler(catch_question13, state=FSMUsers.question13)
    dp_main.register_message_handler(catch_question14, state=FSMUsers.question14)
    dp_main.register_message_handler(catch_question15, state=FSMUsers.question15)
    dp_main.register_message_handler(catch_question16, state=FSMUsers.question16)
    dp_main.register_message_handler(catch_question17, state=FSMUsers.question17)
    dp_main.register_message_handler(catch_question18, state=FSMUsers.question18)
    dp_main.register_message_handler(catch_question19, state=FSMUsers.question19)
    dp_main.register_message_handler(catch_question20, state=FSMUsers.question20)
    dp_main.register_message_handler(all_msg_handler)
