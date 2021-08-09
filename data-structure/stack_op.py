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

def calc(x):
    s2= Stack()
    for token in x:
        if token not in '+-*/':
            s2.push(token)
        elif token =='+':
            a=int(s2.pop())
            b=int(s2.pop())
            s2.push(b+a)
        elif token =='-':
            a=int(s2.pop())
            b=int(s2.pop())
            s2.push(b-a)
        elif token =='*':
            a=int(s2.pop())
            b=int(s2.pop())
            s2.push(b*a) 
        elif token =='/':
            a=int(s2.pop())
            b=int(s2.pop())
            s2.push(int(b/a))
    return int(s2.pop())

print(calc('632-4*+'))           

    



        
            

        
    
