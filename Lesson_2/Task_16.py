# 16. Написать программу проверки, является ли строка палиндромом

inOut = input("Enter numbers -> ")

if inOut == inOut[:: - 1]: print("Palindrom")
else: print("Not palindrom")