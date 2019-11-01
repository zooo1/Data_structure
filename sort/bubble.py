'''
Bubble Sort
인접한 두 개의 원소를 비교하여 자리를 교환하는 방식
O(n^2)
'''

def bubble_sort(ary):
    
    for i in range(len(ary)):
        for j in range(i+1, len(ary)):
            if ary[i] > ary[j]:
                ary[i], ary[j] = ary[j], ary[i]
    print(ary)
    
bubble_sort([4, 3, 2, 5, 67, 100, 23])
