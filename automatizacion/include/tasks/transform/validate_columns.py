def validate_columns(cruce_df, df_hechos):
    """
    Validates if the columns in the processed DataFrame match the expected columns from the reference DataFrame.

    Parameters:
    cruce_df (DataFrame): The processed DataFrame containing the data to validate.
    df_hechos (DataFrame): The reference DataFrame containing the expected columns.

    Returns:
    bool: True if columns match, False otherwise.
    """
    # Obtener columnas actuales
    columnas_actuales = list(cruce_df.columns)

    # Obtener columnas esperadas del archivo de hechos
    campos_esperados = df_hechos['Campo'].dropna().astype(str).tolist()

    # Verificar coincidencia exacta (en orden)
    mismo_orden = columnas_actuales == campos_esperados

    print("¿Columnas con el mismo orden?:", mismo_orden)
    return mismo_orden