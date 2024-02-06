def push(a,b):
    c = a.insert(0,b)
    return c

def pop(a):
    if a == []:
        pass
    else:
        c = a.pop(0)
        return c
    
a = []
b = input("exp")

for i in b:
    if i == "(":
        push(a,i)
    if i == ")" and len(a) >= 1:
        pop(a)
        continue
    if i == ")" and len(a) == 0:
        push(a,i)

print(len(a) == 0)


