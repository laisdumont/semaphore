import time
import random
from myQueue import MyQueue


process = MyQueue()
executionTime = []
MOVES_PER_SECONDE = 0


def moves_in_myQueue():
    # Função de movimento da fila
    global MOVES_PER_SECONDE
    number_execution = 0

    while(sum(executionTime) < 1):
        timeStart = time.time()

        old = process.remove()
        new = random.randint(3,10)
        process.insert(new)

        print('Execução {0}: tira{1:3d}, poe{2:3d}, fila:{3}'.format(number_execution+1, old, new, process.get()))

        number_execution += 1

        timeEnd = time.time()

        executionTime.append(timeEnd - timeStart) # Adiciona o tempo de execução da função para cada elemento
        
    MOVES_PER_SECONDE += number_execution

def sequential():
    # Função principal de execução sem threads

    print("\nFila Inicial: ", process.get(),"\n")

    moves_in_myQueue()

    duration = sum(executionTime)
    moves_per_seconds = MOVES_PER_SECONDE/duration
    
    return [duration, moves_per_seconds]

if __name__=="__main__":
    data_sequential = sequential()

    print("\n-------------- SEQUENCIAL ----------------")
    print("Duração: {0}s".format(data_sequential[0]))
    print("Movimentos por segundo: {0}".format(data_sequential[1]))
    print("------------------------------------------\n")