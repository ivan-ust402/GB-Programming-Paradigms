# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
from random import randint

def get_random_list():
    N = 10
    a = []
    for i in range(N):
        a.append(randint(1, 99))
    print(f'Лист с рандомными числами: {a}')
    return a

 
def sort_list_imperative(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

list = get_random_list()

print(f'Отсортированный лист в императивном стиле: {sort_list_imperative(list)}')

# 💡 Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers
    
print(f'Отсортированный лист в декларативном стиле: {sort_list_declarative(list)}')
