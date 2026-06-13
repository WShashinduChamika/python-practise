class Parent:
    x  = 40

    def func(self):
        print("Hello")

class Clid(Parent):
    x  = 50

    def func(self):
        print('Welcome')

myObj = Clid()
print(myObj.x)
myObj.func()