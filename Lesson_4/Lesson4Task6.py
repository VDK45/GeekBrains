from itertools import count
from itertools import cycle


def func_count(start, stop):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


func_count(start=int(input("Введите первый номер: ")), stop=int(input("Введите последний номер: ")))


def my_cycle_func(my_list, iteration):
    i = 0
    for a in cycle(my_list):
        if i == iteration or iteration < 0:
            break
        else:
            print(a)
        i += 1


my_cycle_func(my_list=['str', 45, True, 0.3], iteration=int(input("Iteration: ")))
