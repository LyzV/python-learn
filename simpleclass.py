
class Person:
    quantity = 0

    def __init__(self, name):
        self.name = name
        Person.quantity += 1
        print('Hi, my name is {0}'.format(self.name))

    def __del__(self):
        self.name = ''
        print('By...')
        if Person.quantity > 0:
            Person.quantity -= 1

    @staticmethod
    def how_much():
        print('Our are {0}'.format(Person.quantity))


Person.how_much()
p = Person('Piter')
print(p)
Person.how_much()
del p
Person.how_much()


