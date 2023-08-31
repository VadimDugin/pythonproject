import csv
import random


def choice_anm_us():
    print(
        '1.Вход от лица админестратора\n'
        '2.Вход от лица пользователя'
    )
    a = input('Выбор: ')
    if a == '1':
        a = input('Пороль админа: ')
        if a == '7878':
            admin_menu()
    elif a == '2':
        reg()


def admin_menu():
    while True:
        print(
            '1.Просмотр всех пользователей\n'
            '2.Удаление пользователя\n'
            '3.Выход'
        )
        v = input('Выбор: ')
        if v == '1':
            with open('User.csv') as name:
                read = csv.reader(name)
                next(read)
                for row in read:
                    print(row)
        elif v == '2':
            u = 0
            i = int(input('Сколько пользователей удалить: '))
            while u < i:
                a = input('Логин пользователя которого удаляем: ')
                with open('User.csv', 'r') as file:
                    reader = csv.reader(file)
                    with open('new_file.csv', 'w', newline='') as new_file:
                        writer = csv.writer(new_file)
                        for row in reader:
                            if row[0] != a:
                                writer.writerow(row)
                        with open('new_file.csv', 'r') as fiile:
                            r = csv.reader(fiile)
                            with open('new_file.csv', 'w', newline='') as neew_file:
                                writer = csv.writer(neew_file)
                                for row in r:
                                    if row[0] != a:
                                        writer.writerow(row)
                u += 1
        elif v == '3':
            print('Конец программы')
            break


def reg():
    print(
        '1.Вход\n'
        '2.Регистрация'
    )
    v = input('Выбор: ')
    if v == '1':
        login()

    elif v == '2':
        log = input('Логин: ')
        name = input('Имя: ')
        sur = input('Фамилия: ')
        patronymic = input('Отчество: ')
        series = input('Серия пасморта: ')
        number_us = input('Номер паспорта: ')
        data_of_bitch = input('Дата рождения: ')
        password = input('Пороль: ')
        register_us(
            log, password, name, sur, patronymic,
            series, number_us, data_of_bitch,
                    )
        print('Регистрация завершена! Для входа перезапустите')
    else:
        print('Не верное значени')


def generate_random_number():
    number = ""
    for _ in range(10):
        digit = random.randint(1, 10)
        number += str(digit)
    return int(number)


def register_us(a, b, c, d, e, f, g, s):
    us_ch = f's-{generate_random_number()}'
    balance = random.randint(1000, 100000)
    validity = '08/29'
    cvv = random.randint(100, 999)
    card = '2022'
    i = 1
    while i <= 12:
        i += 1
        rand = random.randint(1, 9)
        sp = str(rand)
        card += sp
    chunks = [card[i:i + 4] for i in range(0, len(card), 4)]
    res = ' '.join(chunks)
    kridbal = 0
    kridval = '08/28'
    cvc = random.randint(101, 999)
    card2 = '2020'
    ii = 1
    while ii <= 12:
        ii += 1
        rand = random.randint(1, 9)
        sp = str(rand)
        card2 += sp
    chunks = [card2[k:k + 4] for k in range(0, len(card2), 4)]
    rez = ' '.join(chunks)
    kar = [
                a, us_ch, c, d, e, f,
                g, s, b, res, validity, cvv, balance,
                rez, kridval, cvc, kridbal
            ]
    with open('User.csv', 'a', newline="") as file:
        a = csv.writer(file)
        a.writerow(kar)


def login():
    nem = input('Логин: ')
    pas = input('Пороль: ')
    with open('User.csv') as name:
        reader = csv.reader(name)
        next(reader)
        for row in reader:
            user_name = row[0]
            user_pass = row[8]
            if user_name == nem and user_pass == pas:
                print('Доступ разрешен')
                menu()


def credit():
    credit_sum = int(input('Сумма кредита: '))
    us_time = int(input('Кол - во месяцев: '))
    cred10 = credit_sum * 0.1
    b = credit_sum / cred10
    a = credit_sum / us_time
    x = credit_sum * a
    c = b + x
    print(f'На ваш баланс начислено: {credit_sum}')
    print(f'Вам нужно платить ежемесячно: {c}')


def k_card():
    user = input('Введите лицевой счет: ')
    with open('User.csv') as file:
        read = csv.reader(file)
        for row in read:
            if row[1] == user:
                print(f'{row[-4]}\n{row[-3]}         {row[-2]}')
                print(f'Баланс:{row[-1]} ')
                print()


def menu():
    while True:
        print(
            '1.Просмотр лицевого счета\n'
            '2.Просмотр данных дебитовой карты\n'
            '3.Создание кредитной карты\n'
            '4.Просмотр данных кредитной карты\n'
            '5.Взять кредит'

        )
        v = input('Выбор: ')
        if v == '1':
            log = input('Логин: ')
            with open('User.csv') as name:
                read = csv.reader(name)
                for row in read:
                    if row[0] == log:
                        print(f'Номер вашего лицевого счета - {row[1]}\np.s лучше его скопировать')
                        print()
        elif v == '2':
            us_check = input('Введите номер лицевого счета: ')
            with open('User.csv') as name:
                read = csv.reader(name)
                for row in read:
                    if row[1] == us_check:
                        print(f'{row[9]}\n{row[10]}         {row[11]}')
                        print(f'Баланс:{row[12]} ')
                        print()
        elif v == '3':
            print(
                '1.Создать кредитную карту\n'
                '2.Не создавать'
            )
            o = input('Выбор: ')
            if o == '1':
                print('Кредитная карта успешно создана!')
                k_card()
            elif o == '2':
                print('Кредитная карта не создана')

        elif v == '4':
            k_card()
        elif v == '5':
            credit()


choice_anm_us()
