# 7. Проверить истинность утверждения ¬(X v Y v Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
print("<<Задайте значение x - y - z = 0 или 1>>")


x = int(input("Введите x = "))

y = int(input("Введите y = "))

z = int(input("Введите z = "))

print()

e = not(x or y or z)
print(f"¬ (X v Y v Z) = {int(e)}")

k = (not x) and (not y) and (not z)
print(f"¬X ⋀ ¬Y ⋀ ¬Z = {int(k)}")


print(e == k)