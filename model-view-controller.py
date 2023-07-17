# Model
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# View
class PersonView:
    def display_person(self, person):
        print(f"The person {person.name} is {person.age} years old")


# Controller
class PersonController:
    def __init__(self, person, view):
        self.person = person
        self.view = view

    def update_view(self):
        self.view.display_person(self.person)


# Example
person1 = Person("Jimmy", 25)
person2 = Person("James", 40)
# view1 = PersonView()
controller = PersonController(person1, PersonView())
controller.update_view()
controller = PersonController(person2, PersonView())
controller.update_view()
