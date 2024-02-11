
# dag_id
dag = DAG(dag_id='dag',    # dag_id  Это уникальное имя, оно будет в отражаться в интерфейсе. Не должно повторяться в рамках различных дагов              
         default_args={'owner': 'airflow'},
         schedule_interval='@daily', # интервал
         start_date=days_ago(1) ) #дата


#default_args
args = {'retries': 1}
dag = DAG(
    dag_id='my_dag',
    default_args=args, # Передача списка параметров
    schedule_interval=timedelta(days=1),
    start_date= datetime(2023, 1, 1)) # а сегоднишняя дата 2023.01.05 выполниться 2023-01-01 ,2023-01-02 ,2023-01-03,2023-01-04

# для чего вообще он нужен этот оператор 
load_data = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
    op_kwargs={
        'tmp_file': '/tmp/file.csv',
        'table_name': 'table'
    }
)

