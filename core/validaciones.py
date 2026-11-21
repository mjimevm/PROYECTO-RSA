
# Validaciones para el sistema RSA

from core.algoritmos import mcd


# Verificar si un numero es primo
def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


# Verificar los numeros primos
def validar_primos(p, q):
    if not es_primo(p):
        return False

    if not es_primo(q):
        return False

    if p == q:
        return False

    return True


# Verificar el exponente
def validar_exponente(e, total_coprimos):
    if e <= 1:
        return False

    if mcd(e, total_coprimos) != 1:
        return False

    return True


# Verificar el modulo n
def validar_modulo(n):
    if n <= 126126 or n >= 1000000:
        return False

    return True


# Verificar los caracteres permitidos
def validar_mensaje(mensaje):
    if mensaje == "":
        return False

    for letra in mensaje:
        codigo = ord(letra)

        if codigo < 32 or codigo > 126:
            return False

    return True
