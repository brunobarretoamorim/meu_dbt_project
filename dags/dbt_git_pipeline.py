
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='dbt_git_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['dbt', 'git', 'ci-cd']
) as dag:

    git_clone = BashOperator(
        task_id='clone_dbt_repo',
        bash_command='cd /tmp && rm -rf dbt_project && git clone https://github.com/brunobarretoamorim/meu_dbt_project.git dbt_project',
    )

    dbt_seed = BashOperator(
        task_id='dbt_seed',
        bash_command='cd /tmp/dbt_project && dbt seed --profiles-dir ~/.dbt',
    )

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /tmp/dbt_project && dbt run --profiles-dir ~/.dbt',
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /tmp/dbt_project && dbt test --profiles-dir ~/.dbt',
    )

    git_clone >> dbt_seed >> dbt_run >> dbt_test
