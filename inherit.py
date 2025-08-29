class Animal:
    def __init__(self,name):
        self.name = name

    def type(self):
        return f"I am an animal and name is {self.name}"
    

class Dog(Animal):
    def __init__(self, name, breed):
        #super().__init__(name)
        self.breed = breed

    def type(self):
        return f"I am a {self.name} and breed is {self.breed}"
    
    def bark(self):
        return "Woof!"
    
#animal = Animal("monkey")
#print(animal.type())  # Output: I am an animal

dog = Dog("Dog","Golden Retriever")
print(dog.type())  # Output: I am a dog