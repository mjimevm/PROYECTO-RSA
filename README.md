# PROYECTO-RSA

**Proyecto de Criptografía RSA**  
MM2015 — Matemática Discreta 1

Aplicación de escritorio desarrollada en Python que permite encriptar y desencriptar mensajes de texto utilizando el algoritmo RSA, mediante una interfaz gráfica construida con CustomTkinter.

El proyecto aplica conceptos de aritmética modular, números primos, máximo común divisor, inversos modulares y exponenciación modular.

## 1. Características

La aplicación está diseñada para ofrecer las siguientes funcionalidades:

- Encriptación de mensajes de texto mediante RSA.
- Desencriptación y recuperación exacta del mensaje original.
- Validación de los parámetros matemáticos.
- Conversión de caracteres a códigos ASCII.
- Procesamiento de mensajes en bloques de dos caracteres.
- Visualización de resultados y cálculos intermedios.
- Interfaz gráfica con navegación entre Dashboard, Encriptar y Desencriptar.

## 2. Tecnologías utilizadas

| Tecnología | Descripción |
|---|---|
| Python | Lenguaje de programación principal |
| CustomTkinter | Biblioteca para la interfaz gráfica |
| Pillow | Carga de iconos e imágenes PNG |
| Tkinter | Biblioteca gráfica base |
| Poppins | Tipografía principal |
| Consolas | Visualización de bloques numéricos |

La interfaz utiliza una paleta de colores blanco, negro, azul pastel, lavanda y verde menta, con tarjetas y botones de bordes redondeados.

## 3. Requisitos

Para ejecutar el proyecto desde el código fuente se necesita:

- Python 3.
- Tkinter disponible en la instalación de Python.
- Las dependencias indicadas en `requirements.txt`.
- Los recursos gráficos incluidos en `assets/`.

El proyecto está preparado principalmente para ejecutarse en Windows.

## 4. Instalación

### Clonar el repositorio

```bash
git clone "URL_DEL_REPOSITORIO"
```

Acceder a la carpeta principal de la aplicación:

```bash
cd Proyecto_RSA
```

### Crear un entorno virtual

```bash
python -m venv .venv
```

### Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:

```text
customtkinter
Pillow
```

## 5. Ejecución

Desde la carpeta donde se encuentra `main.py`, ejecutar:

```bash
python main.py
```

## 6. Procedimiento de uso

**Para encriptar:**

1. Seleccionar la opción **Encriptar** en la barra lateral o directamente en la opción de la Vista General.
2. Introducir los números primos `p` y `q`, junto con el exponente `e`.
3. Escribir el mensaje deseado.
4. Presionar **Encriptar mensaje**.
5. Consultar el mensaje cifrado `C` y la longitud original `L` en el panel de resultados.

**Para desencriptar:**

1. Seleccionar la opción **Desencriptar**.
2. Introducir los mismos valores `p`, `q` y `e` utilizados en la encriptación.
3. Ingresar el mensaje cifrado `C` y la longitud original `L`.
4. Presionar **Desencriptar mensaje**.
5. Consultar el mensaje recuperado y los detalles matemáticos del procedimiento.

La longitud `L` permite identificar si se agregó un espacio de relleno durante la encriptación. Si el mensaje original tenía una cantidad impar de caracteres, se retira exactamente el último espacio agregado, conservando todos los espacios originales.

## 7. Fundamento matemático

RSA utiliza dos números primos distintos, `p` y `q`.

Se calcula:

$$
n = pq
$$

$$
\varphi(n) = (p-1)(q-1)
$$

El exponente público `e` debe cumplir:

$$
e > 1,\qquad MCD(e,\varphi(n)) = 1
$$

La llave pública es `(e, n)`.

El exponente privado `d` se obtiene mediante el inverso modular:

$$
ed \equiv 1 \pmod{\varphi(n)}
$$

La llave privada queda determinada por `(d, n)`.

### Encriptación

Para cada bloque numérico `m`:

$$
c = m^e \bmod n
$$

### Desencriptación

Para cada bloque cifrado `c`:

$$
m = c^d \bmod n
$$

Los algoritmos matemáticos se implementan directamente en Python,
sin utilizar funciones que sustituyan el cálculo del MCD,
el inverso modular o la exponenciación modular.

## 8. Representación de los mensajes

