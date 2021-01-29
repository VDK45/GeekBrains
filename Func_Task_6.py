def int_func():
    a = input().title().split()
    x = len(a)
    y = []
    while x > 0:
        x -= 1
        for i_2 in a[x - 1]:

            if ord(i_2) > 122:
                y.append(x - 1)
    y = set(y)
    b = []
    for x in y:
        b.append(a[x])
    a = set(a)
    b = set(b)
    a.difference_update(b)
    a = list(a)
    a = ' '.join(a)
    return a


print(int_func())
