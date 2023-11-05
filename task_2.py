from collections import deque

class task_2:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int):
        self.queue1.append(x)
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

    def pop(self) -> int:
        popped = self.queue1.popleft()
        while self.queue2:
            self.queue1.append(self.queue2.popleft())
        return popped

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1


stack = task_2()
stack.push(1)
stack.push(2)
print(stack.top()) 
print(stack.pop())  
print(stack.empty()) 
