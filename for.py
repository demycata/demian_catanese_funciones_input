'''
# 1) Mostrar los números ascendentes desde el 1 al 10
for i in range(1, 11):
    print(i)
'''

'''
# 2) Mostrar los números descendentes desde el 10 al 1

for i in range(10, 0, -1):
    print(i)
'''
'''
num = int(input('Ingrese un numero: '))

if num > 0: 
    for i in range(0, num+1):
        print(i)
else:
    for i in range(num, 1):
        print(i)
'''
'''
num = int(input('Ingrese un numero: '))

for i in range(11):
    print(f'{num} x {i} = {num*i}')
'''
'''
acu = 0
suma = 0
for i in range(10):
    num = int(input('Ingrese un numero: '))
    if num == 0:
        break
    acu += 1
    suma+= num
print(f"Suma = {suma}, promedio = {suma/acu}")
'''
'''
for i in range(10):
    if i % 3 == 0:
        print(i)
'''
'''
num = int(input("Ingrese un número para la pirámide: "))

for i in range(1, num + 1):
    print(" " * (num - i) + str(i) * i)
'''
'''
num = int(input("Ingrese un número: "))
contador_primos = 0

for i in range(2, num + 1):
    es_primo = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(i)
        contador_primos += 1

print(f"Se encontraron {contador_primos} números primos.")
'''