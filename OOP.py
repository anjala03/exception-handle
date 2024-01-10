class Student:
    def __init__(self, name, age, height, year):
        self.name= name
        self.age= age
        self.height= height
        self.year= year
    def __str__(self):
        return f"{self.name}, ({self.age}, {self.height}, {self.year})"
    def my_func(self):
        print("this is just to demonstrate that method can be formed inside class")


s1= Student("ram", 32, 5.1, 2002)
s2= Student("hari", 12, 5.0, 2000)

print (s1)
print (s2)
s1.my_func()
