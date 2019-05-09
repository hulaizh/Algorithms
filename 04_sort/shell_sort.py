# Arthor: Hulai Zhang

def shell_sort(lst):
    gap = len(lst)
    while gap > 0:
        index = 0
        while index < gap:
            for pos in range(index+gap, len(lst), gap):
                current = pos
                current_value = lst[pos]
                while current > 0 and lst[current-gap] > current_value:
                    lst[current] = lst[current-gap]
                    current -= gap
                lst[current] = current_value
            index += 1
        gap = gap//2
    return lst

import random
lst = [i for i in range(5) for j in range(5)]
random.shuffle(lst)
print(lst)
print(shell_sort(lst))