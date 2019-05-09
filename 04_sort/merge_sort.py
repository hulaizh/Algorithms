# Arthor: Hulai Zhang

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        middle = len(lst)//2
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:])
        merged_lst = []
        while left and right:
            merged_lst.append(left.pop(0) if left[0]<right[0] else right.pop(0))
        merged_lst.extend(left if left else right)
        return merged_lst

import random
lst = [i for i in range(5) for j in range(5)]
random.shuffle(lst)
print(lst)
print(merge_sort(lst))