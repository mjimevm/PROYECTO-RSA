
# Conversion de texto a bloques ASCII


# Convertir texto a bloques de dos caracteres
def texto_a_numeros(mensaje):
    bloques = []

    for i in range(0, len(mensaje), 2):
        letra1 = mensaje[i]
        letra2 = mensaje[i + 1]

        numero1 = str(ord(letra1)).zfill(3)
        numero2 = str(ord(letra2)).zfill(3)

        bloque = numero1 + numero2
        bloques.append(int(bloque))

    return bloques


# Convertir bloques numericos a texto
def numeros_a_texto(bloques):
    mensaje = ""

    for bloque in bloques:
        numero = str(bloque).zfill(6)

        codigo1 = int(numero[:3])
        codigo2 = int(numero[3:])

        if codigo1 < 32 or codigo1 > 126:
            raise ValueError("Codigo ASCII no valido")

        if codigo2 < 32 or codigo2 > 126:
            raise ValueError("Codigo ASCII no valido")

        mensaje += chr(codigo1)
        mensaje += chr(codigo2)

    return mensaje
