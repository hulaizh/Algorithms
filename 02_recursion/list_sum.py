# Author: Hulai Zhang

def listSum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0]+listSum(numlist[1:])

print(listSum([1, 4, 5]))