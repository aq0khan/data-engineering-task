import read_csv

from airflow import DAG

from airflow.operators.python import PythonOperator
from datetime import datetime

def read_csv_class():
    read_csv.read_csv_from_s3('contiamo-challenge', 'data-engineer-challenge/')
    return ("Successfull")
with DAG("read_csv_file", start_date = datetime(2023,1,1) ,schedule_interval = "@once") as dag:
    model = PythonOperator(
        task_id = "read_csv",
        python_callable = read_csv_class,

    )

