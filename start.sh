
#!/bin/sh
set -e

# Configurar pantalla virtual
export DISPLAY=:99

Xvfb :99 -screen 0 1280x800x24 -ac &
sleep 2

# Verificar contraseña
if [ -z "${VNC_PASSWORD:-}" ]; then
    echo "ERROR: Falta VNC_PASSWORD"
    exit 1
fi

# Crear archivo de autenticación
mkdir -p /run/vnc
umask 077

x11vnc -storepasswd "$VNC_PASSWORD" /run/vnc/passwd

# Iniciar servidor VNC
x11vnc \
    -display :99 \
    -forever \
    -shared \
    -rfbport 5900 \
    -localhost \
    -rfbauth /run/vnc/passwd \
    -noxdamage \
    -noxrecord \
    -noxfixes \
    -wait 30 \
    -bg

# Iniciar noVNC
websockify \
    --web=/usr/share/novnc/ \
    "${PORT:-6080}" \
    localhost:5900 &

# Ejecutar aplicación RSA
exec python main.py
