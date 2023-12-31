# Домашнее задание
# ● Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# ● Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9



input_number = int(input("Введите число для вывода таблицы умножения всех чисел до данного числа: "))
while(input_number == 0):
    print('Введенное число не может быть нулем!')
    input_number = int(input("Введите число для вывода таблицы умножения всех чисел до данного числа: "))


print('\nСтруктурная парадигма \n')
# Структурная парадигма
# последовательное исполнение структурированных блоков без goto
# однократное выполнение следующей написанной операции
# ветвление (в нашем случае его не будет)
# цикл

string = ""
for number in range(1, input_number + 1):
    for num in range(0, 11):
        string += f'{number} x {num} = {number * num} \n' 
    string += '\n'

print(string)

print('-------------------- \n')

# Процедурная парадигма
# Это императивный стиль, заключаемый в последовательности команд и вызовов процедур
# в нашем случае процедура mult_table, идущая за стандартной подпрограммой-процедурой print 


def mult_table(input_num):
    string = ""
    for number in range(1, input_num + 1):
        for num in range(0, 11):
            string += f'{number} x {num} = {number * num} \n' 
        string += '\n' 
    print(string)

print('Процедурная парадигма \n')
mult_table(input_number)