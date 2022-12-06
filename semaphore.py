import threading
import time
import random
import myQueue


semaphore = threading.Semaphore(2)
process = myQueue.myQueue()
threadsTime = []


def moves_in_myQueue(number_thread):

    timeStart = time.time()
    
    semaphore.acquire()

    old = process.remove()
    new = random.randint(1,99)
    process.insert(new)

    print('Thread-{0}: tira{1:3d}, poe{2:3d}, fila:{3}'.format(number_thread+1, old, new, process.get()))
    
    semaphore.release()
    
    timeEnd = time.time()
    
    threadsTime.append(timeEnd - timeStart)


def concurrent():

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