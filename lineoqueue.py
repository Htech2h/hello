class CallCenter:
    def __init__(self):
        self.customers = []

    def is_empty(self):
        return self.customers == []

    def add(self, x):
        return self.customers.insert(0, x)

    def next(self):
            return self.customers.pop()


c = CallCenter()
#a function to determine how many names should be given
z = 2()
while z > 0:
    n = input("enter name")
    c.add(n)
    z -= 1

#your code goes here
time = 0
while True:
    if c.is_empty():
        break
    out = c.next()
    if out == "general":
        time+=5
    if out == "technical":
        time+=10

print(time)