# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

def Numbers():
    data = open("Lesson_5/Task_35.txt", "r")
    res = list(map(int, data.read().split(' ')))
    for i in range(1, len(res)):
        if res[i] - 1 != res[i - 1]:
            return res[i] - 1
    data.close()

print(Numbers())