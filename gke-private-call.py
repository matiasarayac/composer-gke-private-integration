import datetime

from airflow import models
from airflow.operators import python_operator



default_dag_args = {
    "start_date": datetime.datetime(2018, 1, 1),
}

# DAG object.
with models.DAG(
    "composer_gke_integration",
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_dag_args,
) as dag:
    def gke_service_call():
        import requests
        import logging
        api_url = "http://10.0.0.22"
        response = requests.get(api_url, verify=False)        
        logging.info(response.text)

    gke_service_call = python_operator.PythonOperator(
        task_id="gke_service_call", python_callable=gke_service_call
    )
  
    gke_service_call
