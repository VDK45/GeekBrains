def my_func(x, y):
    try:
        x = float(input('Number X > 0: '))
        y = int(input('Number y < 0: '))
    except ValueError:
        print('Wrong number!')
    if x > 0 and y < 0:
        y = abs(y)
        a = x
        for i in range(y - 1):
            a *= x
        # result = 1 / (x ** abs(y))
        return print('{} степенью -{} будет  {}'.format(x, y, 1 / a))
    else:
        print('Need x > 0 and y < 0')


my_func(0, 0)
