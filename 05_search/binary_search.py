# Author: Hulai Zhang

def binary_search(aList, item):
    left = 0
    right = len(aList)-1
    found = False
    while left < right and not found:
        middle = (left+right)//2
        if item == aList[middle]:
            found = True
        else:
            if item < aList[middle]:
                left = middle-1
            else:
                right = middle+1
    return found

print(binary_search([1,3,4,5], 3))