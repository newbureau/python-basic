"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]




def is_prime(input_number):
    """
    Функция, которая проверяет простое ли число.
    :param input_number: одно число
    :return: `True` / `False`
    """
    if input_number < 2:
        return False
    divisor = 2
    while divisor <= input_number ** (0.5):
        if (input_number % divisor == 0):
            return False
        divisor += 1
    else:
        return True




def filter_numbers(numbers_list, filter_type = ODD):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    >>> filter_numbers([1, 3, 4, 5], PRIME)
    <<< [3, 5]
    """
    if filter_type == ODD:
        return [number for number in numbers_list if number % 2 != 0]
    if filter_type == EVEN:
        #filter(number % 2 == 0, numbers_list)
        return [number for number in numbers_list if number % 2 == 0]
    if filter_type == PRIME:
        return list(filter(is_prime, numbers_list))



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"
print (power_numbers(1, 2, 5, 7))
print (filter_numbers([1, 2, 3], ODD))
print (filter_numbers([2, 3, 4, 5], EVEN))
print (filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], PRIME))
