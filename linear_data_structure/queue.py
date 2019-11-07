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


'''
# 연결 큐
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node
    

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        # Queue가 비어있는 경우 알려준다.
        return self.front == None

    def initialize(self):
        self.front = self.rear = Node("first data", None)
        return self.front
    
    def enQueue(self, data):
        self.rear.next = Node(data, None)
        self.rear = self.rear.next
        return self.rear

    def deQueue(self):
        if self.is_empty():
            return f"Queue is Empty!"
        res = self.front.data
        self.front = self.front.next
        return res

    def show(self):
        p = self.front
        while p!=self.rear:
            print(p.data)
            p = p.next


queue = Queue()
print(queue.initialize())
print(queue.enQueue(1))
print(queue.enQueue(2))
print(queue.enQueue(3))
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
'''

'''
# 원형 큐
Queue = [0] * 4
front, rear = 0, 0
def is_empty():
    global front, rear
    return front == rear

def is_full():
    return (rear+1)%len(Queue) == front

def enQueue(data):
    global front, rear
    if is_full():
        return f"Queue is Full"
    N = len(Queue)
    rear = (rear+1) % N
    Queue[rear] = data
    return rear, Queue[rear]

def deQueue():
    global front, rear
    if is_empty():
        return f"Queue is Empty"
    front = (front+1) % len(Queue)
    return front, Queue[front]

print(enQueue(1))
print(enQueue(2))
print(enQueue(3))
print(enQueue(4))
print(enQueue(5))
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
'''

# 덱(Deque)
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node
    
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None
    
    def initialize(self):
        self.front = self.rear = Node("first data", None)

    def push_front(self, data):
        self.front = Node(data,self.front)
        return self.front.data
    
    def push_back(self, data):
        self.rear.next = Node(data, None)
        self.rear = self.rear.next
        return self.rear.data

    def pop_front(self):
        if is_empty():
            return f"Queue empty!"
        res = self.front.data
        self.front = self.front.next
        return res

    def pop_back(self):
        if is_empty():
            return f"Queue empty!"
        res = self.rear.data
        self.rear = self.rear.next
        return res

    def show(self):
        p = self.front
        while p != None:
            print(self.front.data)
            p = p.next

deque = Deque()
deque.initialize()
print(deque.push_front(1))
print(deque.push_front(2))
print(deque.push_front(3))
print(deque.push_back(4))
print(deque.push_back(5))
print(deque.push_back(6))

