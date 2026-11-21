
# Sistema de encriptacion RSA

from core.algoritmos import inverso_modular, potencia_modular
from core.validaciones import (
    validar_primos,
    validar_exponente,
    validar_modulo,
    validar_mensaje
)
from core.ascii_utils import texto_a_numeros, numeros_a_texto


# Generar las claves RSA
def generar_claves(p, q, e):

    if not validar_primos(p, q):
        raise ValueError("p y q deben ser primos diferentes")

    n = p * q
    total_coprimos = (p - 1) * (q - 1)

    if not validar_modulo(n):
        raise ValueError("n debe estar entre 126126 y 1000000")

    if not validar_exponente(e, total_coprimos):
        raise ValueError("El exponente e no es valido")

    d = inverso_modular(e, total_coprimos)

    return n, d


# Encriptar un mensaje
def encriptar(mensaje, p, q, e):

    n, d = generar_claves(p, q, e)

    if not validar_mensaje(mensaje):
        raise ValueError("El mensaje contiene caracteres no validos")

    # Guardar la longitud original
    L = len(mensaje)

    # Agregar relleno si la longitud es impar
    if L % 2 != 0:
        mensaje += " "

    # Convertir a bloques ASCII
    bloques = texto_a_numeros(mensaje)

    cifrados = []

    for bloque in bloques:
        numero = potencia_modular(bloque, e, n)
        cifrados.append(str(numero).zfill(6))

    resultado = " ".join(cifrados)

    return resultado, L


# Desencriptar un mensaje
def desencriptar(mensaje_cifrado, L, p, q, e):

    n, d = generar_claves(p, q, e)

    # Verificar que el cifrado tenga un formato correcto
    if mensaje_cifrado == "":
        raise ValueError("El mensaje cifrado esta vacio")

    if "\n" in mensaje_cifrado or "\t" in mensaje_cifrado:
        raise ValueError("No se permiten saltos de linea ni tabulaciones")

    if mensaje_cifrado.startswith(" ") or mensaje_cifrado.endswith(" "):
        raise ValueError("No debe haber espacios al inicio o al final")

    if "  " in mensaje_cifrado:
        raise ValueError("Los bloques deben separarse por un solo espacio")

    bloques = mensaje_cifrado.split(" ")
    numeros = []


    if len(bloques) == 0:
        raise ValueError("El mensaje cifrado esta vacio")

    # Verificar la longitud original
    if L != len(bloques) * 2 and L != len(bloques) * 2 - 1:
        raise ValueError("La longitud L no coincide con los bloques")

    for bloque in bloques:

        if len(bloque) != 6 or not bloque.isascii() or not bloque.isdigit():
            raise ValueError("Cada bloque debe tener 6 digitos")

        numero = int(bloque)

        if numero >= n:
            raise ValueError("Bloque cifrado fuera de rango")

        descifrado = potencia_modular(numero, d, n)
        numeros.append(descifrado)

    mensaje = numeros_a_texto(numeros)

    # Quitar solamente el espacio de relleno
    if L % 2 != 0:
        if mensaje[-1] != " ":
            raise ValueError("El relleno no es valido")

        mensaje = mensaje[:-1]

    return mensaje
