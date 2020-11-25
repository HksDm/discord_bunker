import random
from discord.ext import commands


TOKEN = 'Укажите Developer Discord Token'

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == '!играю':
        response = f'Ваша профессия: {proffs()}\nСостояние здоровья: {health()}\nБиологическая характеристика: {bio_char()}\n' \
                   f'Дополнительная информация: {dop_info()}\nЧеловеческое качество: {human_qualities()}\nХобби: {hobbie()}\n' \
                   f'Фобия: {phobia()}\nБагаж: {baggage()}\nКарта специального условия: {action()}'
        await message.author.send(response)

    if message.content.lower() == '!профессия':
        response = f'Ваша профессия: {proffs()}'
        await message.author.send(response)

    if message.content.lower() == '!здоровье':
        response = f'Состояние здоровья: {health()}'
        await message.author.send(response)

    if message.content.lower() == '!био':
        response = f'Биологическая характеристика: {bio_char()}'
        await message.author.send(response)

    if message.content.lower() == '!допинфо':
        response = f'Дополнительная информация: {dop_info()}'
        await message.author.send(response)

    if message.content.lower() == '!качество':
        response = f'Человеческое качество: {human_qualities()}'
        await message.author.send(response)

    if message.content.lower() == '!хобби':
        response = f'Хобби: {hobbie()}'
        await message.author.send(response)

    if message.content.lower() == '!фобия':
        response = f'Фобия: {phobia()}'
        await message.author.send(response)

    if message.content.lower() == '!багаж':
        response = f'Багаж: {baggage()}'
        await message.author.send(response)

    if message.content.lower() == '!хелп':
        response = f'!играю !профессия !био !здоровье !допинфо !качество !хобби !фобия !багаж'
        await message.author.send(response)

    if message.content.lower() == '!катастрофа':
        response = f'Катастрофа: {cataclism()}'
        await message.channel.send(response)


def cataclism():
    cataclism = ['Потоп']
    cataclism = random.choice(cataclism)
    return cataclism


def proffs():
    proffs = [
        'иммунолог',
        'стоматолог',
        'сексолог',
        'психолог',
        'вирусолог',
        'хирург',
        'педиатр',
        'отоларинголог',
        'Дерматолог',
        'Патологоанатом',
        'Биолог',
        'Физик',
        'Историк',
        'Астроном',
        'Экономист',
        'Переводчик',
        'Химик',
        'Геолог',
        'Социолог',
        'Философ',
        'Военный офицер',
        'Полицейский',
        'Пожарный',
        'Охранник',
        'Президент',
        'Военный врач',
        'Телохранитель',
        'Дезертир',
        'Моряк',
        'Десантник',
        'Писатель',
        'Музыкант',
        'Поэт',
        'Художник',
        'Блогер',
        'Режиссёр',
        'Порно актёр',
        'Телеведущий',
        'Скульптор',
        'Архитектор',
        'Фотограф',
        'Столяр',
        'Слесарь',
        'Хакер',
        'Электрик',
        'Батюшка',
        'Инструктор по выживанию',
        'Повар',
        'Безработный бомж',
        'Разнорабочий',
        'Механик',
        'Уборщик',
        'Продавщица',
        'Вор в законе'
    ]
    proffs = random.choice(proffs)
    return proffs.lower()


def health():
    value = random.randint(1, 5)
    if value < 3:
        health = 'идеально здоров'
    if value < 5:
        health = [
            'косоглазие',
            'глухота',
            'немота',
            'слепота',
            'глухонемой',
            'бесплодие',
            'заикание',
            'без руки',
            'без ноги',
            'плохая память',
            'табачная зависимость',
        ]
        health = random.choice(health)
    if value == 5:
        health = [
            'онкология',
            'ожирение',
            'алкоголизм',
            'наркомания',
            'диабет',
            'вич',
            'туберкулез',
            'анорексия',
        ]
        health = f'{random.choice(health)} {random.randint(1, 9) * 10}%'

    return health


