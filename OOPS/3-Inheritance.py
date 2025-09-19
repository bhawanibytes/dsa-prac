class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    # When child class redefines the Parent class methods, they are overriden in child class
    def speak(self):
        print("Woof!")


dog = Dog()
dog.speak()
