# Author: Hulai Zhang

def sequential_search(aList, item):
    pos = 0
    found = False
    while pos < len(aList) and not found:
        if aList[pos] == item:
            found = True
        else:
            pos += 1
    return found

print(sequential_search([1,3,4,5], 3))