def quick_sort(ary):

    # ary의 길이가 1 이하라면 더 이상 정렬할 필요가 없다.
    if len(ary) <= 1:
        return ary

    # pivot을 정한다
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
        
        ary[start_idx], ary[end_idx] = ary[end_idx], ary[start_idx]
        start_idx += 1
        end_idx -= 1
        
    start_idx -= 1

    # 값의 교환이 끝났다면 start idx를 기준으로 왼, 오른쪽을 나눈다.
    print(start_idx, ary[:start_idx], ary[start_idx:])
    left_ary = quick_sort(ary[:start_idx])
    right_ary = quick_sort(ary[start_idx:])
    return left_ary+right_ary


print(quick_sort([6,5,1,4,7,2,3]))

