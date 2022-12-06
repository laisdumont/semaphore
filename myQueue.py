import random


class MyQueue:
    # Classe de implementação da fila

    def __init__(self):
        # Inicia a fila de tamanho 10 com valores aleatórios
        # A variável "start" indica onde está o começo da fila
        # A variável "end" indica onde está o final da fila

        self.myQueue = [random.randint(1,99) for _ in range(10)]  
        self.start = 0
        self.end = 9          
    
    def remove(self):
        # Remove o primeiro elemento da fila e atribui um novo index para o começo da fila

        value = self.myQueue[self.start]
        self.myQueue[self.start] = None
        if self.start < 9:
            self.start += 1
        else:
            self.start = 0
        return value
    
    def insert(self, value):
        # Adiciona o último elemento a fila e atribui um novo index para o final da fila

        if self.end < 9:
            self.end += 1
        else:
            self.end = 0
        self.myQueue[self.end] = value
        return value

    def get(self):
        # Retorna os valores da fila

        list_myQueue = []
        if (self.end >= self.start):
            for i in range(self.start, self.end + 1):
                list_myQueue.append(self.myQueue[i])
        else:
            for i in range(self.start, 10):
                list_myQueue.append(self.myQueue[i])
            for i in range(0, self.end + 1):
                list_myQueue.append(self.myQueue[i])
        return list_myQueue