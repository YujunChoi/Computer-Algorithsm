class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None
    
    def __str__(self):
        return str(self.data)
# __init__을 불러 데이터, 왼쪽 자식, 오른쪽 형제를 초기화하고 __str__을 사용해서 반환된 문자열 표현
class Tree:
    def __init__(self):
        self.root = None

    def preorderTraversal(self, node):
        print(node, end='') 
        if not node.left == None : 
            self.preorderTraversal(node.left) #left_node가 비어있지 않으면 left_node 호출 
        if not node.right == None : 
            self.preorderTraversal(node.right) #right_node가 비어있지 않으면 자기호출

    def inorderTraversal(self, node):
        if not node.left == None : self.inorderTraversal(node.left)
        print(node, end='')
        if not node.right == None : self.inorderTraversal(node.right)
    
    def postorderTraversal(self, node):
        if not node.left == None : self.postorderTraversal(node.left)
        if not node.right == None : self.postorderTraversal(node.right)
        print(node, end='')

    def makeRoot(self, node, left_node, right_node):
        if self.root ==None:
            self.root=node
        node.left=left_node
        node.right=right_node

if __name__=="__main__":
    node =[]
    node.append(Node('-')) 
    node.append(Node('*')) 
    node.append(Node('/')) 
    node.append(Node('A'))
    node.append(Node('B'))
    node.append(Node('C'))
    node.append(Node('D')) 

    m_tree =Tree()
    for i in range(int(len(node)/2)):
        m_tree.makeRoot(node[i],node[i*2+1],node[i*2+2])

    print(      '전위 순회: ',end=''); m_tree.preorderTraversal(m_tree.root)
    print('\n'+ '중위 순회: ',end=''); m_tree.inorderTraversal(m_tree.root)
    print('\n'+ '후위 순회: ',end=''); m_tree.postorderTraversal(m_tree.root)
