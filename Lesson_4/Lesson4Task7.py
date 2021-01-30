from math import factorial

n = int(input('Enter n: '))


def fact(n):
    yield factorial(n)


for el in fact(n):
    print(el)
