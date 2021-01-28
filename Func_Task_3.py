def my_func(a, b, c):
    x = a + b
    y = b + c
    z = c + a
    if x > y and x > z:
        return print(f'Max sum {a} + {b} = {x}')
    elif y > x and y > z:
        return print(f'Max sum {b} + {c} = {y}')
    elif z > x and z > y:
        return print(f'Max sum {a} + {c} = {z}')


try:
    my_func(int(input('Number a: ')), int(input('Number b: ')), int(input('Number c: ')))
except ValueError:
    print('Wrong number!')
