import threading
import time
import random
from myQueue import MyQueue


semaphore = threading.Semaphore(2) # Quantidade de semáforos usados
process = MyQueue() # Inicia a fila
threadsTime = []


def moves_in_myQueue(number_thread):
    # Função de movimento da fila

    timeStart = time.time()
    
    semaphore.acquire()

    old = process.remove()
    new = random.randint(1,99)
    process.insert(new)

    print('Thread-{0}: tira{1:3d}, poe{2:3d}, fila:{3}'.format(number_thread+1, old, new, process.get()))
    
    semaphore.release()
    
    timeEnd = time.time() 
    
    threadsTime.append(timeEnd - timeStart) # Adiciona o tempo de execução de cada thread


def concurrent():
    # Função principal de execução com threads 
    
    print("\nFila Inicial: ", process.get(),"\n")
    number_thread = 0
    series = []

    while(sum(threadsTime) < 1):
        series.append(threading.Thread(target=moves_in_myQueue, args=(number_thread,)))
        series[number_thread].start() 
        series[number_thread].join() 
        number_thread += 1

    duration = sum(threadsTime) 
    moves_per_seconds = number_thread/duration
    
    return [duration, moves_per_seconds]