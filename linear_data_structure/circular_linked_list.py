'''
원형 연결 리스트
'''
class Node:
    def __init__(self, data, next_node):
        self.next = next_node
        self.data = data

def initialize():
    HEAD = Node("HEAD", None)
    TAIL = Node("TAIL", HEAD)
    HEAD.next = TAIL
    return HEAD, TAIL


def create_node(data, order):
    global HEAD
    new_node = Node(data, None)
    # HEAD 바로 뒤에
    if order == 1:
        p = HEAD
        new_node.next = HEAD.next
        HEAD.next = new_node
    
    # TAIL 바로 앞에
    else:
        p = HEAD
        while p.next.next != HEAD:
            p = p.next
        new_node.next = p.next  # TAIL
        p.next = new_node


def delete_node(key):
    global HEAD
    p = HEAD
    while p.next.data != key:
        p = p.next
    p.next = p.next.next


def show():
    global HEAD
    flag = 1
    p = HEAD
    while 1:
        if p.data == "TAIL":
            print(p, p.data, p.next)
            break
        else:
            print(p, p.data, p.next)
            p = p.next
    print()


HEAD, TAIL = initialize()
create_node(1, 1)
show()
create_node(2, 3)
create_node(3, 1)
create_node(4, 3)
show()
delete_node(4)
show()