def bio_char():
    sex = ['мужчина', 'женщина']
    sex = random.choice(sex)

    value = random.randint(1, 10)
    if value < 9 and sex == 'мужчина':
        orientation = 'гетеросексуален'
    if value < 9 and sex == 'женщина':
        orientation = 'гетеросексуальна'
    if value == 9 and sex == 'мужчина':
        orientation = 'бисексуален'
    if value == 9 and sex == 'женщина':
        orientation = 'бисексуальна'
    if value == 10 and sex == 'мужчина':
        orientation = 'гомосексуален'
    if value == 10 and sex == 'женщина':
        orientation = 'гомосексуальна'

    age = [18, 20, 25, 28, 30, 35, 38, 40, 45, 47, 49, 50, 60, 70]
    age = random.choice(age)
    bio_char = f'{sex}, {orientation}, {age} лет'
    return bio_char


def dop_info():
    dop_info = [
        'умеет ориентироваться по звездам',
        'вышивает крестиком',
        'любит постарше',
        'ходил под парусником',
        'объездил весь мир',
        'знает все стихи Пушкина',
        'прочитал все комиксы про зомби',
        'по первому образованию биолог',
        'сладкоежка',
        'ходит в походы',
        'умеет делать алкоголь из чего угодно',
        'выиграл чемпионат мира по пейнтболу',
        'метко стреляет из лука',
        'садовод',
        'брал курсы первой помощи',
        'рыболов',
        'охотник',
        'мастер спорта по фри дайвингу',
        'верит в призраков',
        'верит в экстрасенсов',
        'знает президента лично',
        'ограбил банк',
        'человек-энциклопедия',
        'подрабатывает в театре',
        'копрофил',
        'инженер-самоучка',
        'по жизни счастливчик - трижды выигрывал миллион',
        'чемпион области по бодибилдингу',
        'нимфомания'
    ]

    dop_info = random.choice(dop_info)
    return dop_info


def human_qualities():
    human_qualities = [
        'аккуратный',
        'бережливый',
        'бескорыстный',
        'вежливый',
        'верный',
        'дисциплинированный',
        'добрый',
        'коммуникабельный',
        'ответственный',
        'решительный',
        'скромный',
        'смелый',
        'толерантный',
        'упорный',
        'честный',
        'авторитарный',
        'агрессивный',
        'азартный',
        'безалаберный',
        'безответственный',
        'вульгарный',
        'грубый',
        'жадный',
        'лживый',
        'занудный',
        'избалованный',
        'любопытный',
        'наглый',
        'самовлюбленный',
        'паникер',
        'трусливый',
        'эгоист',
        'альтруист',
        'креативный',
        'истеричный',
    ]
    human_qualities = random.choice(human_qualities)
    return human_qualities


def hobbie():
    hobbie = [
        'выращивание растений',
        'пивоварение',
        'парусный спорт',
        'конный спорт',
        'плавание',
        'ремонт электротехники',
        'ремонт часов',
        'катание на скейте',
        'катание на лыжах',
        'спортивное ориентирование',
        'валяние шерсти',
        'лежание на диване',
        'компьютерные игры',
        'танцы',
        'пение',
        'исторические реконструкции',
        'волонтерство',
        'путешествия',
        'велоспорт',
        'игра на губной гармошке',
        'рисование',
        'поэзия',
        'чтение книг',
        'самодельщик',
        'закаляться',
        'армрестлинг',
        'просмотр порно',
        'кулинария',
        'виноделие',
        'паркур'
    ]
    hobbie = random.choice(hobbie)
    return hobbie


