def parcheck(s):
    d= {
        '(' : ')',
        '}' : '{',
        ']' : '['
    }
    stack =[]

    for symbol in s:
        if symbol in '(':
            stack.append(symbol)
        elif symbol in ')':
            if stack:
                top = stack.pop()
                if d[symbol] != top:
                    return False
            else:
                return False
    return len(stack) ==0

print(parcheck('(()())'))




