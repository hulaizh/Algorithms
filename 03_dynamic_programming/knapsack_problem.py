# Author: Hulai Zhang

def knapsack(maxLoad, weightList, valueList, maxValueWithWeight, items):
    for i in range(maxLoad+1):
        maxValue = 0
        theItem = 0
        for j, weight in [(h, w) for h, w in enumerate(weightList) if w <= i]:
            if maxValueWithWeight[i-weight]+valueList[j] > maxValue:
                maxValue = maxValueWithWeight[i-weight]+valueList[j]
                theItem = j
        maxValueWithWeight[i] = maxValue
        items[i] = theItem
    return maxValueWithWeight[i]