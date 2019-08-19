import random
n = int(input("cuantos numeros desea generar"))
list=[]
num=0
for i in range(0, n):
    num = random.randint(0,50)
    list.append(num)

print(list)