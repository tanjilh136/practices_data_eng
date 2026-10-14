from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(f"{self.name} is walking.")
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def wagging_tail(self):
        print(f"{self.name} is wagging its tail.")
    def bark(self):
        print(f"{self.name} is barking.")

class talk(ABC):
    @abstractmethod
    def talk(self):
        pass

class talking_dog(Dog,talk):
    def __init__(self, name):
        super().__init__(name)
    def talk(self):
        print(f"{self.name} is talking.")

scooby = talking_dog("Scooby")
scooby.walk()
scooby.eat()
scooby.sleep()
scooby.wagging_tail()
scooby.bark()
scooby.talk()