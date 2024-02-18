class Student:
    print("Hello")
    def __init__(self, name=None):
        self.height = 167
        self.name = name
        print("I'm alive")

    def grow(self):
        self.height += 12

    def __del__(self):
        print("That's over")

    def __bool__(self):
        return self.name != None

    def __len__(self):
        return self.height


Vasia = Student()
Anton = Student()

Vasia.grow()
Anton.grow()
print(Vasia.__len__())
print(Vasia.__bool__())
print(len(Vasia))
print(bool(Vasia))

print(Vasia.height)
print(Anton.height)


