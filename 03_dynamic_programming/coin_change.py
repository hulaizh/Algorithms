# Author: Hulai Zhang

def coinChange(change, coinList, numCoins, changeCoin):
    for chg in range(change+1):
        minCoins = chg
        theCoin = 1
        for i in [c for c in coinList if c<=chg]:
            if numCoins[chg-i]+1 < minCoins:
                minCoins = numCoins[chg-i]+1
                theCoin = i
        numCoins[chg] = minCoins
        changeCoin[chg] = theCoin
    return numCoins[change]

def printCoin(change, changeCoin):
    chg = change
    while chg > 0:
        theCoin = changeCoin[chg]
        chg = chg - theCoin
        print(theCoin)

if __name__ == '__main__':
    change = 63
    coinList = [1, 5, 10, 21, 25]
    numCoins = [0]*64
    changeCoin = [0]*64
    print('Minimum coins number:', coinChange(change, coinList, numCoins, changeCoin))
    printCoin(change, changeCoin)