def phobia():
    phobia = [
        'без фобий',
        'без фобий',
        'без фобий',
        'без фобий',
        'без фобий',
        'агорафобия — боязнь пространства, открытых мест, площадей, толп людей, рынков',
        'аграфобия  — боязнь сексуальных домогательств, секса',
        'айлурофобия — боязнь кошек',
        'айхмофобия — боязнь острых предметов',
        'аквафобия — боязнь воды, утопления',
        'аклиофобия — боязнь глухоты',
        'акротомофобия — боязнь ампутации',
        'алгофобия — боязнь боли',
        'андрофобия — боязнь мужчин',
        'бактериофобия — боязнь заразиться бактериями',
        'баллистофобия — боязнь поражения пулей, бомбой или снарядом',
        'блаптофобия — боязнь нанести кому-либо повреждение',
        'венерофобия — боязнь заразиться венерической болезнью',
        'гексакосиойгексеконтагексафобия — страх числа 666',
        'гелотофобия — страх оказаться объектом юмора, насмешек',
        'гемофобия — боязнь крови',
        'дентофобия — боязнь стоматологов, лечения зубов',
        'зоофобия — боязнь животных',
        'кинофобия — боязнь собак',
        'арахнофобия - боязнь пауков',
        'клаустрофобия — боязнь замкнутого пространства',
        'мусофобия — боязнь мышей и крыс',
        'некрофобия — боязнь трупов и похоронных принадлежностей'
        'ахлуофобия — боязнь темноты, ночи',
        'онанофобия — боязнь вредных последствий онанизма',
        'пирофобия — боязнь огня, пожаров, гибели от огня',
        'радиофобия — боязнь радиации',
        'спидофобия — боязнь заразиться СПИДом',
        'тетрафобия — боязнь числа 4',
        'фазмофобия — боязнь призраков и духов',
    ]
    phobia = random.choice(phobia)
    return phobia


def baggage():
    baggage = [
        'Набор медицинских инструментов',
        'Набор холодного оружия',
        'Набор набор огнестрельного оружия',
        'Набор инструментов для электромонтажных работ',
        'Набор слесарных инструментов',
        'Набор столярных инструментов',
        'Набор отверток и гаечных ключей',
        'Набор для рисования(холсты, краски, ручки, карандаши)',
        'Фотокамера',
        'Видеокамера',
        'Грудной ребёнок',
        'Лопата',
        'Ноутбук',
        'Переносная гидроэлектростанция',
        'Переносная ветреная электростанция',
        'Переносная солнечная батарея',
        'Набор аккумуляторов на 30 дней работы',
        'Набор зарядок для аккаумяторов',
        'Флейта',
        'Гитара',
        'Персидский кот',
        'Овчарка',
        'Паук',
        'Саженцы деревьев',
        'Семена пшеницы',
        'Семена конопли',
        'Канистра с бензином 10 л',
        'Аптечка первой необходимости',
        'Десять сигаретных блоков',
        'Набор антитабачных пластырей',
        'Канистра со спиртом 10 л',
        'Куст конопли',
        'Презервативы 10 шт',
        'Верёвка',
        'Мыло',
        'Стопка порножурналов',
        'Набор настольных игр',
        'Набор карточных игр',
        'протез руки',
        'Протез ноги',
        'Слуховой аппарат',
        'набор респираторных масок',
        'дресированная крыса',
        'пакеты с отличной почвой'
    ]
    baggage = random.choice(baggage)
    return baggage.lower()


