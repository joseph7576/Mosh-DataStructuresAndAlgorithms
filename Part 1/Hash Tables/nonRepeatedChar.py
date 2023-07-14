# a green apple
# should return g because a is repeated 2 times...
# how can is solve this in python... hoom.
# should i use hash tables or what?


test_string = "a green apple"

for char in test_string.replace(' ', ''):
    if test_string.count(char) == 1:
        print(char)
        break
    
# bruh - EZ
# i should have used hash tables -_-
# also should include white space


def first_non_repeated_char(string:str):
    hashTable = {}
    for i in range(len(string)):
        if string[i] in hashTable.keys():
            hashTable[string[i]] += 1
            continue
        else:
            hashTable[string[i]] = 1
            continue
        
    for i in range(len(string)):
        if hashTable[string[i]] == 1:
            return string[i]

    return 'CHAR.MIN_CHAR!'

print(first_non_repeated_char(test_string))
