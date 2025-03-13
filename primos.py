
"""
Nom i cognoms: Joan Gallardo Caparrós
Mòdul que defineix funcions amb nombres primers.

>>> esPrimo(4)
False

>>> esPrimo(-2)
True

>>> esPrimo(-4)
False
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()