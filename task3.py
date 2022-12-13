# 3-Создайте программу для игры в ""Крестики-нолики"".
# Предложено игровое поле вида [['*','*','*']],[['*','*','*']],[['*','*','*']]

# from typing import list

def draw_gamefield(game_field: list[str]):
    """
    Выводит игровое поле в виде трех строк по три позиции
    """
    for line in game_field:
        print(line)


def put_simbol(simbol: str):
    """
    Запрашивает позицию и устанавливает символ X или O
    """
    simbol_insert = False
    while not simbol_insert:
        answer = input(f'Введите позицию игрового поля (Две цифры через пробел) куда поставить символ -> ').split(' ')
        answer_line = answer[0]
        answer_pos = answer[1]
        try:
            answer_line = int(answer_line)
            answer_pos = int(answer_pos)
        except ValueError:
            print('Ошибка ввода. Нужно ввести два числа через пробел')
            continue
        if 0 < answer_line <= 3 and 0 < answer_pos <= 3:
            line = game_field[answer_line-1]
            if line[answer_pos-1] not in "XO":
                line[answer_pos-1] = simbol
                simbol_insert = True
            else:
                print('Клетка уже занято, введите другое значение')
        else:
            print('Ошибка ввода. Нужно ввести два числа через пробел')


def check_win_line(game_field: list[str]) -> bool or str:
    """
    Выполняет проверку выигрышной комбинации на игровом поле
    """
    now_line = []
    win_line = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for line in game_field:
        for s in line:
            now_line.append(s)
    for block in win_line:
        if now_line[block[0]] == now_line[block[1]] == now_line[block[2]]:
            return now_line[block[0]]
    return False


game_field = [['1 1', '1 2', '1 3'], ['2 1', '2 2', '2 3'], ['3 1', '3 2', '3 3']]

draw_gamefield(game_field)

for counter in range(9):
    if counter % 2 == 0:
        put_simbol(' X ')
    else:
        put_simbol(' O ')

    draw_gamefield(game_field)

    simbol = check_win_line(game_field)

    if simbol:
        print(f'Игрок {simbol} - ПОБЕДИТЕЛЬ!')
        break
    if counter == 8:
        print('Ничья!')
        break

print('Bye!')
