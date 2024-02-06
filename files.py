class animal:
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
    def __sub__(self,other):
        return animal(self.s1 - other.s1, self.s2 - other.s2)
    
f1 = animal(2,4)
f2 = animal(3,6)
res = f1 - f2

print(res.s1)
print(res.s2)


