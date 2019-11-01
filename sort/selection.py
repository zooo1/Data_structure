def selection_sort(ary):
    N = len(ary)
    for i in range(N):
        min_idx = i
        # 최소값, 최소값을 가지는 인덱스 구하기
        for j in range(i+1, N):
            if ary[j] < ary[min_idx]:
                min_idx = j
        ary[i], ary[min_idx] = ary[min_idx], ary[i]
    print(ary)

selection_sort([9, 6, 7, 3, 5])
        
        