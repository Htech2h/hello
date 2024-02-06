class User:
    user = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.email = f"{self.name}{age}@risinghigh.tech.ac.za"

        User.user += 1

    def employee_num(self):
        return User.user
    @classmethod
    def from_string(cls,emp):               
        name,age = emp.split(
        )
        return cls(name,age)

mike = User("mike",18)

sec_employee = User.from_string(input("detail").lower())

print(sec_employee.email)