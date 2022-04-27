# 19. Составить список простых множителей натурального числа N

num = int(input("Integer: "))

for i in range(1, num+1):
    if(num %i ==0):
        print(i, end = ' ')