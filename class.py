class Phone:
    def say(self, name):
        self.x = name;
        print("Hello "+ name)

phone1 = Phone()
phone1.say("nokiya")
print(phone1.x)

phone1.x = "apple"
print(phone1.x)