# we need to classes
# 1. node -> value, next
# 2. LinkedList itself -> first (head), last (tail) of type Node class
# with methods: addfirst, addlast, deletefirst, deletelast, contains, indexof
import _ctypes

class Node():
    def __init__(self, value=None, _next=None):
        self.value = value
        self.next = _next # jesus
        
        
class LinkedList():
    def __init__(self, first=None, last=None, length=None):
        self.first = first
        self.last = last
        self.length = length if length else 0
        
    def addFirst(self, value):
        if self.length == 0:
            self.first = self.last = Node(value)
            self.length += 1
            return
        elif self.length > 0:
            # was_first_id = self.first
            self.first = Node(value, self.first)
            self.length += 1
            return
    
    def addLast(self, value):
        if self.length == 0:
            self.first = self.last = Node(value)
            self.length += 1
            return
        elif self.length > 0:
            was_last_node = self.last
            self.last = Node(value)
            was_last_node.next = self.last  # type: ignore
            self.length += 1
            return
    
    def deleteFirst(self):
        if self.length == 0:
            raise Exception('Linked List is empty!')
        elif self.length == 1:
            self.first = self.last = None
            self.length = 0
            return
        elif self.length > 1:
            self.first = self.first.next # type: ignore
            self.length -= 1
            return
            
    def deleteLast(self):
        if self.length == 0:
            raise Exception('Linked List is empty!')
        elif self.length == 1:
            self.first = self.last = None
            self.length = 0
            return
        elif self.length > 1:
            last_node = self.last
            current_node = self.first
            for i in range(self.length): # bruh
                if current_node.next == last_node: # type: ignore
                    current_node.next = None # type: ignore
                    self.last = current_node
                    self.length -= 1
                    return
                current_node = current_node.next # type: ignore
        
    def contains(self, value):
        # returns true of false
        return self.indexOf(value) != -1 # :D
        # saves a code :D
        if self.length == 0:
            return False
        elif self.length > 0:
            current_node = self.first
            while current_node is not None:
                if current_node.value == value:
                    return True
                current_node = current_node.next
            return False
    
    def indexOf(self, value):
        # return the index
        if self.length == 0:
            return -1
        elif self.length > 0:
            current_node = self.first
            index = 0
            while current_node is not None:
                if current_node.value == value:
                    return index
                current_node = current_node.next
                index += 1
            return -1
        
    def printList(self):
        if self.length != 0:
            current_node = self.first
            while current_node is not None:
                print(current_node.value)
                current_node = current_node.next
        else:
            print('Linked List is empty.')
            
    def toList(self):
        if self.length != 0:
            toList = []
            current_node = self.first
            while current_node is not None:
                toList.append(current_node.value)
                current_node = current_node.next
            return toList
        print('List is empty!')
        
    def reverse(self):
        # reverse in place
        if self.length != 0:
            current_node = self.first
            next_node = current_node.next # type: ignore
            while next_node is not None:
                next_temp = next_node.next 
                next_node.next = current_node
                if current_node == self.first:
                    current_node.next = None # type: ignore
                current_node = next_node
                next_node = next_temp
            self.first, self.last = self.last, self.first
                
    def getKthFromTheEnd(self, k:int):
        dis = k - 1
        p1 = p2 = self.first
        
        # move the second pointer
        current_node = self.first
        for i in range(dis):
            p2 = current_node.next # type: ignore
            current_node = current_node.next # type: ignore
            
        # move pointers
        current_p1 = self.first
        current_p2 = p2
        while current_p2 is not None:
            p2 = current_p2.next
            current_p2 = p2
            
            if current_p2 is not None:
                p1 = current_p1.next # type: ignore
                current_p1 = p1
        return p1.value # type: ignore
            
        
            

# test
linkedtest = LinkedList()

linkedtest.addFirst(1)
linkedtest.addLast(10)
linkedtest.addFirst(2)
linkedtest.addLast(20)
linkedtest.addFirst(3)
linkedtest.addLast(30)
linkedtest.addFirst(4)
linkedtest.addLast(40)
# print(linkedtest.length) # -> 4
# linkedtest.printList()

# linkedtest.printList()
print(linkedtest.toList())
linkedtest.reverse()
print(linkedtest.toList())
# print(linkedtest.printList())

# print(linkedtest.contains(3)) # -> True
# print(linkedtest.indexOf(30)) # -> 3

print(linkedtest.getKthFromTheEnd(1))

