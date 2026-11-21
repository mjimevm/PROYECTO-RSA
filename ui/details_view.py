
# Mostrar los detalles del proceso RSA

from core.ascii_utils import texto_a_numeros
from core.algoritmos import potencia_modular


def detalles_encriptacion(mensaje, p, q, e):

    n = p * q
    L = len(mensaje)

    # Agregar relleno cuando sea necesario
    if L % 2 != 0:
        mensaje += " "

    # Convertir el mensaje a bloques ASCII
    bloques = texto_a_numeros(mensaje)

    detalles = "PROCESO DE ENCRIPTACION\n\n"

    detalles += "Longitud original: " + str(L) + "\n"
    detalles += "Modulo n: " + str(n) + "\n\n"

    for i in range(len(bloques)):
        bloque = bloques[i]

        cifrado = potencia_modular(bloque, e, n)

        detalles += "Bloque " + str(i + 1) + "\n"
        detalles += "ASCII: " + str(bloque).zfill(6) + "\n"
        detalles += "Cifrado: " + str(cifrado).zfill(6) + "\n\n"

    return detalles


# Mostrar los detalles de la desencriptacion
def detalles_desencriptacion(cifrado, L, p, q, e):

    from core.rsa import generar_claves, desencriptar

    n, d = generar_claves(p, q, e)
    total_coprimos = (p - 1) * (q - 1)

    # Validar primero el cifrado y la longitud
    mensaje = desencriptar(cifrado, L, p, q, e)

    bloques = cifrado.split()

    detalles = "PROCESO DE DESENCRIPTACION\n\n"
    detalles += f"Modulo n: {n}\n"
    detalles += f"Phi: {total_coprimos}\n"
    detalles += f"Exponente privado d: {d}\n"
    detalles += f"Longitud original L: {L}\n"

    if L % 2 == 0:
        detalles += "Relleno: No\n\n"
    else:
        detalles += "Relleno: Si\n\n"

    for i in range(len(bloques)):
        numero = int(bloques[i])

        recuperado = potencia_modular(numero, d, n)
        ascii_bloque = str(recuperado).zfill(6)

        codigo1 = int(ascii_bloque[:3])
        codigo2 = int(ascii_bloque[3:])

        caracteres = chr(codigo1) + chr(codigo2)

        detalles += f"Bloque {i + 1}\n"
        detalles += f"Cifrado: {bloques[i]}\n"
        detalles += f"ASCII recuperado: {ascii_bloque}\n"
        detalles += f"Caracteres: {repr(caracteres)}\n\n"

    detalles += f"Mensaje recuperado: {repr(mensaje)}"

    return detalles
