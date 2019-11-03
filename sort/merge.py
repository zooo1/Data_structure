'''
Merge Sort
주어진 리스트의 1이 될 때까지 나눈(divide) 후 
분할된 리스트를 정렬하며 합하여 정렬된 리스트가 되도록 만드는 방법
'''

def merge(left_ary, right_ary):
    print(left_ary, right_ary)
    new_ary = []
    i, j = 0, 0 
    # 합치는 과정 
    while i < len(left_ary) and j < len(right_ary):
        if left_ary[i] < right_ary[j]:
            new_ary.append(left_ary[i])
            i += 1
        else:
            new_ary.append(right_ary[j])
            j += 1

    # 둘 중 하나가 먼저 끝났을 경우
    if i < len(left_ary):
        new_ary.extend(left_ary[i:])
    if j < len(right_ary):
        new_ary.extend(right_ary[j:])

    return new_ary
    


    
def merge_sort(ary):
    if len(ary) == 1:
        return ary
    
    left = merge_sort(ary[:len(ary)//2])
    right = merge_sort(ary[len(ary)//2:])
    merged = merge(left, right)
    return merged

print(merge_sort([21, 10, 12, 20, 25, 13, 15, 22]))