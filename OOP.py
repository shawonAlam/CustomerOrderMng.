class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

# c = Child()          # instance of child
# c.childMethod()      # child calls its method
# c.parentMethod()     # calls parent's method
# c.setAttr(200)       # again call parent's method
# c.getAttr()
# print(isinstance(c, Parent))
# print(issubclass(Parent, Child))


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __sub__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
# print(v1 - v2)


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
# counter.count()
# counter.count()
# print(counter._JustCounter__secretCount)


class Dog:
    def walk(self):
        print("*walking*")

    def speak(self):
        print("Woof!")


class JackRussellTerrier(Dog):
    def talk(self):
        return super().speak()


bobo = JackRussellTerrier()
# bobo.talk()



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
# print(isinstance(jack, Dachshund))

# from array import *
# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
#
# T.insert(2, [0,5,11,13,6])
#
# for r in T:
#     for c in r:
#         print(c, end=' ')
#     print()

# from numpy import *
# a = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
#            ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
#            ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
#            ['Sun', 13, 15, 19, 16]])
#
# m = reshape(a, (7, 5))
# print(m)


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
# print(Days)
# print(Months)
# print(Dates)


Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
# Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in Days:
    # print(d, end=' ')
    pass


# PUSH into a Stack
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
# print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
# print(AStack.peek())


# POP from a Stack
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()


AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
# print(AStack.remove())
# print(AStack.remove())
# print(AStack.remove())
# # print(AStack.remove())
# print(AStack.remove())

# Adding Elements to a Queue


class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          print(self.queue)
      return False

  def size(self):
      return len(self.queue)

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size())