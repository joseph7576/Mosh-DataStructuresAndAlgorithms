# how should i implement array class in python? bruh. python is like water :D
# try to think very basic!
# class should be initialize with fixed size, have insert, removeAt, indexOf, print methods

import array # -> wow!
import ctypes # -> holy wow!

class Array():
    def __init__(self, length:int):
        self.array = [''] * length
        self.len_array = len(self.array)
        
    def insert(self, item):
        for i in range(self.len_array):
            # add to array when array is not full
            if not self.array[i]:
                self.array[i] = item
                return # TODO: user return or break?
        
        # extend array 
        new_array = [''] * ( 2 * self.len_array)
        for i in range(len(new_array)):
            if i < self.len_array:
                new_array[i] = self.array[i]
            else:
                new_array[i] = item
                self.array = new_array
                self.len_array = len(self.array)
                return
            
    def removeAt(self, index):
        # validate index
        if index >= self.len_array or index < 0: raise Exception('Index out of range!')
        
        # shift to left
        # 1 2 3 4 5
        # 1 3 4 5 -
        # from 1 to 3
        for i in range(index, self.len_array - 1): # len array minus one is important
            self.array[i] = self.array[i + 1]
        self.len_array -= 1
                
    def indexOf(self, item):
        for i in range(self.len_array):
            if self.array[i] == item:
                print(i)
                return i
        print(-1)
        return -1
    
    def print_array(self):
        for i in range(self.len_array):
            if self.array[i]: #? is this really a cheat?
                print(self.array[i])
        print('---')
        
            
# testing
test_array = Array(length=3)

test_array.insert(item=10)
test_array.insert(item=20)
test_array.print_array()

test_array.insert(item=30)
test_array.insert(item=40)
test_array.print_array()

test_array.removeAt(index=3)
test_array.print_array()

test_array.insert(50)
test_array.insert(60)
test_array.insert(70)
test_array.print_array()

test_array.removeAt(3)
test_array.print_array()

test_array.removeAt(0)
test_array.print_array()

test_array.indexOf(item=10)

# test_array.indexOf(item=20)
# test_array.removeAt(index=100)