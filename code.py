def gen(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2,x):
        if x % n == 0:
            return False
    return True

def prime(a,b):
    for i in range(a,b):
        if gen(i):
            yield i

print(list(prime(5,19))) 


