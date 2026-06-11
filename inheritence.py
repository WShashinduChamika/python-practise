class Phone1:
    def feature1(self):
        print('Camera')

class Phone2 ():
    def feature2(self):
        print('Internet')

class Phone3 (Phone2):
    def feature3(self):
        print('Bluetooth')

class Phone4 (Phone1, Phone2):
    def feature4(self):
        print('5G Connection')

# myObj = Phone3()
# myObj.feature1()
# myObj.feature2()
# myObj.feature3()


myObj = Phone4()
myObj.feature1()
myObj.feature2()
myObj.feature4()

