'''
스택
한 쪽 끝에서만 자료를 넣고 뺄 수 있는 LIFO(Last In First Out) 형식의 자료구조
'''


# 1. 배열 형태의 stack
N = 10  # 배열의 크기
stack = [-1] * N
top = -1

def is_empty(top):
    return top < 0


def push(stack, data):
    global top
    top += 1
    stack[top] = data
    return stack


def pop(stack):
    global top
    if is_empty(top):
        return f"ERROR!!!!! Stack is Empty!"
    top -= 1
    return stack[top+1]

print(push(stack, 1))
print(push(stack, 2))
print(pop(stack))
print(pop(stack))
print(pop(stack))



# 2. linked list 형태의 stack
class Node:
    def __init__(self, data, prev_node, next_node):
        self.data = data
        self.prev = prev_node
        self.next = next_node


def is_empty():
    global TOP
    return TOP == None


def initialize(data):
    return Node(data, None, None)


def push(data):
    global TOP
    TOP.next = Node(data, TOP, None)
    TOP.next.prev = TOP
    TOP = TOP.next
    return TOP


def pop():
    global TOP
    if is_empty(): 
        return f"ERROR!!!! stack is Empty"

    res = TOP.data
    TOP = TOP.prev
    return res


def show():
    global TOP
    p = TOP
    while p.prev != None:
        print(p.data)
        p = p.prev
        if p.prev == None:
            print(p.data)
            break


TOP = initialize(1)
print(TOP)
print(push(2))
print(push(3))
print()
print("show")
show()
print()
print(pop())
print(pop())
print(pop())
print(pop())