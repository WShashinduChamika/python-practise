# class Student:
#     name = "Kamal"
#     age = 20

# student1 = Student()
# print(student1.name)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

st1 = Student("Kamal", 23)
st2 = Student("Nimal", 43)

print(st1.name)
print(st2.name)