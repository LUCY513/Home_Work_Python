# 17. Найти наименьшее общее кратное двух чисел

print("<<Общее кратное двух чисел>>")

getNum1 = int(input("Enter first number -> "))
getNum2 = int(input("Enter second number -> "))

def Nok(x, y):
    if x > y: nok = x                               # - находим максивмльное из двух чисел  
    else: nok = y

    while(True):                                    # - делим числа на максимально число, так мы найдем общее НОК которые = 0 
        if((nok % x == 0) and (nok % y == 0)):      # 
            result = nok
            break
        nok += 1
    return result

print(f"Общее кратное чисел**: {getNum1}, {getNum2} = {Nok(getNum1, getNum2):}")