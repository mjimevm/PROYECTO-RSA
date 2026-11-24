
function copiarCifrado(boton) {
    const cifrado = boton.dataset.cipher;

    navigator.clipboard.writeText(cifrado)
        .then(() => {
            boton.textContent = "¡Copiado!";

            setTimeout(() => {
                boton.textContent = "Copiar";
            }, 2000);
        })
        .catch(() => {
            boton.textContent = "Error al copiar";
        });
}


/* =========================================
   GUARDAR ESTADO DE ENCRIPTAR Y DESENCRIPTAR
========================================= */

document.addEventListener("DOMContentLoaded", () => {
    const ruta = window.location.pathname;

    if (ruta !== "/encrypt" && ruta !== "/decrypt") {
        return;
    }

    const clave = `rsa_estado_${ruta}`;
    const formulario = document.querySelector("form");

    if (!formulario) return;

    const campos = formulario.querySelectorAll(
        "input[name], textarea[name]"
    );

    // Restaurar los campos guardados
    try {
        const guardado = sessionStorage.getItem(clave);

        if (guardado) {
            const datos = JSON.parse(guardado);

            campos.forEach(campo => {
                if (Object.hasOwn(datos, campo.name)) {
                    campo.value = datos[campo.name];
                }
            });
        }
    } catch (error) {
        console.warn("No se pudo restaurar el formulario", error);
    }

    // Guardar los campos cuando cambien
    function guardarCampos() {
        const datos = {};

        campos.forEach(campo => {
            datos[campo.name] = campo.value;
        });

        try {
            sessionStorage.setItem(
                clave,
                JSON.stringify(datos)
            );
        } catch (error) {
            console.warn("No se pudo guardar el formulario", error);
        }
    }

    formulario.addEventListener("input", guardarCampos);
    formulario.addEventListener("submit", guardarCampos);
});


/* GUARDAR RESULTADOS RSA */

document.addEventListener("DOMContentLoaded", () => {
    const ruta = window.location.pathname;

    if (ruta !== "/encrypt" && ruta !== "/decrypt") {
        return;
    }

    const clave = `rsa_resultado_${ruta}`;
    const resultado = document.querySelector(".result-card");
    const procedimiento = document.querySelector(
        ".cipher-procedure-card"
    );

    const respuestaServidor = document.querySelector(
        ".rsa-server-response"
    );

    // Si Flask devolvió un resultado nuevo, guardarlo
    if (respuestaServidor?.dataset.success === "true") {
        const datos = {
            resultado: resultado?.innerHTML || "",
            procedimiento: procedimiento?.outerHTML || ""
        };

        try {
            sessionStorage.setItem(clave, JSON.stringify(datos));
        } catch (error) {
            console.warn("No se pudo guardar el resultado", error);
        }

        return;
    }

    // Si no hubo una operación nueva, restaurar la anterior
    if (!respuestaServidor) {
        try {
            const guardado = sessionStorage.getItem(clave);
            if (!guardado) return;

            const datos = JSON.parse(guardado);

            if (resultado && datos.resultado) {
                resultado.innerHTML = datos.resultado;
            }

            if (datos.procedimiento && !procedimiento) {
                resultado.insertAdjacentHTML(
                    "afterend",
                    datos.procedimiento
                );
            }
        } catch (error) {
            console.warn("No se pudo restaurar el resultado", error);
        }
    }
});
