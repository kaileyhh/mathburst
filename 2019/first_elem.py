def check(a = []):
    for i in range(len(a) - 1):
        if (a[i] > a[i+1]):
            #returns true if its wrong
            return True
    return False

def flip(index, a = []):
    b = [0 for i in range(len(a))]
    for i in range(index + 1):
        b[i] = a[index - i]

    for i in range(1, len(a) - index):
        b[index + i] = a[index + i]
    return b

def sort(a = []):
    print(a)
    uwu = 0

    
    
    if (a[0] == len(a)):
        a = flip(len(a)-1, a)
        if (check(a) == False):
            return a
        
    for i in range(2, len(a)):
        if (a[i] == a[0] + 1):
            uwu = 1
            a = flip(i-1, a)
            break
    if (check(a) == False):
        return a
    
    if (uwu == 0):
        for i in range(len(a)):
            if (a[i] == a[0] - 1):
                uwu = 1
                a = flip(i-1, a)
                break

    if (check(a) == False):
        return a
    
    if (uwu == 0):
        a = flip(len(a)-1,a)

    
    if (check(a) == True):
        a = sort(a)
    return a

print(sort([1,2,5,4,3]))
