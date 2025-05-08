import os

def clean_zip_files(download_dir):
    """
    This function iterates through the specified download directory and removes ZIP files after extraction.
    It ensures that the directory is cleaned up by deleting unnecessary files.
    """
    for filename in os.listdir(download_dir):
        if filename.endswith(".zip"):
            file_path = os.path.join(download_dir, filename)
            try:
                os.remove(file_path)
                print(f"Archivo eliminado: {file_path}")
            except Exception as e:
                print(f"Error al eliminar el archivo {file_path}: {e}")

    print("Todos los archivos ZIP han sido eliminados.")