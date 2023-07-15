string = '([<1> x [2]])([<>])[]<>'
len_string = len(string)

stack = []

for i in range(len_string):
    if string[i] in ['(', '[', '<']:
        stack.append(string[i])
        continue
    elif string[i] in [')', ']', '>']:
        if stack:
            last_item = stack.pop()
            exp = last_item + string[i]
            if exp in ['()', '[]', '<>']: #* u can also use index comparison with predefined lists of brackets.
                continue
            else:
                print('OY!')
                exit() # -> jesus!
        print('OYOY!!')
        exit()

if stack:
    print('OYOYOY!!!')
else:
    print('ALL GOOD MATE!')