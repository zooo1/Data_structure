'''
Counting Sort
항목들의 순서를 결정하기 위해 집하에 각 몇 항목이 있는지 세는 작업을 하며
선형시간에 정렬하는 효율적인 알고리즘
'''
def counting_sort(ary):
    res = [-1] * len(ary)
    counts = [0] * (max(ary)+1)
  
    # 1. counting
    for num in ary:
        counts[num] += 1

    # 2. counting 누적
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
  
    # 3. 직접 인덱스되는 카운트 배열 저장
    for j in range(len(ary)-1, -1, -1):
        num = ary[j]
        counts[num] -= 1
        res[counts[num]] = num
        

counting_sort([0, 4, 1, 3, 1, 2, 4, 1])