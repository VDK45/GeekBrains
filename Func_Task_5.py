y = 0
while 1:
    i = input(">>> ")
    if i == 'q':
        break
    i = i.split()
    a = 0
    while a < len(i):
        try:
            i[a] = int(i[a])
        except ValueError:
            print("Value Error")
        a += 1
    x = 0
    for c in i:
        try:
            x = x + c
        except TypeError:
            print('Введите число')
    x = y + x
    print(x)
    y = x
