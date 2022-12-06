# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import sqlite3


def get_all_users(path: str, filename: str = 'boss') -> list:
    """ Возращает id, имя"""
    try:
        db = sqlite3.connect(path)
        cursor = db.cursor()
        cursor.execute(f"SELECT id_user, name  FROM {filename}")
        res_users_ids = [(el[0], el[1]) for el in cursor.fetchall()]
        return res_users_ids

    except:
        print('  > Таблица не найдена')

    finally:
        db.commit()
        db.close()


def create_table(file_name: str, path: str, score: bool = False):
    try:
        db = sqlite3.connect(path)
        cursor = db.cursor()
        # Если это юзер, сделаем ему ещё счётчик.
        if score:
            try:
                # TODO: потом просто вернуть.
                '''cursor.execute("CREATE TABLE" + f" {file_name} " + """(
                    id_user integer,
                    name text,
                    q1 integer,
                    q2 integer,
                    q3 integer,
                    q4 integer,
                    q5 integer,
                    q6 integer,
                    q7 integer,
                    q8 integer,
                    q9 integer,
                    q10 integer,
                    q11 integer,
                    q12 integer,
                    q13 integer,
                    q14 integer,
                    q15 integer,
                    q16 integer,
                    q17 integer,
                    q18 integer,
                    q19 integer,
                    q20 integer)""")'''
                cursor.execute("CREATE TABLE" + f" {file_name} " + """(
                                    id_user integer,
                                    name text,
                                    score integer,
                                    q1 integer,
                                    q2 integer,
                                    q3 integer)""")
                print(f'  > Таблица {file_name} создана!')
                # db.commit()
                # db.close()

            except sqlite3.OperationalError:
                # Всё супер. Просто она уже есть.
                print(f'Таблица {file_name} уже есть. Найс найс.')
            finally:
                db.commit()
                db.close()

        else:
            try:
                cursor.execute("CREATE TABLE" + f" {file_name} " + """(
                                    id_user integer,
                                    name text,
                                    q1 integer,
                                    q2 integer,
                                    q3 integer)""")
                print(f'  > Таблица {file_name} создана!')

            except sqlite3.OperationalError:
                # Всё супер. Просто она уже есть.
                print('Таблица  {file_name} уже есть. Найс найс.')

            finally:
                db.commit()
                db.close()

    except:
        # А вот это уже плохо.
        print(' > Таблица не найдена! Гг.')


def create_user_data(user_id: int, user_name: str, filename: str, path: str, score: bool = False):
    db = sqlite3.connect(path)
    cursor = db.cursor()
    # TODO: Расскомментировать потом.
    '''cursor.execute(
        "INSERT INTO {} VALUES ({}, '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(
            self.filename, user_id, user_name,
            args[0], args[1], args[2], args[3], args[4], args[5],
            args[6], args[7], args[8], args[9], args[10], args[11],
            args[12], args[13], args[14], args[15], args[16],
            args[17], args[18], args[19])
    )'''
    if score:
        cursor.execute(f"INSERT INTO {filename} VALUES ({user_id}, '{user_name}', 0, Null, Null, Null)")

    else:
        cursor.execute(f"INSERT INTO {filename} VALUES ({user_id}, '{user_name}', Null, Null, Null)")
    db.commit()
    db.close()


def add_answer(user_id: int, answer_user: str, counter_questions: int, filename: str, path: str):
    db = sqlite3.connect(path)
    cursor = db.cursor()
    res = find_index_of_name(answer_user)
    try:
        cursor.execute(f"UPDATE {filename} SET q{counter_questions} = {res} WHERE id_user = {user_id}")
    except:
        print(' >> ERROR')
    db.commit()
    db.close()


def find_index_of_name(name: str, path: str):
    db = sqlite3.connect(path)
    cursor = db.cursor()
    table = 'users'
    try:
        cursor.execute(f"SELECT id_user FROM {table} WHERE name = {name}")
    except:
        print(' >> ERROR')
    res = None
    for el in cursor.fetchall():
        res = el
    db.commit()
    db.close()
    print(res)
    return res
