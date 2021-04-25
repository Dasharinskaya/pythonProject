# Необходимо создать функцию, которая с помощью оператора IF будет
# сравнивать между собой два ее аргумента по следующей логике:
#
# Если А больше В, то вывести в консоль "Успешно"
# Если А равно В, то вывести в консоль "Почти"
# Если А меньше В, то вывести в консоль "Лузер"

firstNum = int(input('enter the number: '))
secondNum = int(input('enter the number: '))

successfullyStatus = "Успешно"
almostStatus = "Почти"
loserStatus = "Лузер"


def funk(a, b):
    if a > b:
        return successfullyStatus
    elif a == b:
        return almostStatus
    else:
        return loserStatus


result = funk(firstNum, secondNum)
print(result)
