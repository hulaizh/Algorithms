# Author: Hulai Zhang

def hanoiTower(n, fromPole, toPole, betweenPole):
    if n >= 1:
        hanoiTower(n-1, fromPole, betweenPole, toPole)
        moveDisk(fromPole, toPole)
        hanoiTower(n-1, betweenPole, toPole, fromPole)

def moveDisk(fromPole, toPole):
    print('Moving Disk:', fromPole, '->', toPole)

hanoiTower(3, 'A', 'B', 'C')