# 36. Дан список чисел. Создать список в который попадают числа,
# описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#        [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя
from random import randint


size = 20
list_0 = [randint(1, 21) for i in range(size + 1)]
# list_0 = [5, 2, 4, 6, 5, 7, 6, 8, 1, 9, 13, 10]
list_result = []


for k in range(len(list_0) - 1):
    index = k
    lis = [list_0[k]]

    while index < len(list_0) - 1:
        rem_list = [i for i in list_0[index:] if i > lis[-1]]

        if len(rem_list) != 0:
            min_list = min(rem_list)
        else:
            break

        lis.append(min_list)
        index += list_0[index:].index(min_list)

    if len(lis) > len(list_result):
        list_result = lis.copy()

print(list_result)
