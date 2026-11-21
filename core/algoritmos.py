
# Algoritmos matematicos para RSA


# Calcular el maximo comun divisor
def mcd(a, b):
    while b != 0:
        residuo = a % b
        a = b
        b = residuo

    return a



# Calcular el inverso modular con Euclides extendido
def inverso_modular(e, total_coprimos):
    a = e
    b = total_coprimos

    x1 = 1
    x2 = 0

    while b != 0:
        cociente = a // b

        a, b = b, a % b
        x1, x2 = x2, x1 - cociente * x2

    if a != 1:
        return None

    d = x1 % total_coprimos

    return d



# Calcular potencias modulares sin utilizar pow()
def potencia_modular(numero, exponente, modulo):
    resultado = 1
    numero = numero % modulo

    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * numero) % modulo

        numero = (numero * numero) % modulo
        exponente = exponente // 2

    return resultado
