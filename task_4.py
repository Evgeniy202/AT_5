class task_4:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.size = k
        self.front = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            self.count += 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (selffront + 1) % self.size
            self.count -= 1
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


obj = task_4(3)
print(obj.enQueue(1))  
print(obj.enQueue(2))  
print(obj.enQueue(3))  
print(obj.enQueue(4))  
print(obj.Rear())  
print(obj.isFull())  
print(obj.deQueue())  
print(obj.enQueue(4))  
print(obj.Rear())  
