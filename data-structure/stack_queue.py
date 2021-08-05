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
