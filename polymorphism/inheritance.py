from typing import Any

#Base class
class Animal:
    a_classvar = "ANIMAL!"

    def __init__(self, name):
        self.name = name

    def speak(self) -> str:
        return "I don't know what to say"

    def what_am_i(self) -> str:
        return "I am a " + str(type(self))
    
    def __str__(self):
        return f"Animal named '{self.name}', {self.what_am_i()} and {self.speak()}. My self.classvar is: '{self.a_classvar}' and my class.classvar is '{Animal.a_classvar}'"

    #Factory method
    @classmethod
    def create_me(cls, name: str):
        return cls(name)
    
a: Animal = Animal.create_me("Generic Animal")
print(a)
#Animal named 'Generic Animal', I am a <class '__main__.Animal'> and I don't know what to say. My self.classvar is: 'ANIMAL!' and my class.classvar is 'ANIMAL!'

class Dog(Animal):
    #Super constructor is automatically inherited

    #Override
    def speak(self) -> str:
        return "Woof!"
    
dog: Dog = Dog.create_me("Fido")
print(dog)
#Animal named 'Fido', I am a <class '__main__.Dog'> and Woof!. My self.classvar is: 'ANIMAL!' and my class.classvar is 'ANIMAL!'

class Cat(Animal):
    #Unique cat instance attribute
    color: str

    def __init__(self, name: str, color: str):
        #Need to call super constructor manually
        super().__init__(name)
        self.color = color

    #Override
    def __str__(self):
        return super().__str__() + f". My color is {self.color}!"

    #Alternative factories
    #Need to utilize cat-specific 2 arg constructor
    @classmethod
    def create_me(cls, name: str):
        return cls(name, "unknown")
    
    @classmethod
    def create_me_w_color(cls, name: str, color: str):
        return cls(name, color)
    
cat: Cat = Cat.create_me_w_color("Whiskers", "white")
print(cat)
#Animal named 'Whiskers', I am a <class '__main__.Cat'> and I don't know what to say. My self.classvar is: 'ANIMAL!' and my class.classvar is 'ANIMAL!'. My color is white!

cat = Cat.create_me("Shadow")
print(cat)
#Animal named 'Shadow', I am a <class '__main__.Cat'> and I don't know what to say. My self.classvar is: 'ANIMAL!' and my class.classvar is 'ANIMAL!'. My color is unknown!

try:
    color = dog.color
except AttributeError as e:
    print(e)
#'Dog' object has no attribute 'color'
    
class Fish(Animal):
    #Our own constructor to shadow class variable
    def __init__(self, name: str):
        super().__init__(name)
        #Shadowing class variable name for this instance
        self.a_classvar = "FEEEESH!"

    #Override
    def speak(self) -> str:
        return "*silence*"
    
    #Fish is cool, fish allows bracket notation to access attributes
    def __getitem__(self, arg: str) -> Any:
        return getattr(self, arg, "Nope!")

fish: Fish = Fish.create_me("Nemo")
print(fish)
#Animal named 'Nemo', I am a <class '__main__.Fish'> and *silence*. My self.classvar is: 'FEEEESH!' and my class.classvar is 'ANIMAL!'

print("Fish is special! Bracket notation returned", fish["name"])
#Fish is special! Bracket notation returned Nemo

print(fish["kobold"])
# Nope!

try:
    print(dog["name"]) #Dog does not support bracket notation
except Exception as e:
    print(e)
#'Dog' object is not subscriptable