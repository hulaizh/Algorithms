# Arthor: Hulai Zhang

def selection_sort(lst):
    for goThrough in range(len(lst)-1, 0, -1):
        posMax = 0
        for i in range(1, goThrough+1):
            if lst[posMax] < lst[i]:
                posMax = i
        lst[posMax], lst[goThrough] = lst[goThrough], lst[posMax]
    return lst
    
print(selection_sort([2, 6, 3, 1, 9]))