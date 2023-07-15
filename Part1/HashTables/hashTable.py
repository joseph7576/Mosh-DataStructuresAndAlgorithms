# hashtable
# put(k, v)
# get(k) -> v
# remove (k)
# k: int - hehe :D
# v: string
# collision: chaining
# linkedlist<Entry>[] -> Entry wraps key value pair together
# [ ll, ll, ll, ll] # should have fixed lenght

#? learn more about importing in python :/
# from . # hell yeah baby :D
# from linkedListClass import LinkedList


class Node():
    def __init__(self, value=None, _next=None):
        self.value = value
        self.next = _next # jesus
        
        
class LinkedList():
    def __init__(self, first=None, last=None, length=None):
        self.first = first
        self.last = last
        self.length = length if length else 0 #TODO: fix the length thing
        
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
        
    def getValueFromIndex(self, index):
        if self.length == 0:
            return -1
        if index == 0:
            return self.first.value
        elif index == self.length - 1:
            return self.last.value
        else:
            current_node = self.first
            for i in range(index):
                current_node = current_node.next
            return current_node.value
        
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
    
    def delete(self, value):
        if not self.contains(value):
            raise Exception(f'{value} Not Exist!')
        
        current_node = self.first
        previous_node = self.first
        
        for i in range(self.length):
            if current_node.value == value:
                if current_node == self.first:
                    self.deleteFirst()
                    return
                elif current_node == self.last:
                    self.deleteLast()
                    return
                previous_node.next = current_node.next
                self.length -= 1
                return
            previous_node = current_node
            current_node = current_node.next
            
        print('something went wrong')
            
        
class Entry(): # object to wrap key with value
    def __init__(self, key, value): # could define types here but i'm not going to
        self.key = key
        self.value = value
        
    def __str__(self) -> str:
        return f'({self.key}, {self.value})' #* interesting!
        
class HashTable(): 
    def __init__(self, length:int):
        self.array = [''] * length # array of linked lists
        self.length = len(self.array)
        
    def put(self, key:int, value): # assume the key always be int for now - TODO: change it later
        # if self.length == self.max_length:
        #     raise Exception('HashTable Is Full?!') 
        index = self.hash(key)
        
        if self.array[index] == '': # initial linkedlist there
            ll = LinkedList()
            entry = Entry(key, value)
            ll.addLast(entry)
            
            self.array[index] = ll # type: ignore #!
            return
        
        # updating the value if the existing key is given
        ll = self.array[index] # act as bucket
        
        for entry in ll.toList(): # type: ignore
            if entry.key == key:
                entry.value = value
                return
            
        entry = Entry(key, value)
        ll.addLast(entry) # type: ignore #!
        return

    def hash(self, key):
        return key % self.length
    
    def get(self, key:int):
        index = self.hash(key)
        
        if self.array[index] == '':
            raise Exception('Key Not Exist!')
        
        ll = self.array[index]
        
        for entry in ll.toList(): # type: ignore
            if entry.key == key:
                return entry.value
            
        return -1 # not found
        
    def remove(self, key):
        index = self.hash(key)
        
        if self.array[index] == '':
            raise Exception('Key Not Exist!')

        ll = self.array[index]        
        
        for entry in ll.toList(): # type: ignore
            if entry.key == key:
                ll.delete(entry)
                return
            
        print('Something went wrong!')
                
            
# testing time babyeh
testHash = HashTable(5)

testHash.put(1, 'a')
testHash.put(2, 'b')
testHash.put(3, 'c')
testHash.put(4, 'd')
testHash.put(5, 'e')
testHash.put(6, 'f')
testHash.put(7, 'g')
testHash.put(8, 'h')
testHash.put(9, 'i')
testHash.put(10, 'j')
testHash.put(11, 'k')
testHash.put(12, 'l')
for i in range(1, 13):
    print(testHash.get(i))
# print(testHash.get(2))
# print(testHash.get(3))
# testHash.remove(2) -> also works :D
# testHash.remove(3)

# print(testHash.array)
for arr in testHash.array:
    for entry in arr.toList():
        print(entry)
    
# print(testHash.array[3].printList()) # what is None for?
# print(testHash.array[2].printList())