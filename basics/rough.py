class Person:
    def __init__(self):
        self.name=""
        self.age=0

    def set_name(self,n):
        self.name=n

    def get_name(self):
        return self.name

    def set_age(self,a):
        self.age=a

    def get_age(self):
       return self.age

class Tanvi(Person):
    def __init__(self):
        self.length = 0
        self.width = 0

    def setLength(self, l):
        self.length = l

    def getLength(self):
        return self.length

    def setWidth(self, w):
        self.width = w

    def getWidth(self):
        return self.width

t = Tanvi()
t.set_age(20)
t.set_name("tanvi")
t.setLength(10)
t.setWidth(20)
print("age: ",t.get_age())
print("name: ",t.get_name())
print("length: ",t.getLength())
print("width: ",t.getWidth())
