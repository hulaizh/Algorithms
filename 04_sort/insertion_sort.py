# Arthor: Hulai Zhang

def insertion_sort(lst):
    for pos in range(1, len(lst)):
        current = pos
        current_value = lst[pos]
        while current > 0 and lst[current-1] > current_value:
            lst[current] = lst[current-1]
            current -= 1
        lst[current] = current_value
    return lst

import random
lst = [i for i in range(5) for j in range(5)]
random.shuffle(lst)
print(lst)
print(insertion_sort(lst))