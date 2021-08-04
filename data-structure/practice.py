from stack_queue import Stack
def parcheck(parseq):
    S= Stack()
    for symbol in parseq:
        if symbol == '(':
            S.push(symbol)
        else: #symbol ==')':
            if S !=None:
                S.pop()
        if S.__len__()==0:
            return True
        else:
            return False
        


print(parcheck('(()())'))




