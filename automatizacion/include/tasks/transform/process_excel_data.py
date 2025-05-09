def process_excel_data(file_path_cruce):
    import pandas as pd

    # Leer el archivo Excel
    Cruce = pd.read_excel(file_path_cruce)

    tipos_deseados = {
        'FECHA_PROCESO': 'datetime',
        'NUMERO_SERIE': 'int',
        'OFICINA': 'str',
        'COD_ADUANA_DESPACHO': 'int',
        'ADUANA_DESPACHO': 'str',
        'TIPO_IDENT': 'int',
        'NIT_EXPORTADOR': 'int',
        'TIPO_USUARIO': 'int',
        'COD_USUARIO': 'int',
        'CLASE_EXPORTADOR': 'int',
        'COD_DPTO_EXPORTADOR': 'int',
        'COD_PAIS_DESTINO_NUM': 'int',
        'COD_PAIS_DESTINO_ALF': 'str',
        'COD_PAIS_DESTINO': 'str',
        'PAIS_DESTINO_FINAL': 'str',
        'CIUDAD_DESTINATARIO': 'str',
        'NUM_SOLICITUD_AUTO_EMBARQUE': 'int',
        'TIPO_DECLARACION': 'int',
        'TIPO_DESPACHO': 'str',
        'COD_LUGAR_SALIDA_NUM': 'int',
        'COD_LUG_SALIDA_ALF': 'str',
        'COD_REGION_PROCEDENCIA': 'int',
        'REGION_PROCEDENCIA': 'str',
        'NUM__DECLA_EXPORTACION_ANT': 'int',
        'FECH_DECLA_EXPORTACION_ANT': 'datetime',
        'NUM_DECLARACION_PRECEDENTE': 'int',
        'FECH_DECLA_PRECEDENTE': 'datetime',
        'COD_MODALIDAD_PRECEDENTE': 'str',
        'COD_MONEDA_TRANSACCION': 'str',
        'COD_MODO_TRANSPORTE': 'str',
        'MODO_TRANSPORTE': 'str',
        'BANDERA': 'str',
        'COD_NACIONALIDAD_BANDERA': 'str',
        'NACIONALIDAD_BANDERA': 'str',
        'COD_REGIMEN_CAN': 'int',
        'COD_MODALIDAD_EXPORTACION': 'int',
        'MODALIDAD_EXPORTACION': 'str',
        'FORMA_PAGO': 'str',
        'COD_TIPO_EMBARQUE': 'str',
        'TIPO_DE_EMBARQUE': 'str',
        'COD_TIPO_DATOS': 'str',
        'TIPO_DE_DATOS': 'str',
        'TIPO_CERTIFICADO_ORIGEN': 'str',
        'SISTEMAS_ESPECIALES': 'str',
        'COD_EXPORTACION_TRANSITO': 'int',
        'EXPORTACION_EN_TRANSITO': 'str',
        'SUBPARTIDA': 'str',
        'COD_REGION_ORIGEN': 'int',
        'REGION_DE_ORIGEN': 'str',
        'COD_UNIDAD_FISICA_NUM': 'int',
        'COD_UNIDAD_FISICA_ALF': 'str',
        'UNIDAD_FISICA': 'str',
        'CANTIDAD_UNIDADES_FISICAS': 'float',
        'PESO_BRUTO_KGS': 'float',
        'PESO_NETO_KGS': 'float',
        'VALOR_FOB_USD': 'float',
        'VALOR_FOB_PESOS': 'float',
        'VLR_SERIE_AGREGADO_NAL_USD': 'float',
        'VALOR_SERIE_FLETES_USD': 'float',
        'VALOR_SERIE_SEGUROS_USD': 'float',
        'VLR_SERIE_OTROS_GASTOS_USD': 'float',
        'COD_ADUANA_SALIDA': 'str',
        'ADUANA_SALIDA': 'str',
        'FECHA_SOLICITUD_AUTO_EMBARQUE': 'datetime',
        'NUMERO_FORMULARIO': 'int',
        'FECHA_DECLARACION_EXPORTACION': 'datetime',
        'RAZON_SOCIAL_EXPORTADOR': 'str',
        'DIREC_EXPORTADOR': 'str',
        'NIT_DECLARANTE': 'int',
        'RAZON_SOCIAL_DECLARANTE': 'str',
        'RAZON_SOCIAL_DESTINATARIO': 'str',
        'DOMICILIO_DESTINATARIO': 'str',
    }

    for col, tipo in tipos_deseados.items():
        if tipo == 'str':
            Cruce[col] = Cruce[col].astype(str).str.strip()
        elif tipo == 'float':
            Cruce[col] = pd.to_numeric(Cruce[col], errors='coerce').astype('float64')
        elif tipo == 'int':
            Cruce[col] = pd.to_numeric(Cruce[col], errors='coerce').astype('Int64')
        elif tipo == 'datetime':
            Cruce[col] = pd.to_datetime(Cruce[col], errors='coerce')

    Cruce['SUBPARTIDA'] = Cruce['SUBPARTIDA'].apply(lambda x: str(x).zfill(10))
    Cruce['CAPÍTULO'] = Cruce['SUBPARTIDA'].str[:2]
    Cruce['PARTIDA'] = Cruce['SUBPARTIDA'].str[:4]

    Cruce.loc[Cruce['NIT_EXPORTADOR'] == 0, 'NIT_EXPORTADOR'] = 900000000
    Cruce.loc[Cruce['NIT_DECLARANTE'] == 0, 'NIT_DECLARANTE'] = 900000000

    return Cruce