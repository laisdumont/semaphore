import time
import random
from myQueue import MyQueue


process = MyQueue()
threadsTime = []


def moves_in_myQueue(number_thread):
    # Função de movimento da fila
    
    timeStart = time.time()

    old = process.remove()
    new = random.randint(3,10)
    process.insert(new)

    print('Execução {0}: tira{1:3d}, poe{2:3d}, fila:{3}'.format(number_thread, old, new, process.get()))

    timeEnd = time.time()
 
    threadsTime.append(timeEnd - timeStart) # Adiciona o tempo de execução da função para cada elemento

def sequential():
    # Função principal de execução sem threads

    print("\nFila Inicial: ", process.get(),"\n")
    number_thread = 0

    while(sum(threadsTime) < 1):
        moves_in_myQueue(number_thread)
        number_thread += 1

    duration = sum(threadsTime)
    moves_per_seconds = number_thread/duration
    
    return [duration, moves_per_seconds]