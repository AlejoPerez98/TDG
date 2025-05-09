# filepath: c:\Users\Aleja\OneDrive\Escritorio\Icesi\TDG\TDG\Airflow\airflow_project\tasks\extract\generate_download_link.py
from datetime import datetime
import calendar
from dateutil.relativedelta import relativedelta

# Lista de meses en español
meses_espanol = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]


def generar_enlace():
    # Obtener la fecha actual
    today = datetime.today()

    # Restar 2 meses a la fecha actual
    fecha_calculada = today - relativedelta(months=2)

    # Obtener el mes y año
    numero_mes = f"{fecha_calculada.month:02d}"  # Mes en formato 2 dígitos
    mes = meses_espanol[fecha_calculada.month - 1]  # Mes en español
    anio = fecha_calculada.year

    # Crear el enlace de descarga
    enlace = f"https://www.dian.gov.co/dian/cifras/Basesestadisticasexportaciones/{numero_mes}_Exportaciones_{anio}_{mes}.zip"
    print(f"Enlace generado: {enlace}")
    return enlace