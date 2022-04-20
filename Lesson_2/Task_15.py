#15. Дано количество секунд. Вывести результат в виде: дни:часы:минуты:секунды 

second = int(input("Enter secunds - > "))

def Time():
    if second >= 86400:
        day = second // 86400                    # 1 day - 86400 sec
        print(f"Day: {day} ")
    else: print("Day: 0")

    if second >= 3600:
        hour = second // 3600                    # 1 hours - 3600 sec
        print(f"Hours: {hour} ")
    else: print("Hours: 0")

    if second >= 60:
        minute = second // 60                    # 1 minute - 60 sec
        print(f"Minute: {minute} ")
    return 

Time()