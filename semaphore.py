import threading
import time
import random
import queu


semaphore = threading.Semaphore(2)
process = queu.Queu()
threadsTime = []


def movimento_fila(i):
    # with semaphore:

    semaphore.acquire()
    timeStart = time.time()
    # time.sleep(random.random())
    old = process.remove()
    new = random.randint(1,99)
    process.insert(new)
    timeEnd = time.time()
    print('Thread-{0}: tira{1:3d}, poe{2:3d}, fila:{3}'.format(i+1,old, new, process.get()))
    threadsTime.append(timeEnd - timeStart)
    semaphore.release()


if __name__=="__main__":
    print("\nFila Inicial: ", process.get(),"\n")
    i = 0
    # clients = []
    while(sum(threadsTime) < 1):
        movimento_fila(i)
        # clients.append(threading.Thread(target=movimento_fila, args=(i,)))
        # clients[i].start()
        # clients[i].join()
        i += 1
    print("Duração:", sum(threadsTime))   
    print("Movimentos por Segundo:", i/sum(threadsTime)) 
