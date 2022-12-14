# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from random import choice


def get_random_questions_lst() -> list:
    LST_QUESTIONS = [
        ['1. Кто чаще всего смотрит романтические фильмы',
         '2. Кто станет миллионером',
         '3. кто может рассмеяться в самый неподходящий момент',
         '4. С кого скорее всего могут написать книгу',
         '5. Кто забудет где припарковал машину',
         '6. Кто останется дома , в пятницу вечером',
         '7. Кто вернет деньги , найденные на улице',
         '8. Кто тратит больше времени на сборы',
         '9. Кто вечно опаздывает',
         '10. Кто спит до обеда',
         '11. Кто скорее всего споткнётся с лестницы',
         '12. Кто может съесть всю еду в Макдоналдс',
         '13. Кто любит ничего не делать',
         '14. Кому всё равно, какой выйдешь из дома',
         '15. Кто может потратить все деньги за один раз',
         '16. Кто всегда готов пойти на тусовку',
         '17. Кто знает все песни мира',
         '18. Кто чаще всего сидит на ПП',
         '19. У кого самый заразительный смех',
         '20. Кто любит проводить время в одиночестве'],
        ['1. Кто самый главный паникер',
         '2. Чьи сны можно назвать доказательством шизофрении',
         '3. Кто из присутствующих больше всего отвечает твоим визуальным запросам', '4. У кого был крайний секс',
         '5. Назовите человека в компании, с которым вы больше всего похожи',
         '6. Кто из компании выглядит менее вдохновляющим на достижение успеха',
         '7. Кто мог бы стать главным героем комедийного фильма',
         '8. Кому из компании вы хоть раз завидовали по-черному',
         '9. С кем из компании, не будь вы друзьями, стали бы врагами',
         '10. Кто смог бы без зазрения совести заняться сексом в спальне родителей',
         '11. Чья история поиска браузера должна быть помечена знаком строго 18+',
         '12. Кто вероятнее всего упустит свою жизнь из-за собственной лени',
         '13. Человек чьи мысли нужно записывать',
         '14. Кто может споткнуться о собственную ногу и умереть, задохнувшись под одеялом',
         '15. Чья харизма вас больше всего привлекает', '16. У кого больше всего скелетов в шкафе',
         '17. Кем,по вашему мнению, можно гордиться',
         '18. Кто не сможет встречаться с человеком, если по отношению к нему не возникает ни одной пошлой мысли',
         '19. Самый противоречивый человек',
         '20. Кто скорее выберет никогда не есть, чем никогда не спать'],
        ['1. кто мог бы прыгнуть с парашютом',
         '2. кто легко в одиночку может поехать на блаблакар',
         '3. кто может на спор засунуть лампочку в рот',
         '4. кто может подраться за еду',
         '5. у кого всегда в приоритете сон',
         '6. кто делает все в последний момент',
         '7. кто будет рад жить в палатке',
         '8. кто может украсить конфету на развес в ашане',
         '9. кто никогда не поедет в машине не пристегнувшись',
         '10. кто может взять пакет на кассе самообслуживания и не оплатить его',
         '11. кто ставит везде один и тот же пароль',
         '12. кто боится охранников в летуаль',
         '13. кто может уйти из ресторана не заплатив',
         '14. кто может разрушить отношения',
         '15. кто моет полы трижды',
         '16. кто фотографирует все что видит',
         '17. кто настоящий патриот',
         '18. кто готов поехать на машине хоть на край света',
         '19. кто боится собак',
         '20. кто всегда готов помочь'],
        ['1. кто бы смог поплавать с акулами',
         '2. кто бы мог отправиться в путешествие с выключенным телефоном',
         '3. кто чаще попадает в неловкие ситуации',
         '4. за кого иногда бывает стыдно',
         '5. кто смог бы с легкостью познакомится на улице с понравившимся человеком',
         '6. кто откладывает важные задачи на потом',
         '7. кто скорее всего выберет остаться дома, чем тусовку с друзьями',
         '8.кто вместо просмотра фильма будет читать книгу',
         '9.до кого никогда не дозвонишься',
         '10.кто часто не отвечает на сообщения',
         '11.кто не боится смотреть ужастики в темноте и одиночестве',
         '12.у кого на рабочем месте постоянный беспорядок',
         '13.кто скорее всего не уступит место в общественном транспорте',
         '14.кто говорит одно, а делает другое',
         '15.кто бы смог жить в доме на колесах в лесу',
         '16.кто постоянно попадает в неприятности',
         '17.от кого можно ожидать чего угодно',
         '18.кто всегда в сети',
         '19.кто бы не смог жить в глухой деревне',
         '20.с кем всегда весело']
    ]
    return choice(LST_QUESTIONS)
