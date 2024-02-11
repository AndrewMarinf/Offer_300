# Первым делом мы импортируем необходимый class
from airflow import DAG

#После чего создаем объект DAG 
#Какие аргументы принимает DAG мы разберем в следующем шаге.

dag =  DAG('dag', schedule_interval=timedelta(days=1), start_date=days_ago(1))


# 1 varik
from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
 
# Создадим объект класса DAG
dag =  DAG('dag', schedule_interval=timedelta(days=1), start_date=days_ago(1))

# 2 varik
from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
 
# Создадим объект класса DAG
with DAG('dag', schedule_interval=timedelta(days=1), start_date=days_ago(1)) as dag:
  pass

#-----------------------------------------------------------------
from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
 
# Создадим объект класса DAG
dag =  DAG('dag', schedule_interval=timedelta(days=1), start_date=days_ago(1))

# Создадим dummy(пустые)команду
t1 = DummyOperator(task_id='task_1', dag=dag)


# Создадим несколько шагов, которые будут параллельно исполнять dummy(пустые)команды
t2 = BashOperator(task_id='task_1',
                  bash_command='cat /root/airflow/dags/dag.py',
                  dag=dag)

def print_context():
    return 'Hello World'

run_this = PythonOperator(
    task_id='print_the_context',
    python_callable=print_context,
    dag=dag,
)