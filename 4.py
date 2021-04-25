def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


a = int(input('enter the number: '))
b = int(input('enter the number: '))

firstFunk = add(a, b)
secondFunk = sub(a, b)
thirdFunk = mul(a, b)
fourthFunk = div(a, b)

print(firstFunk)
print(secondFunk)
print(thirdFunk)
print(fourthFunk)
