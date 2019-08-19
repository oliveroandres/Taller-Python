n = int(input("ingrese la cantidad de nmeros : "))

for i in range(0, n):
    if i % 3 == 0:
        print(i, "fizz")
    if i % 5 == 0:
        print(i, "Buzz")
    if (i % 3 == 0) and (i % 5 == 0):
        print(i, "fizzBuzz")
    if (i % 3 != 0) and (i % 5 != 0):
        print(i, "NO ES MULTIPLO DE 3 NI 5")