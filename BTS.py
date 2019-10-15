class Node:
    def __init__(self, left, data, right):
        self.left = left
        self.data = data
        self.right = right


def insert(p, item):
    if p.data > item:
        if p.left is None:
            p.left = Node(None, item, None)
        else:
            insert(p.left, item)
    else:
        if p.right is None:
            p.right = Node(None, item, None)
        else:
            insert(p.right, item)
    

def find(p, item):
    if item == p.data or p is None:
        print("find!")
    elif item < p.data:
        find(p.left, item)
    else:
        find(p.right, item)


def delete(item):
    p = root
    flag = 0
    while 1:
        if p.left.data == item:
            parent = p
            p = p.left
            flag = 1
            break
        elif p.right.data == item:
            parent = p
            p = p.right
            flag = 1
            break
        elif p.data > item:
            p = p.left
        elif p.data < item:
            p = p.right

    if flag:
        if p.left and p.right:
            q = p.right
            while q.left != None:
                q = q.left
            q.left = p.left
            parent.right = p.right
            print("p:", p.data)

        elif p.left:
            parent.left = p.left

        elif p.right:
            parent.right = p.right
        print("위치의 데이터", p.data)



def show(p):
    print(p.data)
    if p.left:
        show(p.left)
    if p.right:
        show(p.right)
    

# root 노드 만들어주기 
root = Node(None, 21, None)

items = [28, 14, 32, 25, 18, 11, 30, 19, 15, 23, 27]

for item in items:
    insert(root, item)

delete(28)
show(root)