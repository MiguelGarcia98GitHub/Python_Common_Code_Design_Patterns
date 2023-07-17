class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return f"Woof! Im a dog and my name is {self._name}"


class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return f"Meow! Im a cat and my name is {self._name}"


def create_pet(pet):
    pets = dict(dog=Dog("Goofy"), cat=Cat("Garfield"))
    return pets[pet]


dog1 = create_pet("dog")
print(dog1.speak())

cat1 = create_pet("cat")
print(cat1.speak())
