'''
큐
스택과 마찬가지로 삽입, 삭제의 위치가 제한적인 구조
앞에서는 삭제, 뒤에서는 삽입만 이루어지는 구조
'''

'''
# 배열
Queue = [-1] * 5

def enQueue(data):
    global rear
    if queue_full():
        return "Queue is Full"
    Queue[rear] = data
    rear += 1
    return Queue[rear-1]


def deQueue():
    global front
    if queue_empty():
        return "Queue is Empty"
    front += 1
    return Queue[front-1]


def queue_empty():
    global front, rear
    return front > rear


def queue_full():
    global rear
    return len(Queue) <= rear


front, rear = 0, 0 
print(enQueue(1))
print(enQueue(2))
print(enQueue(3))
print(enQueue(4))
print(enQueue(5))
print(enQueue(6))
print(deQueue())
print(deQueue())
print(deQueue())
'''

# 연결 큐
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node
    

def initialize():
    global front, rear
    front = Node("초기화", None)
    rear = front
    return rear.data, front.data

    
def enQueue(data):
    global rear
    rear.next = Node(data, None)
    rear = rear.next
    return rear.data


def deQueue():
    global front
    if is_empty():
        return f"Queue is Empty!"
    res = front.data
    front = front.next
    return res


def is_empty():
    global front
    return front == None


front, rear = Node(None, None), Node(None, None)
print(initialize())
print(enQueue(1))
print(enQueue(2))
print(enQueue(3))
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
