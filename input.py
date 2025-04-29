from validate import *


def get_int(mensaje: str, mensaje_error: str, minimo:int, maximo:int, reintentos:int) -> int | None:
    """
    Función para validar un número entero dentro de un rango específico.
    Args:
        mensaje: str: Mensaje que se muestra al usuario para ingresar el número.
        mensaje_error: str: Mensaje de error que se muestra si la validación falla.
        minimo: int: Valor mínimo permitido.
        maximo: int: Valor máximo permitido.
        reintentos: int: Número de intentos permitidos para ingresar un valor válido.
    Returns:
        int | None: Devuelve el número entero ingresado si es válido, de lo contrario None.
    """
    flag = None
    print(mensaje)
    for i in  range(reintentos):
        num = input(f'Ingrese un entero entre {minimo} y {maximo}, tenes {reintentos} intentos: ')
        flag, flag_2 = validate_number(num, maximo, minimo)
        if flag == None or flag_2 == True: 
            print(mensaje_error)
        else:
            break
    return flag
    
def get_float(mensaje: str, mensaje_error: str, minimo:int, maximo:int, reintentos:int) -> float | None:
    """
    Función para validar un número flotante dentro de un rango específico.
    Args:
        mensaje: str: Mensaje que se muestra al usuario para ingresar el número.
        mensaje_error: str: Mensaje de error que se muestra si la validación falla.
        minimo: int: Valor mínimo permitido.
        maximo: int: Valor máximo permitido.
        reintentos: int: Número de intentos permitidos para ingresar un valor válido.
    Returns:
        int | None: Devuelve el número flotante ingresado si es válido, de lo contrario None.
    """
    flag = None
    print(mensaje)
    for i in  range(reintentos):
        num = input(f'Ingrese un float entre {minimo} y {maximo}, tenes {reintentos} intentos: ')
        flag, flag_2 = validate_number(num, maximo, minimo)
        if flag == None:
            print(mensaje_error)
        else:
            flag = float(flag)
            break
    return flag
    
def get_str(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> str |None: 
    """
    Función para validar una cadena de texto con una longitud específica.
    Args:
        mensaje: str: Mensaje que se muestra al usuario para ingresar la cadena.
        mensaje_error: str: Mensaje de error que se muestra si la validación falla.
        longitud: int: Longitud exacta que debe tener la cadena.
        reintentos: int: Número de intentos permitidos para ingresar un valor válido.
    Returns:
        str | None: Devuelve la cadena ingresada si es válida, de lo contrario None.
    """
    flag = None
    print(mensaje)
    for i in  range(reintentos):
        palabra = input(f'Ingrese una string con un maximo de {longitud} caracteres, tenes {reintentos} intentos: ')
        flag = validate_length(palabra, longitud)
        if flag == None:
            print(mensaje_error)
        else:
            break
    return flag


mensaje = f'Vamos a validar tu input!!\n-------------------------'
mensaje_error = 'ERROR AL VALIDAR TU DATO'
reintentos = 3

'''
print(get_float(mensaje, mensaje_error, 2, 10, reintentos))
print('-------------------------')
print(get_int(mensaje, mensaje_error, 2, 10, reintentos))
print('-------------------------')
print(get_str(mensaje, mensaje_error, 4, reintentos))
'''