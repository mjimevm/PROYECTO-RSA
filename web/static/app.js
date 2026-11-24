
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
