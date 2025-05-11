import boto3
import zipfile
import io
import os

def extract_zip_to_s3(bucket_name, s3_key, s3_output_prefix):
    # Crear cliente de S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )

    # Descargar el archivo ZIP desde S3 en memoria
    response = s3.get_object(Bucket=bucket_name, Key=s3_key)
    zip_content = response['Body'].read()

    # Descomprimir el archivo ZIP en memoria y subir cada archivo a S3
    with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_ref:
        for file_name in zip_ref.namelist():
            # Leer el contenido del archivo
            file_content = zip_ref.read(file_name)

            # Subir el archivo descomprimido a S3
            output_key = f"{s3_output_prefix}/{file_name}"
            s3.put_object(Bucket=bucket_name, Key=output_key, Body=file_content)
            print(f"Archivo descomprimido y subido a S3: s3://{bucket_name}/{output_key}")