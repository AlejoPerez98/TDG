# filepath: c:\Users\Aleja\OneDrive\Escritorio\Icesi\TDG\TDG\Airflow\airflow_project\tasks\extract\generate_download_link.py
from datetime import datetime
import calendar
from dateutil.relativedelta import relativedelta

def generar_enlace():
    # Obtener la fecha actual
    today = datetime.today()

    # Restar 2 meses a la fecha actual
    fecha_calculada = today - relativedelta(months=2)

    # Obtener el mes y año
    mes = calendar.month_name[fecha_calculada.month]
    anio = fecha_calculada.year

    # Crear el enlace de descarga
    enlace = f"https://www.dian.gov.co/dian/cifras/Basesestadisticasexportaciones/03_Exportaciones_{anio}_{mes}.zip"
    print(f"Enlace generado: {enlace}")
    return enlace