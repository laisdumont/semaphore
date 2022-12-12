import threading
import time
import random
from myQueue import MyQueue


semaphore = threading.Semaphore(2) # Quantidade de semáforos usados
PROCESS = MyQueue() # Inicia a fila
threadsTime = []
number_thread = 0
THREAD_PER_SECONDE = 0


def moves_in_myQueue(number_thread):
    # Função de movimento da fila
    global THREAD_PER_SECONDE
    global PROCESS

    while(sum(threadsTime) < 1):
        timeStart = time.time()
        
        semaphore.acquire()

        old = PROCESS.remove()
        new = random.randint(1,99)
        PROCESS.insert(new)

        print('Thread-{0}: tira{1:3d}, poe{2:3d}, fila:{3}'.format(number_thread+1, old, new, PROCESS.get()))
        
        number_thread+=1
        
        semaphore.release()
        
        timeEnd = time.time() 
        
        THREAD_PER_SECONDE+=1
        threadsTime.append(timeEnd - timeStart) # Adiciona o tempo de execução de cada thread
    


def concurrent():
    # Função principal de execução com threads 
    
    print("\nFila Inicial: ", PROCESS.get(),"\n")

    t1 = (threading.Thread(target=moves_in_myQueue, args=(number_thread,)))
    t2 = (threading.Thread(target=moves_in_myQueue, args=(number_thread,)))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    duration = sum(threadsTime) 
    moves_per_seconds = THREAD_PER_SECONDE/duration
    
    return [duration, moves_per_seconds]

# if __name__=="__main__":
#     data_concurrent = concurrent()

#     print("\n\n------------- CONCORRENTE ----------------")
#     print("Duração: {0}s".format(data_concurrent[0]))
#     print("Movimentos por segundo: {0}".format(data_concurrent[1]))
#     print("------------------------------------------")