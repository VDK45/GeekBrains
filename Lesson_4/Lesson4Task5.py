from functools import reduce

my_list = [a for a in range(100, 1001) if a % 2 == 0]


def my_func(prev_i, i):
    return prev_i * i


print(reduce(my_func, my_list))