La aplicación admite caracteres ASCII imprimibles, cuyos códigos se encuentran entre 32 y 126.

Cada carácter se representa utilizando tres dígitos.

Por ejemplo:

| Carácter | ASCII |
|---|---|
| A | 065 |
| B | 066 |
| R | 082 |
| S | 083 |
| Espacio | 032 |

Los caracteres se agrupan en parejas, formando bloques de seis dígitos.

Si el mensaje tiene longitud impar, se agrega exactamente un espacio al final como relleno.

La longitud original `L` se conserva para poder retirar únicamente ese espacio durante la desencriptación.

Los bloques cifrados se representan con exactamente seis dígitos y se separan mediante espacios.

## 9. Ejemplo completo

El siguiente ejemplo corresponde al caso de referencia del enunciado.

### Datos de entrada

| Parámetro | Valor |
|---|---|
| Mensaje original | `RSA` |
| p | 367 |
| q | 373 |
| e | 17 |


### Cálculos

$$
n = 367 \times 373 = 136891
$$

$$
\varphi(n) = 366 \times 372 = 136152
$$

$$
MCD(17, 136152) = 1
$$

Como la longitud es impar, se agrega un espacio:

```text
RSA 
```

### Conversión a bloques

| Pareja | Bloque ASCII |
|---|---|
| RS | 082083 |
| A + espacio | 065032 |

### Resultado de la encriptación

```text
026054 123875
```

La llave pública es:

```text
(17, 136891)
```

Para desencriptar, se conserva el cifrado `C` junto con `L = 3`.

### Desencriptación

El exponente privado es:

\[
d=8009
\]

Al desencriptar se recuperan los bloques originales, se convierten a caracteres y se retira únicamente el espacio de relleno.

Mensaje recuperado:

```text
RSA
```

El resultado coincide exactamente con el mensaje original.

## 10. Validaciones

El programa debe comprobar las siguientes condiciones:

| Dato | Validación |
|---|---|
| p y q | Enteros, primos y distintos |
| n | `126126 < n < 1000000` |
| e | Entero mayor que 1 y coprimo con φ |
| Mensaje | Caracteres ASCII del 32 al 126 |
| Cifrado | Bloques de exactamente seis dígitos |
| Bloques cifrados | Valores mayores o iguales a 0 y menores que n |
| Longitud L | Para k bloques, debe ser 2k o 2k − 1 |
| Texto recuperado | Caracteres ASCII válidos y relleno coherente |


## 11. Algoritmos implementados

Los algoritmos matemáticos se implementaron directamente en Python, utilizando el algoritmo de Euclides para calcular el máximo común divisor, el algoritmo de Euclides extendido para obtener el inverso modular y la exponenciación binaria modular para realizar las operaciones de cifrado y descifrado.

Estas implementaciones se encuentran en `core/algoritmos.py`, mientras que la comprobación de primalidad se realiza en `core/validaciones.py`.



## 12. Pruebas de funcionamiento

Se comprobaron los siguientes casos:

- Mensajes de longitud par e impar.
- Mayúsculas y minúsculas.
- Números y signos.
- Espacios consecutivos.
- Espacios al inicio y al final.
- Bloques cifrados con ceros iniciales.
- Parámetros RSA inválidos.
- Caracteres no admitidos.
- Bloques cifrados mal formados.
- Longitudes inconsistentes.


## 13. Estructura del proyecto

```text
Proyecto_RSA/
│
├── main.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── fonts/
│   └── icons/
│
├── core/
│   ├── algoritmos.py
│   ├── rsa.py
│   ├── ascii_utils.py
│   └── validaciones.py
│
├── ui/
│   ├── app.py
│   ├── sidebar.py
│   ├── dashboard_view.py
│   ├── encrypt_view.py
│   ├── decrypt_view.py
│   ├── details_view.py
│   ├── fonts.py
│   └── icons.py
│
└── tests/
    └── test_rsa.py
```

## 14. Video demostrativo

**Enlace al video:** https://youtu.be/pa5zy_he3cQ

## 15. Autores

**Nombres:** Alejandro Sagastume y Jimena Vásquez
**Curso:** MM2015 — Matemática Discreta
**Versión de Python utilizada:** 3.11.15  
**Proyecto:** Criptografía RSA
