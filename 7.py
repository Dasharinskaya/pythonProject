# Необходимо создать функцию, которая будет генерировать список (list)
# самостоятельно в псевдослучайном порядке.
#
# Функция должна обладать аргументами, которые будут ограничивать длину списка,
# а также максимальное цифровое значение элементов этого списка.
#
# Например:
#
# Сегнерировать список из 10 чисел, каждое из
# которых может быть в диапазоне от 1 до 9.


from random import randrange


def funk(a, b, c):
    b = [randrange(b, c) for n in range(a)]
    return print(b)


funk(10, 1, 9)
