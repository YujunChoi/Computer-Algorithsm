class DisjoinSet:
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]
        self.size = n
    def find(self, index):
        value= self.data[index]
        if value <0:
            return index
        
        return self.find(value)
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.data[x] < self.data[y]:
            self.data[x] += self.data[y]
            self.data[y] = x
        else:
            self.data[y] += self.data[x]
            self.data[x] = y
        
        self.size -= 1

disjoint = DisjoinSet(10)

disjoint.union(0,1)
disjoint.union(1,2)
disjoint.union(2,3)
disjoint.union(4,5)
disjoint.union(5,6)
disjoint.union(6,7)
disjoint.union(8,9)

print(disjoint.data)
print(disjoint.size)