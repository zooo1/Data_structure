'''
Quick sort
pivot을 중심으로 pivot보다 작은 값은 pivot의 왼쪽, 
pivot보다 큰 값은 pivot의 오른쪽으로 옮겨 정렬하는 방식
'''
def quick_sort(ary):

    # ary의 길이가 1 이하라면 더 이상 정렬할 필요가 없다.
    if len(ary) <= 1:
        return ary
        
    pivot = ary[len(ary)//2]

    start_idx = 0
    end_idx = len(ary) - 1

    while start_idx < end_idx:
        # start_idx 
        while ary[start_idx] < pivot:
            start_idx += 1

        # end_idx
        while ary[end_idx] > pivot:
            end_idx -= 1
        
        if start_idx > end_idx:
            break

        ary[start_idx], ary[end_idx] = ary[end_idx], ary[start_idx]
        start_idx += 1
        end_idx -= 1

    start_idx -= 1

    # 값의 교환이 끝났다면 start idx를 기준으로 왼, 오른쪽을 나눈다.
    left_ary = quick_sort(ary[:start_idx])
    right_ary = quick_sort(ary[start_idx:])
    return left_ary+right_ary


print(quick_sort([6, 5, 1, 4, 7, 2, 3]))
print(quick_sort([3,9,4,7,5,0,1,6,8,2]))
print(quick_sort([100, 23, 22, 45, 11, 0, 1, 4]))

# 같은 값이 있는 경우는 커버 못 함 