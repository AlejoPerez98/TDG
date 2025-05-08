# Airflow Project Documentation

## Overview
This project is designed to automate the processing of Excel files extracted from ZIP archives using Apache Airflow. The workflow consists of three main stages: Extract, Transform, and Load (ETL). Each stage is implemented as a separate task within the Airflow Directed Acyclic Graph (DAG).

## Project Structure
```
airflow_project
├── dags
│   ├── procesamiento_dag.py          # Defines the DAG for orchestrating tasks
├── tasks
│   ├── extract
│   │   ├── extract_zip_files.py      # Extracts Excel files from ZIP archives
│   │   ├── clean_zip_files.py        # Cleans up ZIP files after extraction
│   │   └── rename_files.py           # Renames extracted Excel files
│   ├── transform
│   │   ├── process_excel_data.py     # Processes and transforms Excel data
│   │   ├── validate_columns.py        # Validates the columns of the DataFrame
│   │   └── validate_data_types.py     # Validates the data types of the DataFrame
│   └── load
│       └── save_processed_data.py     # Saves the processed DataFrame to Excel
├── plugins
│   └── __init__.py                   # Initializes the plugins directory
├── requirements.txt                   # Lists project dependencies
└── README.md                          # Project documentation
```

## Setup Instructions
1. **Install Apache Airflow**: Follow the official [Airflow installation guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html) to set up Airflow in your environment.

2. **Install Dependencies**: Navigate to the project directory and install the required Python packages using:
   ```
   pip install -r requirements.txt
   ```

3. **Configure Airflow**: Set up your Airflow environment by initializing the database and starting the web server and scheduler:
   ```
   airflow db init
   airflow webserver --port 8080
   airflow scheduler
   ```

4. **Access the Airflow UI**: Open your web browser and go to `http://localhost:8080` to access the Airflow UI.

5. **Trigger the DAG**: In the Airflow UI, you can find the `procesamiento_dag` DAG. You can manually trigger it or set a schedule for automatic execution.

## Task Descriptions
- **Extract Tasks**:
  - `extract_zip_files.py`: Extracts Excel files from ZIP archives located in a specified directory.
  - `clean_zip_files.py`: Deletes ZIP files after extraction to keep the directory clean.
  - `rename_files.py`: Renames extracted Excel files based on a defined pattern.

- **Transform Tasks**:
  - `process_excel_data.py`: Reads the extracted Excel file into a DataFrame and applies necessary transformations.
  - `validate_columns.py`: Checks if the DataFrame columns match the expected columns.
  - `validate_data_types.py`: Validates the data types of the DataFrame columns against expected types.

- **Load Task**:
  - `save_processed_data.py`: Saves the processed DataFrame to a new Excel file.

## Conclusion
This Airflow project provides a structured approach to automate the ETL process for Excel files. By following the setup instructions and understanding the task descriptions, you can efficiently manage and execute the data processing workflow.