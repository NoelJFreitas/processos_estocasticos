import random
import sys
import time


def generate_arrival_times():
    # qtd_customers: int = int(input('Informe a quantidade de cliente: '))
    qtd_customers: int = 6
    customers = []
    for i in range(qtd_customers):
        entry_time = random.randint(0, 8)
        service_time = random.randint(1, 6)
        customers.append({"cliente": i + 1, "service_time": service_time, "entry_time": entry_time})

    return customers


def customer_service():
    current_customers = {}
    current_time = 0
    service_time = 0
    served = 0
    queue = []
    entry_order = generate_arrival_times()
    queue_time = 0

    while served < len(entry_order):

        if current_customers:
            if current_customers['service_time'] == service_time:
                current_customers = {}
                service_time = 0
                served += 1
                if queue:
                    current_customers = queue[0]
                    queue.pop(0)
            else:
                service_time += 1
        else:
            if queue:
                current_customers = queue[0]
                queue.pop(0)

        for customer in entry_order:
            if customer['entry_time'] == current_time:
                if not current_customers:
                    current_customers = customer
                else:
                    queue.append(customer)
        if queue:
            queue_time += 1

        print("\n" * 130)
        if current_customers:
            print(
                f"Num. {current_customers['cliente']} em atendimento. qtd na fila: {len(queue)}")
        else:
            print(f"ninguem em atendimento. qtd na fila: {len(queue)}")

        current_time += 1
        time.sleep(1)
    calculate_metrics(entry_order, current_time, queue_time)


def calculate_metrics(entry_order, total_time, queue_time):
    tempo_atendimento = 0
    for customer in entry_order:
        tempo_atendimento += customer['service_time']

    tx = (len(entry_order) * 60) / total_time
    ta = tempo_atendimento / len(entry_order)
    tf = queue_time / len(entry_order)

    print(f"Taxa de chegada: {tx} por hora")
    print(f"Taxa de atendimento: {ta} por minuto")
    print(f"Tempo medio de fila: {tf} minutos")


customer_service()
print('Fim do atendimento')
