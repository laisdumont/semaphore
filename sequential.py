import threading
import time
import random
import queu

process = queu.Queu()
threadsTime = []

def movimento_fila():
    timeStart = time.time()
    # time.sleep(random.random())
    old = process.remove()
    new = random.randint(3,10)
    process.insert(new)
    timeEnd = time.time()
    print('tira{0:3d}, poe{1:3d}, fila:{2}'.format(old, new, process.get()))
    threadsTime.append(timeEnd - timeStart)

if __name__=="__main__":
    print("\nFila Inicial: ", process.get(),"\n")
    i = 0
    while(sum(threadsTime) < 1):
        movimento_fila()
        i += 1

    print("Duração:", sum(threadsTime))   
    print("Movimentos/s:", i/sum(threadsTime)) 