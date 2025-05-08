from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from tasks.extract.generate_download_link import generar_enlace
from tasks.extract.extract_zip_files import extract_zip_files
from tasks.extract.clean_zip_files import clean_zip_files
from tasks.extract.rename_files import rename_files
from tasks.transform.process_excel_data import process_excel_data
from tasks.transform.validate_columns import validate_columns
from tasks.transform.validate_data_types import validate_data_types
from tasks.load.save_processed_data import save_processed_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

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
    generate_link_task >> extract_task >> clean_task >> rename_task >> process_task >> validate_columns_task >> validate_data_types_task >> save_task