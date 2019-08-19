lista1 = []
n = 0
cont = 0
promedio = 0
for x in range(0, 10):
    datos =int(input("Digite un valor: "))
    lista1.append(datos)
    promedio = promedio + lista1[x]
    if lista1[x] == 5:
        n += 1
    if lista1[x] > cont:
        cont = lista1[x]

print(lista1)
print("numero mayor es: ", cont)
print("promedio: ", promedio / 10)
print("Hay", n, " 5")