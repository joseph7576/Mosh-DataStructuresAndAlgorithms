# green apple 
# should return e ->
# using set :D

test_string = 'green apple'

for char in test_string:
    if test_string.count(char) > 1:
        print(char)
        break
    
# NAILED IT :D

def first_repeated_char(string:str):
    hashSet = set()
    for i in range(len(string)):
        if string[i] in hashSet:
            return string[i]
        hashSet.add(string[i])
            
    return "MIN_CHAR?"

print(first_repeated_char(test_string))