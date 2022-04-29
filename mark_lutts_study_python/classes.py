class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' %self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return 'ThirdClass: %s' %self.data
    def mul(self, other):
        self.data *= other

a = ThirdClass("abc") #вызов __init__
a.display() #SecondClass method
print(a) #call __str__

b = a + 'xyz' #call __add__, creation new object
b.display() #SecondClass method
print(b) #call __str__
a.mul(3) #изменение самого экземпдяра
print(a)

x = FirstClass()
y = FirstClass()

x.data = 456789
print(x.data)

x.anothername = 'это ахуеть че реально так можно?'
print(x.anothername)

z = SecondClass()
z.setdata(42)
z.display()
x.display()


class SharedData:
    s = 22

x = SharedData()
y = SharedData()
SharedData.s = 88
y.s = 58

print(x.s, y.s, SharedData.s)


class Wrapper:
    def __init__(self, ob):
        self.wrapped = ob

    def __getattr__(self, item):
        print('Trace:', item)
        return getattr(self.wrapped, item)

x = Wrapper([1,2,3])
x.append(88)
print(x.wrapped)