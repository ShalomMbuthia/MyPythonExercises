class Animal:  #Parent class
    def speak(self):
        print("Animal is speaking")

class Dog(Animal): #meaning dog extends animal class
    def bark(self):
     print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meawing")

d = Dog()  #creating an object for my child class
d.speak()   #calling the function
d.bark()

c = Cat()
c.meow()
c.speak()



