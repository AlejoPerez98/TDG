def validate_data_types(cruce_df, tipos_esperados):
    diferencias_tipos = []

    # Función para mapear dtype real a tipo base
    def mapear_tipo(dtype):
        if pd.api.types.is_integer_dtype(dtype):
            return 'int'
        elif pd.api.types.is_float_dtype(dtype):
            return 'float'
        elif pd.api.types.is_bool_dtype(dtype):
            return 'bool'
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return 'datetime'
        else:
            return 'str'

    # Comparar tipos
    for col in cruce_df.columns:
        tipo_real = mapear_tipo(cruce_df[col].dtype)
        tipo_esperado = tipos_esperados.get(col)

        if tipo_esperado and tipo_real != tipo_esperado:
            diferencias_tipos.append((col, tipo_real, tipo_esperado))

    # Mostrar resultados
    if diferencias_tipos:
        print("❌ Columnas con diferencias de tipo de datos:")
        for col, real, esperado in diferencias_tipos:
            print(f"- {col}: tipo real = {real}, tipo esperado = {esperado}")
    else:
        print("✅ Todos los tipos de datos coinciden.")