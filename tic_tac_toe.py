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

def draw_board(board, board_side):
    """Функция отрисовки игрового поля"""
    print('_' + ('_' * 4) * board_side)
    for i in range(board_side):
        print('|' + (' ' * 3 + '|')*3)
        print('|', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|') 
        print('|' + ('_' * 3 + '|') * board_side)
    print('')

def game_step(index, char, board):
    """Функция для выполнения шага игры"""
    if (board[index - 1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True

def check_win(board):
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

def validate_index(player, board):
    """Функция валидации входного параметра"""
    not_ready = True
    while (not_ready):
        index = input(f'Ходит игрок {player}. Введите номер ячейки (0 - выход из игры): ')
        if (not index.isdigit()):
            print('Вы ввели не число, попробуйте еще раз!')
            continue
        if (int(index) == 0):
            break
        elif (int(index) < 1 or int(index) > len(board)):
            print('Вы ввели число, выходящее за пределы игрового поля!')
            print('Попробуйте ввести значение снова!')
            continue
        else:
            not_ready = False
    
    return int(index)

def start_game():
    # Количество ячеек по вертикали и по горизонтали
    board_side = 3
    # Игровая доска
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Текущий игрок
    current_player = 'X'
    # Текущий шаг
    current_step = 1
    draw_board(board, board_side)

    while (current_step < len(board) + 1) and (check_win(board) == False):
        index = validate_index(current_player, board)
        if (index == 0):
                break
        if (game_step(index, current_player, board)):
            print('')
            print('Ход принят!')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board(board, board_side)
            current_step += 1
        else: 
            print('Ячейка занята! Выберите другую')
    if (current_step == len(board) + 1 and check_win(board) == False):
        print('Игра завершена. Ничья!')
    elif (index == 0):
        print("Игра завершена!")
    else:
        print('Игра завершена с победой игрока ' + check_win(board) + '!!!')


while True:        
    print('Добро пожаловать в игру "Крестики-нолики"!')
    start_game()
    print()
    continue_play = input('Хотите сыграть еще? (введите "Yes" для продолжения): ')
    if continue_play.strip().lower() == 'yes':
        print('')
        continue
    else:
        break

# При разработке игры были использованы императивный (последовательность команд и вызовов процедур, набор инструкций), структурный (есть циклы и ветвления, goto отсутствует) и процедурный (использование функций) подходы. Если я правильно понимаю, возможно, еще есть декларативная парадигма, т.к. я использовал методы "из коробки" для работы со строками, такие как strip(), lower(), isdigit() (работа данных функций от нас скрыта под капотом). Т.к. я не использовал классы и объекты подхода ООП в данном решении нет. 