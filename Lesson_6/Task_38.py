# 38. Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

import random


def bot_intellect(num):
    if num % 5 == 0:
        return 1
    else:
        return num % 5



with_bot = input('Игра с Ботом -> "1", c человеком -> "Enter" ') == '1'
candies = random.randint(20, 30)
player = 1
while candies > 0:
    print(f'Конфет на столе: {candies}')
    print('За один раз можно взять до ', end='')
    if candies >= 4:
        print('4-х конфет')
    else:
        print(f'{candies}-х конфет')
    if with_bot and player == 2:
        candies_get = bot_intellect(candies)
        print(f'Бот взял конфет {candies_get}')
    else:
        candies_get = int(input(f'Игрок {player} берет конфет: '))
    if candies_get > 4 or candies_get > candies:
        print('Неверный ход')
    else:
        candies -= candies_get
        if player == 1:
            player = 2
        else:
            player = 1

if player == 1:
    player = 2
else:
    player = 1
if with_bot and player == 2:
    player = 'Бот))'
print(f'Победил игрок {player}')
