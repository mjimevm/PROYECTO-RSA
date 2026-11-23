
#!/bin/sh
set -e

# Iniciar pantalla virtual
Xvfb :99 -screen 0 1280x800x24 -ac &
export DISPLAY=:99

# Esperar a que la pantalla esté disponible
sleep 2

# Iniciar servidor VNC
x11vnc -display :99 -forever -shared \
  -rfbport 5900 -localhost -nopw \
  -noxdamage -bg

# Iniciar noVNC en el puerto 6080
websockify --web=/usr/share/novnc/ \
  "${PORT:-6080}" localhost:5900 &

# Ejecutar la aplicación RSA
exec python main.py
