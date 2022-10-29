def check(a = []):
    for i in range(len(a) - 1):
        if (a[i] > a[i+1]):
            #returns true if its wrong
            return True
    #print('a')
    return False

def checkConsec(index, a = []):
    #print(index)
    if index != 0 or index != len(a)-1:
        if (abs(a[index-1] - a[index]) == 1):
            return True
        return False
    elif index == 0:
        if abs(a[index+1] - a[index]) == 1:
            return True
        return False
    else:
        return True
    return False

def flip(index, a = []):
    b = [0 for i in range(len(a))]
    for i in range(index + 1):
        b[i] = a[index - i]

    for i in range(1, len(a) - index):
        b[index + i] = a[index + i]
    return b

def sort(steps, a=[], previous = []):
    flipped = False

    #len(a) is on top
    if (a[0] == len(a)):
        ####print("len(a) on top")
        #print(0)
        previous = a
        a = flip(len(a) - 1, a)
        flipped = True
        print(a)
        steps+=1

    #default flip if theres 2 options and one flips biggest to top, do that one
    if flipped == False:
        ####print("default")
        #print(1)
        i = len(a)-1
        choice1 = 0
        choice1ind = 0
        choice2 = 0
        choice2ind = 1
        for i in range(len(a)-1, 1, -1):
        #while (i > 0):
            if abs(a[0]-a[i]) == 1 and choice1 == 0 and checkConsec(i, a) == False:
                choice1 = a[i]
                choice1ind = i
            elif abs(a[0] - a[i]) == 1 and checkConsec(i, a) == False:
                choice2 = a[i]
                choice2ind = i

        if a[choice1ind-1] == len(a):
            yes = choice1ind
        elif a[choice2ind - 1] == len(a) and choice2ind != 1:
            yes = choice2ind
        else:
            yes = choice1ind

        #print(a[yes])
            
        if(flip(yes-1,a) != a and flip(yes-1, a) != previous):
            previous= a
            a = flip(yes - 1, a)
            flipped = True
            print(a)
            steps+=1
        ###i -= 1

        

    #default flip doesn't work (bc all consecutive), so largest number up then down
    if flipped == False:
        ####print("bad alg")
        #print('2')
        index = 0
        max1 = 0
        for i in range(len(a)):
            if a[i] != i+1:
                if a[i] > max1:
                    max1 = a[i]
                    index = i
        if flip(index, a) != a and flip(index, a) != previous:
            previous = a
            a = flip(index, a)
            print(a)
            steps+=1
            a = flip(a[0] - 1, a)
            flipped = True
            print(a)
            steps+=1
        
    #what to do otherwise
    if flipped == False:
        #thing = False
        for i in range(len(a)-2, 2, -1):
            if checkConsec(i, a) == False and flip(i - 1, a) != a and flip(i - 1, a) != previous:
                previous= a
                a = flip(i - 1, a)
                flipped = True
                print(a)
                steps+=1
                break
            elif (checkConsec(i, a) == False and flip(i - 1, a) != a and flip(i-1, a) == previous):
                if (a[len(a)-1] != len(a)): #checks to make sure it isn't flipping the largest to the top if its already on the bottom
                    previous = a
                    a = flip(len(a)-1, a)
                    flipped = True
                    print(a)
                    steps+=1
                    break
                else:
                    previous = a
                    a = flip(len(a)-2, a)
                    flipped = True
                    print(a)
                    steps+=1
                    break

    if check(a) == False:
        print(steps)
        return a
    else:
        a = sort(steps, a, previous)
    return a
       
