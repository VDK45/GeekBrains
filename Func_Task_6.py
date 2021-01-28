def int_func():
    a = input().title().split()
    x = len(a)
    while x > 0:
        x -= 1
        for i_2 in a[x - 1]:
            if ord(i_2) > 122:
                a[x - 1].lower()
                print(a[x - 1])

    return a


print(int_func())
