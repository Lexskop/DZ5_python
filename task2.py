# 2-Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет. Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# Если делаете a и b - не нужно создавать отдельных файлов с полностью копированным кодом, лучше выделите в отдельные функции бота и умного бота.

import random

def playing_two_players(candy_count: int, step_count: int):
    """
    Непосредственно код для игры двух игроков
    """
    player_number = 1
    while candy_count != 0:
        step_player = int(input(f'Игрок {player_number} берет конфеты -> '))
        if candy_count-step_player < 0 or step_player > step_count:
            print('Ты не можешь брать столько!')
        else:
            candy_count = candy_count-step_player
            print(
                f'Игрок {player_number} взял {step_player} конфет и {candy_count} осталось')
            if candy_count == 0:
                print(f'Игрок {player_number} - ПОБЕДИТЕЛЬ!')
            if player_number == 1:
                player_number = 2
            else:
                player_number = 1


def game_one_player(candy_count: int, step_count: int):
    """
    Код для игры с ботом
    """
    player_who = 'Игрок'
    while candy_count != 0:
        if player_who == 'Игрок':
            step_player = int(input(f'{player_who} взял конфет -> '))
        else:
            step_player = random.randint(1, min(step_count, candy_count))
            if step_count < candy_count <= step_count*2:
                step_player = candy_count-step_count-1
            if candy_count <= step_count:
                step_player = candy_count
        if candy_count-step_player < 0 or step_player > step_count:
            print('Ты не можешь брать столько!')
        else:
            candy_count = candy_count-step_player
            print(f'{player_who} взял {step_player} конфет и {candy_count} осталось')
            if candy_count == 0:
                print(f'{player_who} ПОБЕДИТЕЛЬ')
            if player_who == 'Игрок':
                player_who = 'Бот'
            else:
                player_who = 'Игрок'

choice_game = int(input('В какую версию хотите поиграть? 1 - одиночная игра, 2 - игра для двух игроков -> '))
if choice_game == 1:
    candy_count = int(input('Введите количество конфет -> '))
    step_count = int(input('Введите количество шагов -> '))
    game_one_player(candy_count, step_count)
elif choice_game == 2:
    candy_count = int(input('Введите количество конфет -> '))
    step_count = int(input('Введите количество шагов -> '))
    playing_two_players(candy_count, step_count)
else:
    exit('Bye')