import zipfile
import os

def extract_zip_files(download_dir):
    """
    Extract Excel files from ZIP archives located in the specified download directory.
    
    Args:
        download_dir (str): The directory where ZIP files are located.
        
    Returns:
        list: A list of extracted Excel file names.
    """
    extracted_files = []
    
    for filename in os.listdir(download_dir):
        if filename.endswith(".zip"):
            zip_path = os.path.join(download_dir, filename)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                for file in zip_ref.namelist():
                    if file.endswith(".xlsx"):
                        zip_ref.extract(file, download_dir)
                        extracted_files.append(file)
                        print(f"Archivo {file} extraído a {download_dir}")
    
    return extracted_files