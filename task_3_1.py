from collections import deque

class task_3_1:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        self.requests.append(t)
        return len(self.requests)


counter = task_3_1()
print(counter.ping(1))  
print(counter.ping(100))  
print(counter.ping(3001))  
print(counter.ping(3002))  
