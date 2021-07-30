class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class SLL_list:
    #노드 생성
    def __init__(self):
        self.head= Node(None)
        self.size = 0
    
    #노드 추가
    def append(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)
    
    def expression(self):
        currnet= self.head
        while currnet is not None:
            print(currnet.data)
            currnet = currnet.next

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next

if __name__ == '__main__':
    prac_list=SLL_list()
    prac_list.append(5)
    prac_list.expression