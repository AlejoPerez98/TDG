import boto3
import os
import requests

def descargar_archivo(url, bucket_name, s3_key_prefix):
    # Crear cliente de S3 con credenciales explícitas
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )

    # Descargar el archivo desde la URL
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # Obtener el nombre del archivo desde la URL
    nombre_archivo = url.split('/')[-1]
    s3_key = f"{s3_key_prefix}/{nombre_archivo}"

    # Subir el archivo directamente a S3
    s3.upload_fileobj(response.raw, bucket_name, s3_key)
    print(f"Archivo subido directamente a S3: s3://{bucket_name}/{s3_key}")
    
    return nombre_archivo