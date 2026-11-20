
import ctypes
from pathlib import Path

FONT_DIR = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "fonts"
)

FR_PRIVATE = 0x10

def cargar_fuentes():
    fuentes = [
        "Poppins-Regular.ttf",
        "Poppins-Bold.ttf"
    ]

    for nombre in fuentes:
        ruta = FONT_DIR / nombre

        if not ruta.exists():
            print(f"No se encontró: {ruta}")
            continue

        resultado = ctypes.windll.gdi32.AddFontResourceExW(
            str(ruta),
            FR_PRIVATE,
            0
        )

        if resultado == 0:
            print(f"No se pudo cargar: {nombre}")
        else:
            print(f"Fuente cargada: {nombre}")


TITLE = ("Poppins", 30, "bold")
SUBTITLE = ("Poppins", 20, "bold")
SECTION = ("Poppins", 17, "bold")
BODY = ("Poppins", 14)
SMALL = ("Poppins", 12)
BUTTON = ("Poppins", 14, "bold")
CODE = ("Consolas", 15)
