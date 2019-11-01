def quick_sort(ary, start, end):
    
    if start >= end:
        return f"{ary}"
    else:
        pivot_idx = (start + end) // 2  
        print("pivot idx", pivot_idx)
        new_start, new_end = start, end
        while new_start < new_end:
            if ary[new_start] < ary[pivot_idx]:
                new_start += 1
            if ary[new_end] > ary[pivot_idx]: 
                new_end -= 1
            print(new_start, new_end)
        ary[new_start], ary[new_end] = ary[new_end], ary[new_start]
        
        # 왼쪽
        quick_sort(ary, start, pivot-1)
        # 오른쪽
        quick_sort(ary, pivot, end)

data = [5,3,8,4,9,1,6,2,7]
print(quick_sort(data , 0, len(data)-1))