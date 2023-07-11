# stack with array :(
    # has push, pop, peek, isEmpty
    # and you should handle the scenario when is the stack is full?!)
    
class Stack():
    def __init__(self):
        self.stack = [] # my stack does not have any limitation on length :(((
        
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        raise Exception('Stack is empty!')
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return False if self.stack else True
    

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
stack.push(3)
print(stack.peek())
stack.pop()
stack.pop()
print(stack.isEmpty())
stack.pop()
print(stack.isEmpty())
