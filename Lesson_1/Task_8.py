# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

print("Findt point coordinate")

x = int(input("Enter coordinate X -> "))
y = int(input("Enter coordinate Y -> "))

if x > 0 and y > 0: print("I quarter")            # quarter - четверть
elif x < 0 and y > 0: print("II quarter")
elif x < 0 and y < 0: print("III quarter")
elif x > 0 and y < 0: print("IV quarter")
else: print("You beginning point coordinate")