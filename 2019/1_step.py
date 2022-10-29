def flip(index, a = []):
    b = [0 for i in range(len(a))]
    for i in range(index + 1):
        b[i] = a[index - i]

    for i in range(1, len(a) - index):
        b[index + i] = a[index + i]
    return b

def check(arr1 = [], arr2 = []):
    for i in range(len(arr1)):
        if arr2 == arr1[i]:
            return False
    return True

def fac(n):
    a = 1
    for i in range(1, n+1):
        a = a * i
    return a

def generate(size, n, a = [], b = []):
    for i in range(n):
        b = []
        owo = False
        for k in a:
            d = k
            for i in range(size - 1):
                c = flip(i + 1, d)
                if(check(a, c)):
                    b+= [c]
        for i in range(len(b)):
            a += [b[i]]
    print(b)


print('hi')
#6 is size of array, 2 is amount of steps away, 6 is size of array (again)
print(generate(6, 2, [[i+1 for i in range(6)]], []))


