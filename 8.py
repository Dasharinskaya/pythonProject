# Необходимо написать функцию, которая будет брать два случайно сгенерированных списка (задача №7)
# и сравнивать их между собой.
#
# Уникальные числа (которые есть только в одном списке)
# выводить в консоль с любым комментарием.


from random import randrange


first_random_list = [randrange(1, 9) for n in range(10)]
second_random_list = [randrange(1, 9) for n in range(10)]

print(first_random_list)
print(second_random_list)


def funk(a, b):
    comparison = list(set(a) ^ set(b))
    comparison_to_string = ", ".join(str(x) for x in comparison)
    result = comparison_to_string + " - это уникальное(-ые) числа"
    return print(result)


funk(first_random_list, second_random_list)
