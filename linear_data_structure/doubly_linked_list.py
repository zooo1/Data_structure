'''
이중 연결 리스트
'''
class Node:
    def __init__(self, prev_node, data, next_node):
        self.prev = prev_node
        self.data = data
        self.next = next_node
    

def create_head():
    return Node(None, "HEAD", None)


def insert2head():
    global cnt1
    next_node = HEAD.next
    cnt1 += 1
    if next_node:
        HEAD.next = Node(HEAD, cnt1, next_node)
        next_node.prev = HEAD.next
    else:
        HEAD.next = Node(HEAD, cnt1, None)


def insert2tail():
    global cnt2
    p = HEAD
    while p.next != None:
        p = p.next
    cnt2 += 1
    p.next = Node(p, cnt2, None)


def delete(item):
    p = HEAD
    flag = 0
    while 1:
        if p.data == item:
            break
        elif p == None:
            flag = 1
            break
        else:
            p = p.next

    p.prev.next = p.next 
    p.next.prev = p.prev


def show():
    p = HEAD
    while p != None:
        print(f"prev: {p.prev} \tnode:{p}\tdata:{p.data}\tnext:{p.next}")
        p = p.next



# HEAD 생성
HEAD = create_head()
cnt1, cnt2 = 0, 0
insert2head()
insert2head()
insert2tail()
insert2tail()
delete(1)
show()