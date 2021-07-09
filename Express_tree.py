class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

class Express_Tree:
    def __init__(self):
        self.root =None

    def makeRoot(self, node, left_node, right_node):
        if self.root == None : self.root=node
        node.left= left_node
        node.right = right_node
    def preorderTraversal(self, node):
        print(node, end='')
        if not node.left == None : self.preorderTraversal(node.left)
        if not node.right == None : self.preorderTraversal(node.right)
    def inorderTraversal(self, node):
        if not node.left == None : self.inorderTraversal(node.left)
        print(node, end='')
        if not node.right == None : self.inorderTraversal(node.right)
    def postorderTraversal(self, node):
        if not node.left == None : self.postorderTraversal(node.left)
        if not node.right == None : self.postorderTraversal(node.right)
        print(node, end='')

class expression:
    def switch(self, arg):
        self.case_name = 'case_' + str(arg)
        self.case= getattr(self, self.case_name, lambda: )



if __name__ == "__main__":
    node =[]
    node.append(Node('/'))
    node.append(Node('*'))
    node.append(Node('7'))
    node.append(Node('1'))
    node.append(Node('-'))
    node.append(Node('5'))
    node.append(Node('2'))

