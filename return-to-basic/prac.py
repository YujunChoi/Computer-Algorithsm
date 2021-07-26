def find(target):
    if target == parent[target]:
        return target
    
    parent[target] =find(parent[target])
    return parent[target]

def union(a, b):
    a=find(a)
    b=find(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

parent = [0,1,2,3,4,5]

if find(3) == find(5):
    print("same union")
else:
    print("not same")

union(3,5)

if find(3)== find(5):
    print("same")
else:
    print("not same")
    


    
