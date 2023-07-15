'''
- enqueue
- dequeue
- peek
- isEmpty
- isFull
- Front pointer
- Rear pointer
- [0,0,0,0,0]

for the love of god - think in simple terms - be simple man :D
'''

class QueueArray():
    def __init__(self, length:int):
        self.queue = [''] * length
        self.f = 0
        self.r = 0
        self.length = 0
        
    def enqueue(self, item):
        if self.length == len(self.queue):
            raise Exception('Queue is Full!')
        
        self.queue[self.r] = item
        
        self.r = (self.r + 1) % len(self.queue)
        self.length += 1
        
        return
            
    def dequeue(self):
        if self.length == 0:
            raise Exception('Queue is Full!')
        
        front = self.queue[self.f]
        self.queue[self.f] = ''
        
        self.f = (self.f + 1) % len(self.queue)
        self.length -= 1
        
        return front
    
    def peek(self):
        if self.length > 0:
            return self.queue[self.f] # peek the front
        raise Exception('Queue is empty!')

    def isEmpty(self):
        return True if self.length == 0 else False
    
    def isFull(self):
        return True if self.length == len(self.queue) else False
    

# let's test this stuff mate

def queueInfo(queue):
    print('queue:', queue.queue)
    print('length:', queue.length)
    print('front:', queue.f)
    print('rear:', queue.r)
    print('peak:', queue.peek())
    print('is empty:',queue.isEmpty())
    print('is full:', queue.isFull())
    print('='*20)

testQ = QueueArray(5)
testQ.enqueue(1)
testQ.enqueue(2)
testQ.enqueue(3)
testQ.enqueue(4)
testQ.enqueue(5)
queueInfo(testQ)
print(testQ.dequeue())
queueInfo(testQ)
testQ.enqueue(6)
queueInfo(testQ)


# testQ.enqueue(6) # should throw an error
# print(testQ.queue)
# print(testQ.length) # 5
# print(testQ.f)
# print(testQ.r)
# print(testQ.peek()) # 1
# print(testQ.queue) # [1,2,3,4,5]
# print(testQ.dequeue()) # 1
# print(testQ.dequeue()) # 2
# print(testQ.length) # 3
# # testQ.enqueue(6)
# # print(testQ.peek()) # 3
# print(testQ.queue)
# # print(testQ.f)
# # print(testQ.r)
# print(testQ.isEmpty()) # F
# print(testQ.isFull()) # True
# # print(testQ.queue)
# print(testQ.length) # 4
# print(testQ.dequeue())
# print(testQ.dequeue())
# print(testQ.peek())
# print(testQ.dequeue())
# print(testQ.isEmpty())
# print(testQ.length)
# print(testQ.dequeue()) 
# print(testQ.dequeue()) 
# print(testQ.dequeue()) 
# print(testQ.dequeue()) 
# print(testQ.dequeue()) 

# print('-'*20)
# testQ.enqueue(1)
# testQ.enqueue(2)
# testQ.enqueue(3)
# testQ.enqueue(4)
# testQ.enqueue(5)

# testQ.dequeue()
# testQ.dequeue()
# testQ.dequeue()
# print(testQ.queue)

# print(testQ.f)
# print(testQ.r)

# testQ.enqueue(6)
# testQ.enqueue(7)
# testQ.enqueue(8)
# # testQ.enqueue(9)

# print(testQ.queue)

#TODO: What the fuck is the problem with my code.