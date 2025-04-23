'''
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...

'''
nota = int(input('Ingrese la nota: '))

if nota in (6, 7, 8, 9, 10):
    print(f'Promocion directa, la nota es {nota}')
elif nota in (4, 5):
    print(f'Aprobado su nota es {nota}')
else:
     print(f'Desaprobado su nota es {nota}')