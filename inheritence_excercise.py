class Parent:
    def function1(self):
        print("Hello")

class Child(Parent):
    def function2(self):
        super().function1()
        print("Welcome")

myObj = Child()
myObj.function2()


class Fruit:
    number_of_fruits = None
    unit_price = None

    def set_value(self, x, y):
        self.number_of_fruits = x
        self.unit_price = y

class Apple(Fruit):
    def price(self):
        print('For Apple ' + str(self.number_of_fruits * self.unit_price))

class Orange(Fruit):
    def price(self):
        print('For Orange ' + str(self.number_of_fruits * self.unit_price))



myObj1 = Apple()
myObj2 = Orange()

myObj1.set_value(10, 200)
myObj2.set_value(20, 300)

myObj1.price()
myObj2.price()