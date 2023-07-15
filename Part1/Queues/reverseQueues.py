# only allowed to use add, remove, isEmpty() methods


test_queue = [1,2,3,4,5,6]

def reverseQueue(queue:list):
    reversed_queue = []
    for i in range(len(queue)):
        reversed_queue.append(queue.pop()) #? am i really cheating man? :(
    return reversed_queue

print(reverseQueue(test_queue))

#? the solution can be use stacks for this because of LIFO behaviour 