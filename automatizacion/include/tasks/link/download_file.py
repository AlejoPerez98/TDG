import os
import requests

def descargar_archivo(url, carpeta_destino):
    # Crear carpeta si no existe
    os.makedirs(carpeta_destino, exist_ok=True)

    nombre_archivo = url.split('/')[-1]
    ruta_completa = os.path.join(carpeta_destino, nombre_archivo)

    response = requests.get(url)
    response.raise_for_status()

    with open(ruta_completa, 'wb') as f:
        f.write(response.content)

    print(f"Archivo guardado en: {ruta_completa}")
