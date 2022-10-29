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

def generate(size, a = [], b = []):
    owo = False
    for k in a:
        d = k
        for i in range(size - 1):
            c = flip(i + 1, d)
            if(check(b, c)):
                b+= [c]
    if len(b) == fac(size):
        print(b)
        return b
    else:
        print("length is ", len(b))
        b = generate(size,  b, [])


print('hi')
print(generate(6, [[i+1 for i in range(6)]], []))

