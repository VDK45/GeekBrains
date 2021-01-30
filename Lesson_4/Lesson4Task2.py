a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [print(j) for j in a[1:] if a[a.index(j)] > a[a.index(j) - 1]]

print('-' * 7, )
new_2 = [print(a[i]) for i in range(1, len(a)) if a[i] > a[i - 1]]
