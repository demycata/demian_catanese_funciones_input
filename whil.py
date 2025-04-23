'''
suma = 0
contador = 0

while True:
    numero = int(input("Introduce un número: "))
    suma += numero
    contador += 1
    continuar = input("¿Quieres introducir otro número? (s/n): ").strip().lower()
    while continuar not in ('s', 'n'):
        continuar = input("Entrada no válida. ¿Quieres introducir otro número? (s/n): ").strip().lower()
    if continuar == 'n' and contador >= 5:
            break
    if continuar == 'n':
            print("Debes introducir al menos 5 números.")

print(f"La suma de los números introducidos es: {suma}")
print(f"El promedio de los números introducidos es: {suma / contador}")
'''
'''
suma = 0
contador = 0

for i in range(10):
    numero = int(input("Introduce un número: "))
    suma += numero
    contador += 1
    continuar = input("¿Quieres introducir otro número? (s/n): ").lower()
    while continuar not in ('s', 'n'):
        continuar = input("Entrada no válida. ¿Quieres introducir otro número? (s/n): ").lower()
    if continuar == 'n' and contador >= 5:
            break
    if continuar == 'n': 
            print("Debes introducir al menos 5 números.")

print(f"La suma de los números introducidos es: {suma}")
print(f"El promedio de los números introducidos es: {suma / contador}")
'''
'''

clave = "clave123"
ingresoclave = input("Ingrese la clave: ")
intentos = 0

while clave != ingresoclave:
    ingresoclave = input("CLAVE INCORRECTA. Ingrese la clave: ")
    intentos += 1
    if intentos == 2 and ingresoclave != clave:
        print('INTENTOS SUPERADOS')
        break
if ingresoclave == clave:
    print("CLAVE CORRECTA")
'''
'''
sumaneg = 0
sumapos = 0
negins = 0
posins = 0
max = None
ingresos_totales = 0

while True:
    numero  = int(input("Ingrese un numero: "))
    if numero < 0:
        sumaneg += numero
        negins += 1
    if numero > 0:
        if max == None:
             max = numero
        if numero > max:
             max = numero
        sumapos += numero
        posins += 1
    ingresos_totales += 1
    continuar = input("¿Quieres introducir otro número? (s/n): ").lower()
    while continuar not in ('s', 'n'):
        continuar = input("Entrada no válida. ¿Quieres introducir otro número? (s/n): ").lower()
    if continuar == 'n':
            break
    
print(f"La suma acumulada de los números negativos es: {sumaneg}")
print(f"La suma acumulada de los números positivos es: {sumapos}")
print(f"La cantidad de números negativos ingresados es: {negins}")
print(f"El promedio de los números positivos es: {sumapos/posins}")
print(f"El número positivo más grande es: {max}")
print(f"El porcentaje de números negativos ingresados, respecto del total de ingresos es: {(negins*100)/ingresos_totales}%")
'''
'''
nota = int(input("Ingrese una nota: "))
while nota > 10 or nota < 0:
    nota = int(input("ERROR. Porfavor ingrese una nota valida: "))

print(f"Tu nota es: {nota}")
'''
""""
while True:
    color = input("Ingrese un color (Rojo, Verde o Azul): ").strip().lower()
    if color in ("rojo", "verde", "azul"):
        break  # Sale del bucle si el color es válido
    else:
        print("Error: El color ingresado no es válido. Por favor, ingrese Rojo, Verde o Azul.")
"""
'''
apellido = input('Ingrese su apellido: ')

while True:
    edad = int(input('Ingrese su edad: '))
    if edad >= 18 and edad <= 90:
        break
    else:
        print('ERROR ==> LA EDAD INGRESADA NO ES VALIDA. PORFAVOR INGRESAR UNA EDAD VALIDA')

while True:
    estado_civil = input('Ingrese su Estado civil (“Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”): ').lower()
    if estado_civil in ("soltero", "soltera", "casado", "casada", "divorciado", "divorciada", "viudo", "viuda"):
        break
    else:
        print('ERROR ==> EL ESTADO CIVIL INGRESADO NO ES VALIDO. PORFAVOR INGRSE UN ESTADO CIVIL VALIDO')

legajo = int((input('Ingrese su numero de legajo: ')))

while legajo > 9999 or legajo < 1000:
    legajo = int(input('ERROR ==> EL NUMERO DE LEGAJO NO ES VALIDO. PORFAVOR INGRESAR UN NUMERO VALIDO: '))

print(f"Su apellido es {apellido}")
print(f'Su estado civil es {estado_civil}')
print(f'Su numero de lejao es {legajo}')
'''
'''
encuestados = 0
hombres_IOT_IA_entre25y50 = 0
empleados_noIA = 0
edadMax = None
nombreMAX = None
tecnoMax = None
'''
'''
print('Encuesta para empleados')

for empleados in range(10):

    nombre = input('Ingrese su nombre: ')

    edad = int(input('Ingrese su edad: '))

    while edad < 18:
        edad = int(input('Ingrese una edad valida (+18): '))
    if edadMax == None:
        edadMax = edad

    while True:
        genero = input('Ingrese un genero valido (Masculino , Femenino, Otro): ').strip().lower()
        if genero in ("masculino", "femenino", "otro"):
            break
        else:
            print('Respuesta no valida. Por favor ingrese un genero valido.')

    while True:
        tecno = input('Ingrese la Tecnología elegida (IA, RV/RA, IOT): ').strip().lower()
        if tecno in ("ia", "rv/ra", "iot"):
            break
        else:
            print('Respuesta no valida. Por favor ingrese una tecnologia valido.')
    
    encuestados += 1

    if genero == 'masculino' and tecno == 'ia' or tecno == 'iot' and edad >= 25 and edad <= 50:
        hombres_IOT_IA_entre25y50 += 1
    
    if genero != 'femenino' and edad > 33 and edad < 40:
        empleados_noIA += 1

    if edad > edadMax:
        edadMax = edad
        nombreMAX = nombre
        tecnoMax = tecno

tecnoMax = tecnoMax.upper

print(f'Cantidad de empleados encuestados: {encuestados}')
print("")
print(f'Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive): {hombres_IOT_IA_entre25y50}')
print("")
print(f'Porcentaje de empleados que NO votaron por IA: {(empleados_noIA*100)/encuestados}%')
print("")
print(f'El empleado mas grande es {nombreMAX} con {edadMax} anos y su tecnologia es {tecnoMax}')
'''

