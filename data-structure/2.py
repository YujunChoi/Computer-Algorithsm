class node:
    def __init__(self, data, next = None):
        self.data =data
        self.next = next

class ssl:
    def __init__(self):
        self.head = None
        self.size = 0
    def is_empty(self):
        if self.head == 0:
            return True
        else:
            return False
    def search(self, idx):
        if idx >= self.size:
            print('idx error :overflow')
        elif idx ==0:
            return self.head
        else:
            cur = self.head
            for _ in range(idx):
                cur = cur.next
            return cur 
    def append(self, val):
        if self.is_empty():
            self.head = node(val)
            self.size += 1
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            new = node(val)
            cur.next = new
            self.size += 1

    def insert(self, val , idx):
        if self.is_empty():
            self.head = node(val)
            self.size += 1
        elif idx ==0:
            self.head = node(val, self.head)
            self.size += 1
        elif idx > self.size:
            print('overflow')
            return 
        else:
            cur = self.search(idx -1)
            if cur ==None:
                return
            new = node(val)
            tmp =cur.next
            cur.next = new
            new.next = tmp
            self.size += 1

    def delete(self, idx):
        if self.is_empty():
            print('error!')
            return None
        elif 