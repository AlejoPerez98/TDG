from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from include.tasks.link.generate_download_link import generar_enlace
from include.tasks.link.download_file import descargar_archivo
from include.tasks.extract.extract_zip_files import extract_zip_files
from include.tasks.extract.clean_zip_files import clean_zip_files
from include.tasks.extract.rename_files import rename_files
from include.tasks.transform.process_excel_data import process_excel_data
from include.tasks.transform.validate_columns import validate_columns
from include.tasks.transform.validate_data_types import validate_data_types
from include.tasks.load.save_processed_data import save_processed_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

def obtener_enlace(**context):
    # No necesitas usar xcom_push si la función ya devuelve un valor
    enlace = generar_enlace()
    print(f"Enlace generado: {enlace}")  # Para depuración
    return enlace  # Esto se almacenará automáticamente en XCom bajo la clave 'return_value'

def descargar(**context):
    # Recuperar el valor desde XCom usando la clave predeterminada 'return_value'
    url = context['ti'].xcom_pull(task_ids='generate_download_link')
    print(f"URL recuperada desde XCom: {url}")  # Para depuración
    if not url:
        raise ValueError("No se pudo obtener el enlace para descargar el archivo.")
    carpeta_destino = "/tmp/ZIP"
    descargar_archivo(url, carpeta_destino)
    
with DAG(
    'procesamiento_dag',
    default_args=default_args,
    description='DAG para el procesamiento de datos',
    schedule_interval='0 0 10 * *',  # Ejecutar el 10 de cada mes
    catchup=False,
) as dag:

    generate_link_task = PythonOperator(
        task_id='generate_download_link',
        python_callable=generar_enlace,
        dag=dag,
    )
    
    download_task = PythonOperator(  # Nueva tarea para descargar el archivo
        task_id='download_file',
        python_callable=descargar,
        dag=dag,
    )

    extract_task = PythonOperator(
        task_id='extract_zip_files',
        python_callable=extract_zip_files,
        dag=dag,
    )

    clean_task = PythonOperator(
        task_id='clean_zip_files',
        python_callable=clean_zip_files,
        dag=dag,
    )

    rename_task = PythonOperator(
        task_id='rename_files',
        python_callable=rename_files,
        dag=dag,
    )

    process_task = PythonOperator(
        task_id='process_excel_data',
        python_callable=process_excel_data,
        dag=dag,
    )

    validate_columns_task = PythonOperator(
        task_id='validate_columns',
        python_callable=validate_columns,
        dag=dag,
    )

    validate_data_types_task = PythonOperator(
        task_id='validate_data_types',
        python_callable=validate_data_types,
        dag=dag,
    )

    save_task = PythonOperator(
        task_id='save_processed_data',
        python_callable=save_processed_data,
        dag=dag,
    )

    # Definir el flujo de tareas
    generate_link_task >> download_task >> extract_task >> clean_task >> rename_task >> process_task >> validate_columns_task >> validate_data_types_task >> save_task