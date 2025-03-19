
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
    (2, 3, 5, 7, 11)

    >>> primos(7)
    (2, 3, 5)

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    tupla = ()
    for i in range(2, numero):
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

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    
    >>> mcm(90, 14)
    630
    """
    descomp1 = descompon(numero1)
    descomp2 = descompon(numero2)

    # Obtenemos los factores primos de cada número
    factores = set(descomp1 + descomp2)

    mcm_factors = []
    
    # Para cada factor primo, tomamos el máximo exponente de cada número
    for factor in factores:
        mcm_factors.append(factor ** max(descomp1.count(factor), descomp2.count(factor)))
    
    # El MCM es el producto de los factores primos con sus máximos exponentes
    resultado = 1
    for factor in mcm_factors:
        resultado *= factor
    
    return resultado
    
def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> mcd(924, 780)
    12
    """
    descomp1 = descompon(numero1)
    descomp2 = descompon(numero2)

    # Obtenemos los factores primos comunes de cada número
    factores = set(descomp1) & set(descomp2)

    mcd_factors = []
    
    # Para cada factor primo, tomamos el máximo exponente de cada número
    for factor in factores:
        mcd_factors.append(factor ** min(descomp1.count(factor), descomp2.count(factor)))
    
    # El MCM es el producto de los factores primos con sus máximos exponentes
    resultado = 1
    for factor in mcd_factors:
        resultado *= factor
    
    return resultado


if __name__ == "__main__":
    import doctest
    doctest.testmod()