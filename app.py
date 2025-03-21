from flask import Flask, jsonify, render_template_string, request, redirect, url_for
import requests
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict

app = Flask(__name__)

# Variable global para almacenar los resultados del escaneo
scan_results = []
ip_mac_mapping = {}

# Diccionario para asignar nombres a las MAC conocidas
mac_to_name = {
    "FCEE1103C1A5": "E3KE-2",
    "FCEE1103BFE1": "E3KE-1"
}

def perform_scan():
    global scan_results, ip_mac_mapping
    start_ip = 1
    end_ip = 300
    base_ip = "192.168.137."
    scan_attempts = 3

    def check_ip(ip):
        url = f"http://{base_ip}{ip}"
        info_url = f"{url}/info"
        try:
            response = requests.get(info_url, timeout=0.1)
            if response.status_code == 200:
                data = response.json()
                mac = data.get("mac", "Unknown MAC")
                model = data.get("model", "Unknown Model")
                
                # Asegurarse de que la MAC esté en un formato consistente (mayúsculas y sin espacios)
                mac = mac.upper().replace(" ", "")
                
                # Asignar nombre según la MAC
                device_name = mac_to_name.get(mac, f"Unknown Device ({model})")
                # Guardar la relación IP <-> MAC
                ip_mac_mapping[mac] = url
                return {'url': url, 'device_name': device_name, 'mac': mac}
                
        except requests.RequestException:
            return None

    all_results = []
    for _ in range(scan_attempts):
        with ThreadPoolExecutor(max_workers=50) as executor:
            results = executor.map(check_ip, range(start_ip, end_ip + 1))
            all_results.extend(results)

    # Usar un conjunto para filtrar duplicados basados en la MAC
    unique_results = {result['mac']: result for result in all_results if result}.values()

    # Filtrar y organizar resultados
    scan_results = [
        {
            'url': result['url'],
            'device_name': result['device_name'],
            'mac': result['mac']
        }
        for result in unique_results
    ]

    print("Scan Results:", scan_results)  # Agregar esta línea para depurar

@app.route('/')
def home():
    perform_scan()  # Realizar un escaneo al cargar la página principal
    html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Printer Network</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container py-5">
        <h1 class="text-center mb-4">3D Printer Network</h1>
        <div class="card shadow-sm">
            <div class="card-body">
                <h2 class="h4">Available Devices</h2>
                <ul class="list-group">
                    {% for result in results %}
                        <li class="list-group-item">
                            <a href="{{ result.url }}" target="_blank" class="text-decoration-none">
                                <span class="fw-bold">{{ result.device_name }}</span>
                                <small class="text-muted">({{ result.url }})</small>
                            </a>
                        </li>
                    {% endfor %}
                </ul>
                <form action="/scan" method="post" class="mt-3">
                    <button type="submit" class="btn btn-primary w-100">Update IPs</button>
                </form>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    '''
    return render_template_string(html_template, results=scan_results)

@app.route('/scan', methods=['POST'])
def scan_network():
    perform_scan()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=5000)
