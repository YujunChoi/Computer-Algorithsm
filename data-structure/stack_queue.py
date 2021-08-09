class Stack:
    def __init__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('Stack is empty')
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    def size(self):
        return len(self.items)
    def is_empty(self):
        if len(self.items) !=0:
            return False
        else:
            return True

class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0
        self.size =0

    def enqueue(self, val):
        self.items.append(val)
        self.size += 1
    
    def dequeue(self):
        if self.front_index == len(self.items):
            print('Queue is empty')
            return None
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x
    def pop(self):
        if len(self.items) != 0:
            self.size -= 1
            return self.items.pop(self.front_index)
        else:
            return -1