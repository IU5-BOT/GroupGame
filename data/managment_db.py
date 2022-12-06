# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import sqlite3


# TODO: boss ->users
def get_all_users(path: str = '../data/boss.bd') -> list:
    """ Возращает id, имя"""
    try:
        db = sqlite3.connect(path)
        cursor = db.cursor()
        # TODO: После сменить boss -> users
        cursor.execute(f"SELECT id_user, name  FROM boss")
        res_users_ids = [(el[0], el[1]) for el in cursor.fetchall()]
        return res_users_ids

    except:
        print('  > Таблица не найдена')

    finally:
        db.commit()
        db.close()


# TODO: В конце расскоментировать для 20 вопросов всё.
class SQL:
    def __init__(self, file_name: str, path: str):
        self.filename = file_name
        self.path = path
        try:
            db = sqlite3.connect(path)
            cursor = db.cursor()
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
                print('Таблица уже есть. Найс найс.')

        except:
            # А вот это уже плохо.
            print(' > Таблица не найдена! Гг.')

        finally:
            db.commit()
            db.close()

    def create_user_data(self, user_id: int, user_name: str):
        db = sqlite3.connect(self.path)
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
        cursor.execute(f"INSERT INTO {self.filename} VALUES ({user_id}, '{user_name}', Null, Null, Null)")
        db.commit()
        db.close()

    def add_answer(self, user_id: int, answer: int, counter_questions: int):
        db = sqlite3.connect(self.path)
        cursor = db.cursor()
        cursor.execute(f"UPDATE {self.filename} SET q{counter_questions} = {answer} WHERE id_user = {user_id}")
        db.commit()
        db.close()


if __name__ == '__main__':
    bd = SQL('boss', 'boss.db')
    bd.add_answer(0, 777, 1)
    res = get_all_users('boss.db')
    print(*res)
