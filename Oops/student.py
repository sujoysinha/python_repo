class Student:
    def __init__(self, n='', m=0):
        self.name=n
        self.marks=m

    def display(self):
        print('Hi ', self.name)
        print('Your marks ', self.marks)

s=Student()
s.display()
print('...................................')

s1=Student('Sujoy Sinha', 500)
s1.display()
print('________________________________________')