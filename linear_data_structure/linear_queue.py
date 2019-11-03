'''
선형 큐
1차원 배열을 이용한 큐
잘못된 포화 상태 인식으로 메모리를 낭비할 수 있다.
'''

def initialize():
    return -1, -1


def enQueue(data):
    global rear
    if is_full():
        return f"Queue is Full!!"
    rear += 1
    Queue[rear] = data
    return Queue


def deQueue():
    global front
    if is_empty():
        return f"Queue is Empty"
    front += 1
    return Queue[front]


def is_empty():
    return front + 1 > rear


def is_full():
    return rear+1 > N-1


N = 5
Queue = [-1] * N
front, rear = initialize()
print(enQueue(1))
print(enQueue(2))
print(enQueue(3))
print(enQueue(1))
print(enQueue(2))
print(enQueue(3))
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
