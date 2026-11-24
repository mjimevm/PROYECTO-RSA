from flask import Flask, render_template, request, send_from_directory
from pathlib import Path
from core.rsa import encriptar, generar_claves
from ui.details_view import detalles_encriptacion
from core.rsa import desencriptar
from ui.details_view import detalles_desencriptacion
app = Flask(__name__)

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"


@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory(ASSETS_DIR, filename)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")




@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    datos = {
        "p": "",
        "q": "",
        "e": "",
        "mensaje": "",
        "resultado": None,
        "error": None,
        "detalles": None
    }

    if request.method == "POST":
        datos["p"] = request.form.get("p", "")
        datos["q"] = request.form.get("q", "")
        datos["e"] = request.form.get("e", "")
        datos["mensaje"] = request.form.get("mensaje", "")

        try:
            p = int(datos["p"] or "367")
            q = int(datos["q"] or "373")
            e = int(datos["e"] or "17")
            mensaje = datos["mensaje"]

            # Funciones originales del proyecto
            cifrado, L = encriptar(mensaje, p, q, e)
            
            n, d = generar_claves(p, q, e)

            detalles = detalles_encriptacion(
                mensaje, p, q, e
            )

            datos.update({
                "resultado": cifrado,
                "L": L,
                "n": n,
                "phi": (p - 1) * (q - 1),
                "relleno": L % 2 != 0,
                "llave_publica": (e, n),
                "detalles": detalles
            })

        except ValueError as error:
            datos["error"] = str(error)

    return render_template("encrypt.html", **datos)





@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():

    datos = {
        "p": "",
        "q": "",
        "e": "",
        "L": "",
        "cifrado": "",
        "resultado": None,
        "detalles": None,
        "error": None
    }

    if request.method == "POST":

        datos["p"] = request.form.get("p", "")
        datos["q"] = request.form.get("q", "")
        datos["e"] = request.form.get("e", "")
        datos["L"] = request.form.get("L", "")
        datos["cifrado"] = request.form.get("cifrado", "")

        try:
            p = int(datos["p"] or "367")
            q = int(datos["q"] or "373")
            e = int(datos["e"] or "17")

            if not datos["L"].strip():
                raise ValueError(
                    "Debes ingresar la longitud original L"
                )

            L = int(datos["L"])
            cifrado = datos["cifrado"]

            # Reutilizar RSA original
            mensaje = desencriptar(
                cifrado, L, p, q, e
            )

            # Calcular claves
            n, d = generar_claves(p, q, e)
            phi = (p - 1) * (q - 1)

            # Procedimiento original
            detalles = detalles_desencriptacion(
                cifrado, L, p, q, e
            )

            datos.update({
                "resultado": mensaje,
                "n": n,
                "phi": phi,
                "d": d,
                "L": L,
                "detalles": detalles
            })

        except ValueError as error:
            datos["error"] = str(error)

    return render_template(
        "decrypt.html",
        **datos
    )



if __name__ == "__main__":
    app.run(debug=True, port=5000)
