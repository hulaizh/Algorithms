# Arthor: Hulai Zhang

def quick_sort(lst):
    left = 1
    right = len(lst)-1
    if left < right:
        return lst
    else:
        median = lst[0]



import random
lst = [i for i in range(5) for j in range(5)]
random.shuffle(lst)
print(lst)
print(quick_sort(lst))