# 34. Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.

file = open('Lesson_5/Task_34.txt', 'r')
list_0 = []

for i in file:
    list_0.append(i)

list_1 = list_0[0].split(' ')
list_2 = list_0[1].split(' ')


def list4(lis): return [i for i in lis if i not in {'+', '=', '0\n', '0'}]


print(list_1 := list4(list_1))
print(list_2 := list4(list_2))
print()


def high_degree(list):
    for i in list:
        num = (i.index('^'))
        num = int(i[num + 1])
        break
    return num


hidegree1 = high_degree(list_1)
hidegree2 = high_degree(list_2)


def degree(list, x, y):
    while x - y != 0:
        list.reverse()
        list.append('0')
        list.reverse()
        x -= 1
    return list


if hidegree1 > hidegree2:
    list_2 = degree(list_2, hidegree1, hidegree2)
else:
    list_1 = degree(list_1, hidegree2, hidegree1)


def list_num(list, li):
    result = []
    for i in list:
        if i not in list[-1]:
            if '^' not in i:
                result.append((int(i)))
            else:
                num1 = i.index('^')
                num1 = int(i[num1 + 1:])
                num2 = i.index('*')
                num2 = int(i[0: num2])

                while li - num1 >= 1:
                    result.append(0)
                    li -= 1
            result.append(num2)
            li -= 1
        else:
            if '^' not in i:
                result.append(int(i))
            else:
                num1 = i.index('^')
                num1 = int(i[num1 + 1:])
                num2 = i.index('*')
                num2 = int(i[0: num2])

                while li - num1 >= 1:
                    result.append(0)
                    li -= 1

                while num1 != 1:
                    result.append(0)

            result.append(num2)
            result.append(0)

    return result


print(list_format1 := list_num(list_1, hidegree1))
print(list_format2 := list_num(list_2, hidegree2))

list_result = [x + y for x, y in zip(list_format1, list_format2)]
print()
print(f"result -> {list_result}")