def action():
    action = [
        "Карта врага - вы проиграете, если с вами в бункер пападет хотя бы один из ваших соседей",
        "Карта друга - вы програете, если с вами в бункер НЕ попадет хотя бы один из ваших соседей",
        'Вы вскрываете информацию о том, что рядом с вами дружественный бункер с двумя химиками мужчинами способными дать потомство',
        'Вы вскрываете информацию о том, что рядом с вами дружественный бункер с двумя химиками женщинами способными дать потомство',
        'Вы вскрываете информацию о том, что рядом с вами дружественный бункер с двумя химиками',
        'Вы вскрываете информацию о том, что рядом с вами дружественный бункер с двумя военными мужчинами способными дать потомство',
        'Вы вскрываете информацию о том, что рядом с вами дружественный бункер с двумя военными женщинами способными дать потомство',
        'Вы вскрываете информацию о том, что рядом с вами дружественный бункер с двумя военными',
        'Вы вскрываете информацию о том, что рядом с вами дружественный бункер с двумя биологами мужчинами способными дать потомство',
        'Вы вскрываете информацию о том, что рядом с вами дружественный бункер с двумя биологами женщинами способными дать потомство',
        'Вы вскрываете информацию о том, что рядом с вами дружественный бункер с двумя биологами',
        "Вы вскрываете информацию о том, что рядом с вами враждебно настроенный бункер",
        "Вы вскрываете информацию о том, что рядом с вами враждебно настроенный бункер",
        "Вы вскрываете информацию о том, что рядом с вами враждебно настроенный бункер",
        "Вы вскрываете информацию о том, что рядом с вами находится склад с провиантом, а также рассказываете, где он находится",
        "Вы вскрываете информацию о том, что рядом с вами находится склад с провиантом, но только вам известно где он",
        "Вы вскрываете информацию о том, что рядом с вами находится склад с оружием и боеприпасами, а также рассказываете, где он находится",
        "Вы вскрываете информацию о том, что рядом с вами находится склад с оружием и боеприпасами, но только вам известно где он",
        "Вы вскрываете информацию о том, что рядом с вами находится склад с медикаментами, а также рассказываете, где он находится",
        "Вы вскрываете информацию о том, что рядом с вами находится склад с медикаментами, но только вам известно где он",
        "Вы можете обменяться профессией с любым другим игроком",
        "Вы можете обменяться здоровьем с любым другим игроком",
        "Вы можете обменяться багажом с любым другим игроком",
        "Вы можете обменяться фобией с любым другим игроком",
        'Вы можете обменяться хобби с любым другим игроком',
        'Вы можете обменяться человеческими качествами с любым другим игроком',
        'Вы можете обменяться дополнительным навыком с любым другим игроком',
        "Вы можете заменить свою профессию на случайную",
        "Вы можете заменить свое здоровье на случайное",
        "Вы можете заменить свой багаж на случайный",
        "Вы можете заменить свою фобию на случайную",
        'Вы можете заменить свое хобби на случайное',
        'Вы можете заменить свои человеческие качества на случайные',
        'Вы можете заменить свои дополнительные навыки на случайные',
        "Вы можете заменить чужую профессию на случайную",
        "Вы можете заменить чужое здоровье на случайное",
        "Вы можете заменить чужой багаж на случайный",
        "Вы можете заменить чужую фобию на случайную",
        'Вы можете заменить чужое хобби на случайное',
        'Вы можете заменить чужие человеческие качества на случайные',
        'Вы можете заменить чужие дополнительные навыки на случайные',
        'Вы можете излечить любого игрока, в том числе и себя от любой болезни',
        'Вы можете возродить любого игрока, но не себя',
        'Вы можете все голоса направленные против вас в этом ходу, перенести на другого игрока',
        'Вы можете использовать карту и получить иммунитет на изгнание в этом ходу',
        'Вы меняете всем игрокам их профессию, в том числе и свою на случайную',
        'Вы меняете всем игрокам их здоровье, в том числе и свое на случайное',
        'Вы меняете всем игрокам их багаж, в том числе и свой на случайный',
        'Вы меняете всем игрокам их фобию, в том числе и свою на случайную',
        'Вы меняете всем игрокам их человеческие качества, в том числе и свои на случайные',
        'Вы меняете всем игрокам их дополнительную информацию, в том числе и свою на случайную',
        'Вы увеличиваете бункер на 1 место, а в этом ходу никого не выгоняют',
    ]
    action = random.choice(action)
    return action.lower()


client.run(TOKEN)
