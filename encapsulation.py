class myClass:
    x = 10
    __y = 20

    def display(self):
        return self.__y
    
    def meth1(self):
        print("Hello")
        self.__meth2()
    
    def __meth2(self):
        print("Welcome")


myObj = myClass()
print(myObj.display())
myObj.meth1()
