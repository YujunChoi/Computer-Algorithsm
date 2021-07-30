#Single Linked List

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SList:
    def __init__(self):
        self.head = Node(next)
        self.size = 0
        
    def listSize(self):
        return self.size
    
    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True
        
    def selectNode(self, idx):
        if idx >= self.size:
            print("Index Error")
            return None
        if idx == 0:
            return self.head
        else:
            tail = self.head
            for cnt in range(idx):
                tail = tail.next
            return tail
        
    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.size += 1
    
    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            newtail = Node(value)
            tail.next = newtail
            self.size += 1
        
    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        elif idx == 0:
            self.head = Node(value, self.head)
            self.size += 1
        else:
            tail = self.selectNode(idx-1)
            if tail == None:
                return
            newNode = Node(value)
            tmp = tail.next
            tail.next = newNode
            newNode.next = tmp
            self.size += 1
        
    def delete(self, idx):
        if self.is_empty():
            print('Underflow: Empty Linked List Error')
            return
        elif idx >= self.size:
            print('Overflow: Index Error')
            return
        elif idx == 0:
            tail = self.head
            self.head = tail.next
            del(tail)
            self.size -= 1
        else:
            tail = self.selectNode(idx-1)
            deltarget = tail.next
            tail.next = tail.next.next
            del(deltarget)
            self.size -= 1
            
    def printlist(self):
        target = self.head
        while target:
            if target.next != None:
                print(target.data, '-> ', end='')
                target = target.next
            else:
                print(target.data)
                target = target.next


if __name__ == '__main__':
    a= SList()
    a.append(5)
    a.printlist()
    a.append(6)
    a.printlist()