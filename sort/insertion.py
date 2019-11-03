'''
Insertion Sort
모든 요소를 앞에서부터 차례로 이미 정렬된 배열 부분과 비교하며 자신의 위치를 찾아 삽입
두 번째 요소(index=1)부터 검사하는 것이 특징이다.
O(n^2)
'''

def insertion_sort(ary):
    for i in range(1, len(ary)):
        tmp_idx = i
        for j in range(tmp_idx-1, -1, -1):
            if ary[tmp_idx] < ary[j]:
                ary[tmp_idx], ary[j] = ary[j], ary[tmp_idx]
                tmp_idx = j
    return ary
    
print(insertion_sort([8,5,6,2,4]))
