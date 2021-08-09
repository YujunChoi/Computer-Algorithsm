from stack_queue import Queue

def rullet(n,k):
    Q=Queue()
    for cnt in range(1, n+1):
        Q.enqueue(cnt)
    while Q.size !=0:
        for i in range(1,k):
            Q.enqueue(Q.dequeue())
        Q.pop()
    return Q.dequeue()

