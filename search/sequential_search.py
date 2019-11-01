def sequential_search_sorted(ary, key):
    # 오름차순으로 정렬되어 있을 때
    for num in ary:
        if key == num:
            return "key found!"
        elif key < num:
            return "no key here"
        
        
def sequential_search_not_sorted(ary, key):
    for num in ary:
        if key == num:
            return "key found"
    return "no key here"

print(sequential_search_sorted([1,2,3,4,5,6,7,10,100], 10))
print(sequential_search_sorted([1,2,3,4,5,6,7,10,100], 20))

print(sequential_search_not_sorted([1,10,7,2,3,5,100], 10))
print(sequential_search_not_sorted([1,10,7,2,3,5,100], 20))

