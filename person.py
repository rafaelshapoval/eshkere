class Person:
    def __init__(self.name):
        self.__name = name
     @property
    def name(self):
        return self.__name
    def do_nothing(self):
        print(f'{self.__name} does nothing')
        class Student(Person)
     def study(self):
        print(f'{self.name} studieng')
    def act(person):
     if isinstance(person,Student):
        person.stady()
    elif isinstance(person,Employee):
         person.work()
    elif isinstance(person,Person):
        person.do_nothing
user1 = Employee("user1")
user2 = Student("user2")
user3 = Person("user3")

act(user1)
act(user2)
act(user3)