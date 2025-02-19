# Importa módulos Schedule e Time
import schedule
import time

# Função(tarefa) a ser executada
def minha_tarefa():
    print("Executando minha tarefa...")

# Agenda a tarefa para executar a cada minuto
schedule.every(1).minutes.do(minha_tarefa)

while True:
    # Executa as tarefas agendadas
    schedule.run_pending()  

    # Evita sobrecarga da CPU
    time.sleep(1)  


