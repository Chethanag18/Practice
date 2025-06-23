"""Define a class Person and its two child classes: Male and Female. All classes have a method 
"getGender" which can print "Male" for Male class and "Female" for Female class."""
class Person:
    def __init__(self):
        self.male = "Male"
        self.female = "Female"
class Male(Person):
    def getGender(self):
        print(self.male)
class Female(Person):
    def getGender(self):
        print(self.female)
m1 = Male()
m1.getGender()
f2 = Female()
f2.getGender()