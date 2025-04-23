'''
#Calculadora
def suma(n1:int, n2:int) -> int:

    #Suma 2 numeros y retorna el resultado
    
    resultado = n1 + n2
    return resultado

def resta(n1:int, n2:int) -> int:

    #resta 2 numeros y retorna el resultado

    resultado = n1 - n2
    return resultado

def producto(n1:int, n2:int) -> int:
    
    #multiplica 2 numeros y retorna el resultado
    
    resultado = n1 * n2
    return resultado

def div(n1:int, n2:int) -> int:
    
    #divide 2 numeros y retorna el resultado
   
    resultado = n1 // n2
    return resultado
    
while True:
    print('---------------------------')
    print('CALCULADORA\nQUE CALCULO QUERES HACER:')
    op = int(input('[1] SUMA\n[2] RESTA\n[3] MULTIPLICACION\n[4] DIVISION\n: '))
    while op not in (1, 2, 3, 4):
        print('---------------------------')
        op = int(input('ERROR --> INGRESE UN VALOR VALIDO\n[1] SUMA\n[2] RESTA\n[3] MULTIPLICACION\n[4] DIVISION\n: '))
    numero1 = int(input('Ingrese un numero: '))
    numero2 = int(input('Ingrese otro numero: '))
    match op:
        case 1:
            resultado = suma(numero1, numero2)
            operador = '+'
        case 2:
            resultado = resta(numero1, numero2)
            operador = '-'
        case 3:
            resultado = producto(numero1, numero2)
            operador = 'x'
        case 4:
            if numero1 == 0:
                resultado = None
            else:
                resultado = div(numero1, numero2)
            operador = '/'
    if resultado != None:
        print(f"El resultado de {numero1} {operador} {numero2} es {resultado}")
    else:
        print('ERROR DE OPERACION')
    print('---------------------------')
    continuar = input("¿Quieres introducir otro número? (s/n): ").lower()
    while continuar not in ('s', 'n'):
        continuar = input("Entrada no válida. ¿Quieres introducir otro número? (s/n): ").lower()
        if continuar == 'n':
            break
'''
'''
def entero():
    numero = int(input('Ingresa un numero: '))
    return numero

print(entero())
'''
'''
def asdas():
    numero = float(input('Ingresa un numero: '))
    return numero

print(asdas())
'''
'''
def area(base, altura):
    area = base * altura
    return area

print(area(2, 3))
'''
'''
def area(radio):
    area = (radio ** 2) * 3.14 
    return area

print(area(2))
'''
'''
def par(num):
    if num % 2 == 0:
        es = True
    else:
        es = False
    return es

print(par(5))
'''
#VALIDACION DE TIPOS DE DATOS
'''
while True:
    num = input('Ingrese un numero: ')
    try:
        num = int(num)
        break
    except ValueError:
        print("ERROR --> Ingrese un numero correcto")
'''
'''
#VALIDACION DE DATOS RE GRONCHO
def verifica_dato_numerico(cadena:str) -> bool:
    flag = True
    for elemento in cadena:
        if ord(elemento) < 48 or ord(elemento) > 57:
            flag = False
            break
    
    return flag

dato2 = "15a"

es_numero = verifica_dato_numerico(dato2) 

while es_numero == False:
    dato2 = input("Error, ingrese un dato numérico: ")
    es_numero = verifica_dato_numerico(dato2) 
    
    
print(verifica_dato_numerico(dato2))

dato2 = int(dato2)

print(dato2)
'''