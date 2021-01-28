def division(numb_1, numb_2):
    try:
        div = numb_1 / numb_2
        return div
    except ZeroDivisionError:
        print('Невозможно делить на ноль')


a = int(input('Номер 1: '))
b = int(input('Номер 2: '))
# division(int(input('Номер 1: ')), int(input('Номер 2: ')))
print(f'Округленный результат: {round(division(a, b), 2)}')
