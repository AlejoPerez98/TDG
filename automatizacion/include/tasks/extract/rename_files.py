def rename_files(download_dir):
    import os
    import re

    # Listar los archivos en el directorio
    archivos = os.listdir(download_dir)

    # Renombrar los archivos en el directorio
    for archivo in archivos:
        match = re.search(r'_(\d{4})_', archivo)  # Buscar un patrón de año (4 dígitos) en el nombre del archivo
        if match:
            nuevo_nombre = archivo[match.start() + 1:]  # Extraer desde el carácter del año
            ruta_actual = os.path.join(download_dir, archivo)
            nueva_ruta = os.path.join(download_dir, nuevo_nombre)
            try:
                os.rename(ruta_actual, nueva_ruta)
                print(f"Archivo renombrado: {ruta_actual} -> {nueva_ruta}")
            except Exception as e:
                print(f"Error al renombrar el archivo {ruta_actual}: {e}")