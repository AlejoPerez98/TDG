def save_processed_data(processed_data, output_file_path):
    """
    Save the processed DataFrame to a new Excel file.

    Parameters:
    processed_data (DataFrame): The DataFrame to save.
    output_file_path (str): The path where the Excel file will be saved.
    """
    processed_data.to_excel(output_file_path, index=False)
    print(f"Archivo actualizado guardado como: {output_file_path}")