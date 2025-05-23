class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, age, color, is_indoor):
        super().__init__(name, age, color)
        self.is_indoor = is_indoor

dog = Dog("Rex", 5, "Brown", "Labrador")
cat = Cat("Luna", 3, "Black", "is_indoor")

print(dog.name, dog.age, dog.color, dog.breed)
print(cat.name, cat.age, cat.color, cat.is_indoor)
