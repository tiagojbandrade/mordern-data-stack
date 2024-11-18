from time import sleep
from airflow.decorators import dag,task
from datetime import datetime

@dag(
        dag_id="pipeline", 
        description="minha pipeline no airflow"
        schedule="0 0 1 * *", 
        start_date=datetime(2024, 11, 1), 
        catchup=False)
def pipeline():

    @task
    def primeira_atividade():
        print("primeira atividade rodou com sucesso")
        sleep(2)

    @task
    def segunda_atividade():
        print("segunda atividade rodou com sucesso")
        sleep(2)
        
    @task    
    def terceira_atividade():
        print("terceira atividade rodou com sucesso")
        sleep(2)        


    t1=primeira_atividade()
    t2=segunda_atividade()
    t3=terceira_atividade()
    
    t1 >> t2 >> t3

pipeline()