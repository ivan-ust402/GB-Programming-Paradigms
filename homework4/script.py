# Корреляция
# ● Контекст
# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.
from statistics import mean
from functools import reduce

list1 = [2, 4, 6, 8]
list2 = [1, 3, 7, 13]
# list2 = [1, 1, 1, 1] # Проверка деления на ноль
# list1 = [2, 4, 6, 8]
# list2 = [2, 4, 10, 12]


def pearson_correlation(x_list, y_list):
    """Функция расчета коэфициента корреляции Пирсона"""
    try:
        average_x = mean(x_list)
        average_y = mean(y_list)

        # Расчет числителя
        dif_x_average_x_list = list(map(lambda x: x - average_x, x_list))
        dif_y_average_y_list = list(map(lambda y: y - average_y, y_list))
        numerator_list = list(map(lambda x, y: x * y, dif_x_average_x_list, dif_y_average_y_list))
        numerator = reduce(lambda x, y: x + y, numerator_list)

        # Расчет знаменателя
        pow_dif_x_list = list(map(lambda x: x**2, dif_x_average_x_list))
        pow_dif_y_list = list(map(lambda y: y**2, dif_y_average_y_list))
        sum_pow_dif_x = reduce(lambda x, y: x + y, pow_dif_x_list)
        sum_pow_dif_y = reduce(lambda x, y: x + y, pow_dif_y_list)
        sqrt_sum_x = pow(sum_pow_dif_x, 0.5)
        sqrt_sum_y = pow(sum_pow_dif_y, 0.5)
        denominator = sqrt_sum_x * sqrt_sum_y

        # if denominator == 0:
        #     raise Exception('!!! При расчете в знаменателе получился ноль! перепроверьте входные данные!')

        # Коэффициент Корелляции Пирсона
        return round(numerator / denominator, 3)
    
    # except Exception as ex:
    #     return ex.args[0]
    except ZeroDivisionError as err:
        return f'Ошибка при расчете: "{err}", проверьте входные данные!'

    

pearson_coefficient = pearson_correlation(list1, list2) # Ожидаемый ответ: 0.976, сильная положительная линейная связь

print(f'Коэффицент корелляции Пирсона для списка {list1} и {list2} равен: {pearson_coefficient}')