
class QueueStack():
    def __init__(self, length:int): # fuck the length mate
        self.front = [] # first stack
        self.rear = [] # second stack
        self.length = 0
        self.max_length = length
        
    def enqueue(self, item):
        if self.length == self.max_length:
            raise Exception('Queue is full!')
        
        if self.front:
            while self.front: # empty front to back
                self.rear.append(self.front.pop())
            self.front.append(item) # add item to front
            while self.rear: # fill the front
                self.front.append(self.rear.pop())        
            self.length += 1
            return
        
        # front is empty
        self.front.append(item)
        self.length += 1
        return
        
    def dequeue(self):
        if self.length == 0:
            raise Exception('Queue is empty!')

        front = self.front.pop()
        self.length -= 1
        return front
    
    def peek(self):
        if self.length > 0:
            return self.front[-1]
        raise Exception('Queue is empty!')
    
    def isEmpty(self):
        return False if self.front or self.rear else True
    
    def isFull(self):
        return self.length == self.max_length
    
def queueInfo(queue):
    print('front stack:', queue.front)
    print('rear stack:', queue.rear)
    print('length:', queue.length)
    try:
        print('peak:', queue.peek())
    except:
        print('peak: queue is empty')
    print('is empty:',queue.isEmpty())
    print('is full:', queue.isFull())
    print('='*20)
    
# it's testing time baby
testQ = QueueStack(5)
testQ.enqueue(1)
testQ.enqueue(2)
testQ.enqueue(3)
testQ.enqueue(4)
testQ.enqueue(5)
queueInfo(testQ)
print(testQ.dequeue())
queueInfo(testQ)
print(testQ.dequeue())
print(testQ.dequeue())
print(testQ.dequeue())
print(testQ.dequeue())
queueInfo(testQ)
