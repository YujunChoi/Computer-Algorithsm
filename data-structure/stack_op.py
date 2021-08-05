from stack_queue import Stack

def postfix_op(x):
    s = Stack()
    outstack=[]
    priority = {
        '*':3,
        '/':3,
        '+':2,
        '-':2,
        ')':4,
        '(':1
    }
    for token in x:
        if token not in '+-*/()':
            outstack.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            while s.top() != '(':
                outstack.append(s.pop())
            s.pop()
        else:
            if s.is_empty():
                s.push(token)
            else:
                while s.size() > 0:
                    if priority[s.top()] >= priority[token]:
                        outstack.append(s.pop())
                    else:
                        break
                s.push(token)
    while not s.is_empty():
        outstack.append(s.pop())
    return outstack

print(postfix_op('(A*B+C)/D'))



        
            

        
    
