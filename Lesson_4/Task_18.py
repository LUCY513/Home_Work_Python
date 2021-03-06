# 18. Вычислить число pi c заданной точностью d
#	Пример: при d = 0.001,  = 3.141. 10^-1 <= d <= 10^-10

import math

def Pi(d):
    if 0.1 >= d >= 10**-10:                         # ограничиваем диапазон
        result = len(str(d))-2                   # переводим в строку и считаем количество
        pi = math.pi
        newPi = round(pi, result)
    else:
        newPi = 'd не в заданном диапазоне'
    return newPi


d = 0.001                                           # int(input('Введите коэффициент точности от 10**-1 до 10**-10'))

print(Pi(d))
