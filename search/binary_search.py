def binary_search(ary, key, N):
    middle_idx = len(ary)//2
    if len(ary) == 1:
        if ary[middle_idx] != key:
            return "key not found"
    else:
        if ary[middle_idx] == key:
            return f"key found {middle_idx}"
        elif ary[middle_idx] < key:
            return binary_search(ary[middle_idx:], key, N)
        elif ary[middle_idx] > key:
            return binary_search(ary[:middle_idx], key, N) 

'''
참고한 함수
'''
def binary_search2(ary, left, right, key):
    if left > right:
        return False
    else:
        middle = (left + right) // 2
        if key == ary[middle]:
            return True
        elif key < ary[middle]:
            return binary_search2(ary, left, middle-1, key)
        elif key > ary[middle]:
            return binary_search2(ary, middle+1, right, key)
        
data = [2,4,6,9,11,19,23]
print(binary_search(data, 10, len(data)))
print(binary_search2(data, 0, len(data), 11))
print(binary_search2(data, 0, len(data), 10))