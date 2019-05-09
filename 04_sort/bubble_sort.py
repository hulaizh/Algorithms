# Arthor: Hulai Zhang

def bubble_sort(lst):
    goThrough = len(lst)-1
    exchange = True
    while goThrough > 0 and exchange:
        exchange = False
        for i in range(goThrough):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                exchange = True
    return lst

import random
lst = [i for i in range(5) for j in range(5)]
random.shuffle(lst)
print(lst)
print(bubble_sort(lst))