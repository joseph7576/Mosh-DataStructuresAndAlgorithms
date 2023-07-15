stack = []

string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
len_string = len(string)

for i in range(len_string):
    stack.append(string[i])

reverse_string = ''

for i in range(len_string):
    reverse_string += stack.pop()
    
print(reverse_string)