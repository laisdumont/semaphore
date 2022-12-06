import threading
import time
import random
import myQueue


process = MyQueue.myQueue()
threadsTime = []


def moves_in_myQueue(number_thread):

    timeStart = time.time()

    old = process.remove()
    new = random.randint(3,10)
    process.insert(new)

    print('Execução {0}: tira{1:3d}, poe{2:3d}, fila:{3}'.format(number_thread, old, new, process.get()))

    timeEnd = time.time()

    threadsTime.append(timeEnd - timeStart)

def sequential():

    print("\nFila Inicial: ", process.get(),"\n")
    number_thread = 0

    while(sum(threadsTime) < 1):
        moves_in_myQueue(number_thread)
        number_thread += 1

    duration = sum(threadsTime)
    moves_per_seconds = number_thread/duration
    
    return [duration, moves_per_seconds]