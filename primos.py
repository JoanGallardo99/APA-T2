
"""
Nom i cognoms: Joan Gallardo Caparrós
Mòdul que defineix funcions amb nombres primers.

>>> esPrimo(4)
False

>>> esPrimo(-2)
True

>>> esPrimo(-4)
True
"""

def esPrimo(numero):
    """
    esPrimo retorna True si el nombre introduit es primo.
    False en cas contrari.

    >>> esPrimo(1023)
    False

    >>> esPrimo(1021)
    True
    """

    for prova in range(2, numero):
        if numero%prova == 0:
            return False
        
    return True

def primos(numero):
    """
    Develve una tupla con todos los números primos menores que su argumento.

    >>> primos(13)
    (1, 2, 3, 5, 7, 11)

    >>> primos(7)
    (1, 2, 3, 5)

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    tupla = ()
    for i in range(1, numero):
        if esPrimo(i):
            tupla += (i,)

    return tupla

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    tupla = ()
    divisor = 2

    while numero > 1:
        while numero % divisor == 0:
            tupla += (divisor,)
            numero = numero // divisor
        divisor += 1

    return tupla


if __name__ == "__main__":
    import doctest
    doctest.testmod()