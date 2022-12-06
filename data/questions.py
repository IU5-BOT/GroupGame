# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from random import choice


def get_random_questions_lst() -> list:
    LST_QUESTIONS = [
        [
            '1. Д1',
            '2. Д2',
            '3. Д3'
        ],
        [
            '1. A1',
            '2. A2',
            '3. A3'
        ],
        [
            '1. Д1',
            '2. Д2',
            '3. Д3'
        ]
    ]
    return choice(LST_QUESTIONS)
