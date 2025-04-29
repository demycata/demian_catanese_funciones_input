
def validate_length(palabra:str, longitud:int) -> str | None:
    """
    Función para validar la longitud de una cadena de texto.
    Args:
        palabra: str: Cadena de texto a validar.
        longitud: int: Longitud exacta que debe tener la cadena.
    Returns:
        str | None: Devuelve la cadena si es válida, de lo contrario None.
    """
    flag = None
    letras = len(palabra)
    if letras == longitud:
        flag = palabra
    return flag

def validate_number(num:int, maximo:int, minimo:int,) -> int | None:
    '''
    Función para validar un número dentro de un rango específico.
    Args:
        num: str: Número a validar.
        maximo: int: Valor máximo permitido.
        minimo: int: Valor mínimo permitido.
    Returns:
        int | None: Devuelve el número entero si es válido, de lo contrario None.
    '''
    flag = None
    flag_2 = None
    no_digit = False
    for elemento in num:
        if elemento == '.':
            flag_2 = True
        if ord(elemento) < 44 or ord(elemento) > 57:
            no_digit = True   
            break
    if no_digit == False:
        if flag_2 == True:
            num = float(num)
        else:
            num = int(num)
        if num > maximo or num < minimo:
            flag = None
        else:
            flag = num
    return flag, flag_2