'''
TB_cargofijo = 7000    #TB es Tarifa base
TB_costometro = 200

metros = int(input('Cantidad de metros consumidos: '))
cliente = input('Ingrese que tipo de cliente es (Residencial, Comercial o Industrial): ').lower
while cliente not in ('residencial', 'comercial', 'industrial'):
    cliente = input('ERROR ==> El tipo de cliente ingresado no es valido. Porfavor ingresar un tipo de cliente valido: ').lower()
bonificaciones = 0
recargo = 0
iva = 21

if cliente == 'residencial':
    if metros < 30:
        bonificaciones += 10
    elif metros > 80:
        recargo -= 15

if cliente == 'comercial':
    if metros > 300:
        bonificaciones += 12
    elif metros > 150:
        bonificaciones += 8
    elif metros > 50: 
        recargo -= 5
if cliente == 'industrial':
    if metros > 1000:
        bonificaciones += 30
    elif metros > 500:
        bonificaciones += 20
    elif metros > 200:
        recargo = -10
subtotal = TB_cargofijo + (TB_costometro * metros) 
subbtotalplus = TB_cargofijo + (TB_costometro * metros) - bonificaciones + recargo
con_iva = subbtotalplus * (iva / 100)
total = subbtotalplus + con_iva

print(f'Tu subtotal es; ${subtotal} ')
print(f'Tu bonificacion es: %{bonificaciones}')
print(f'Tu recargo es: %{recargo}')  
print(f'Tu subtotal con bonificaciones y recargos es: ${subbtotalplus}')
print(f'El IVA es: ${con_iva}')  
print(f'Tu total es: ${total}')
'''