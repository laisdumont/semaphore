import random


class MyQueue:

    def __init__(self):
        self.myQueue = [random.randint(1,99) for _ in range(10)]  
        self.start = 0
        self.end = 9          
    
    def remove(self):
        value = self.myQueue[self.start]
        self.myQueue[self.start] = None
        if self.start < 9:
            self.start += 1
        else:
            self.start = 0
        return value
    
    def insert(self, value):
        if self.end < 9:
            self.end += 1
        else:
            self.end = 0
        self.myQueue[self.end] = value
        return value

    def get(self):    
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