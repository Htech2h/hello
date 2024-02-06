class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def bar(self):
        print("grrr...")

class Dog(Animal):
    def bark(self):
        print("wooof")

fido = Dog("fido","black")
fido.bark()
fido.bar()

