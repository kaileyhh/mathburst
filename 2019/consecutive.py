from math import *

def flip(index, a = []):
    b = [0 for i in range(len(a))]
    for i in range(index + 1):
        b[i] = a[index - i]

    for i in range(1, len(a) - index):
        b[index + i] = a[index + i]
    return b

def check(a = []):
    for i in range(len(a) - 1):
        if (a[i] > a[i+1]):
            #returns true if its wrong
            return True
    return False

def check2(a = []):
    for i in range(len(a) - 1):
        if (a[i] < a[i+1]):
            #returns true if its wrong
            return True
    return False

def checkConsecutive(a = []):
    b = [0 for i in range(len(a))]
    counter = 0
    for i in range(0, len(a) - 1):
        if (abs(a[i] - a[i+1]) == 1):
            b[i] +=1
            b[i+1]+=1
    for i in range(len(b)):
        if (b[i] > 0): counter+=1
    if(b[0] == 1): counter+=1
    if(b[len(b)-1] == len(b)): counter+=1
    return counter

def findBestConsecutiveFlip(a = []):
    uwu = 0
    max1 = checkConsecutive(a)
    best = [0 for i in range(len(a))]
    for i in range(1,len(a)-1):
        b = flip(i, a)
        if (checkConsecutive(b) > max1):
            max1 = checkConsecutive(b)
            for j in range(len(b)):
                best[j] = b[j]
            uwu = 1
    print(uwu)
    if(uwu==1):
        return best
    return a

def functionUwu(a = []):
    print(a)
    a = findBestConsecutiveFlip(a)
    print('hi')
    if check2(a) == False:
        a = flip(len(a)-1, a)
        print('hello')
        return a
    elif check(a):
        print('sup')
        a = functionUwu(a)
    else:
        print('ni hao')
        return a
    return a

print(functionUwu([7,8,6,2,5,4,1,3]))
