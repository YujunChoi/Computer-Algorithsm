from stack_queue import Stack
def parcheck(parseq):
    S= Stack()
    for symbol in parseq:
        if symbol == '(':
            S.push(symbol)
        else: #symbol ==')':
            if S.is_empty():
                return False
            else:
                S.pop()
        if S.is_empty():
            return True
        else:
            return False
        


print(parcheck('(()())'))




