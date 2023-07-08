# how should i implement array class in python? bruh. python is like water :D

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
                return
            
            # extend array one cell to append item to array
            elif i == self.len_array - 1:
                self.array += ['']
                self.array[-1] = item
                self.len_array += 1
                return
            
    def removeAt(self, index):
        # index bigger than array length is meaningless
        if index > self.len_array - 1: raise Exception('Index out of range!')
        
        for i in range(self.len_array):
            if i == index:
                del self.array[index]
                self.len_array -= 1
                return
                
    def indexOf(self, item):
        for i in range(self.len_array):
            if self.array[i] == item:
                print(i)
                return
        print(-1)
        return
    
    def print_array(self):
        for i in range(self.len_array):
            if self.array[i]:
                print(self.array[i])
        print('---')
        
            
test_array = Array(length=3)
test_array.insert(item=10)
test_array.insert(item=20)
test_array.print_array()
test_array.insert(item=30)
test_array.insert(item=40)
test_array.print_array()
test_array.removeAt(index=3)
test_array.print_array()
test_array.indexOf(item=20)
test_array.indexOf(item=100)


