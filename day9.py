'''
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

s1 = "Hello how are you"
s2 = "Hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if not val in s2:
        print(val)
for val in s2:
    if not val in s1:
        print(val)
'''
'''
# 3.)Wrire a code print the 8th fibanochi number

num = 8
n1 = 0
n2 = 1

for val in range(8):
    ans = n1+n2
    n1=n2
    n2=ans
print(ans)

# constructors
# Eg:2
# unparametarised constructor
class profile:
    def __init__(self):
        print("hello world")
obj = profile()
obj.__init__()

# Problem Statement -: A taxi can take multiple passengers to the railway station at the same time.On the way back to the starting point,the taxi driver may pick up additional passengers for his next trip to the airport.A map of passenger location has been created,represented as a square matrix.

The Matrix is filled with cells,and each cell will have an initial value as follows:

A value greater than or equal to zero represents a path.
A value equal to 1 represents a passenger.
A value equal to -
'''
'''
# parametarised constructor
class profile:
    def __init__(self,id,name,age):
        print(id,name,age)

obj = profile(1, "adi",29)

# Eg:4
class c1:
   email = "adikeasv@gmail.com"
   
    def m1(self):
        name = "adi"
        place = "cbe"
        print(name,place)
        print(self.email)

object = c1()
object.m1()


# eg:6
# to use the variables inside the constructor in another methods
class class1:
    def __init__(self):
        self.name = "malli"
        self.email = "malli@gmail.com"
        # return name, email # error --> cannot use return with constructor

    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()


# * sinlge Inheritance
# ? it has only one parent class and only one child class
# | Eg:1
class parent:
    def m1(self):
        print("I am parent class")


class child(parent):
    def m2(self):
        print("I am child class")

obj = child()
obj.m1()

# Eg:2
class c1:
    def __init__(self):
        print("Iam constructor from parent class")

class child1(c1):
    pass

obj = child1()

# Eg:3
class parent:
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()
'''
#  Multilevel inheritance
# Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voice")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("Meow")


class parrot(cat):
    def parrot_voice(self):
        print("speak")


all = parrot()
all.dog_voice()
all.cat_voice()
all.parraot_voice()













