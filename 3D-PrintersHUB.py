import subprocess
import webbrowser
import time
import os
import socket
import psutil

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def kill_process_on_port(port):
    for proc in psutil.process_iter(['pid', 'name']):
        for conn in proc.net_connections(kind='inet'):
            if conn.laddr.port == port:
                proc.kill()
                print("servidor cerrado")
                return

# Verificar si el puerto 5000 está en uso
if is_port_in_use(5000):
    kill_process_on_port(5000)

script_path = os.path.join(os.path.dirname(__file__), 'app.py')
subprocess.Popen(["python", script_path], creationflags=subprocess.CREATE_NO_WINDOW)
# Esperar unos segundos para asegurarse de que el servidor esté en funcionamiento
time.sleep(3)

# Abrir una pestaña en el navegador predeterminado
webbrowser.open('http://localhost:5000')
