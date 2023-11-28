# Крестики-нолики
# ● Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

# Количество ячеек по вертикали и по горизонтали
board_side = 3
# Игровая доска
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_board():
    """Функция отрисовки игрового поля"""
    print('_' + ('_' * 4) * board_side)
    for i in range(board_side):
        print('|' + (' ' * 3 + '|')*3)
        print('|', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|') 
        print('|' + ('_' * 3 + '|') * board_side)

    # print(('_' * 4) * board_side)
    # for i in range(board_side):
    #     print((' ' * 3 + '|')*3)
    #     print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|') 
    #     print(('_' * 3 + '|') * board_side)

def game_step(index, char):
    """Функция для выполнения шага игры"""
    if (board[index - 1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True
def check_win():
    """Функция отслеживания победы"""
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),    # горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8),    # вертикальные линии
        (0, 4, 8), (2, 4, 6),               # диагональные линии
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

def validate_index(index, player):
    not_ready = True
    while (not_ready):
        if (not index.isdigit()):
            print('Вы ввели не число, попробуйте еще раз!')
            index = input(f'Ходит игрок {player}. Введите номер ячейки (0 - выход из игры): ')
        if (int(index) == 0):
            break
        elif (int(index) < 1 or int(index) > len(board)):
            print('Вы ввели число, выходящее за пределы игрового поля!')
            print('Попробуйте ввести значение снова!')
            index = (input(f'Ходит игрок {player}. Введите номер ячейки (0 - выход из игры): '))
        else:
            not_ready = False
    return int(index)

def start_game():
    # Текущий игрок
    current_player = 'X'
    # Текущий шаг
    current_step = 1
    draw_board()

    while (current_step < len(board) + 1) and (check_win() == False):
        index = input(f'Ходит игрок {current_player}. Введите номер ячейки (0 - выход из игры): ')
        index = validate_index(index, current_player)
        if (index == 0):
                print("Игра завершена!")
                break
        if (game_step(index, current_player)):
            print('Ход принят!')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            current_step += 1
        else: 
            print('Ячейка занята! Выберите другую')
        
print('Добро пожаловать в игру "Крестики-нолики"')
start_game()
