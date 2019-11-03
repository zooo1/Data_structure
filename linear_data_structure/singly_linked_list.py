'''
단일 연결 리스트
'''
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

# HEAD Node 뒤에 붙이기 
def insert(data, HEAD):
    new_Node = Node(data, None)
    new_Node.next = HEAD.next
    HEAD.next = new_Node
    
# TAIL Node 뒤에 붙이기 
def append(data, HEAD):
    new_Node = Node(data, None)
    # next node가 TAIL을 가리키는 node 찾기 
    p = HEAD
    while p.next.next != None:
        p = p.next

    TAIL = p.next
    p.next = new_Node
    new_Node.next = TAIL

# 초기화
HEAD = Node("HEAD", None)
TAIL = Node("TAIL", None)
HEAD.next = TAIL

insert("1st", HEAD)
append("2nd", HEAD)
insert("3rd", HEAD)
append("4th", HEAD)

p = HEAD
while p.next != None:
    print(p.data)
    p = p.next
    if p.next == None:
        print(p.data)



