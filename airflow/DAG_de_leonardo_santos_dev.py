from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from custom_operators.tworp_spark_submit_operator import TwoRPSparkSubmitOperator
from datetime import datetime, timedelta

usuario = '2rp-leonardos'
default_args = {
    'owner': usuario,
    'start_date': datetime(2021,1,1),
    'depend_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'run_as_user': usuario,
    'proxy_user': usuario,
}

with DAG(dag_id='de_leonardo_santos_dev',
        schedule_interval=None,
        default_args=default_args,
        catchup=False) as dag:
    dummy_task = DummyOperator(
        task_id='dummy',
    )
    kinit_task = BashOperator(
        task_id='kinit',
        bash_command=f'kinit -kt /home/{usuario}/{usuario}.keytab {usuario}',
    )
    shell_task = BashOperator(
        task_id='shell',
        bash_command=f'bash /home/{usuario}/shell-scripts/executar.sh ' \
            f'"/home/{usuario}/shell-scripts/test" "some text"'
    )
    spark_task = TwoRPSparkSubmitOperator(
        task_id='spark',
        name='pokemon',
        conn_id='spark_conn',
        application=f'/home/{usuario}/pokemons_oldschool.py',
        keytab=f'/home/{usuario}/{usuario}.keytab',
        principal=usuario,
        proxy_user=None,
        verbose=True
    )

    dummy_task >> kinit_task >> shell_task >> spark_task

