def changeList(l):
    print(id(l))
    l.append(55)
    print(l)
    print(id(l))

def changeTuple(l):
    print(id(l))
    l+=(4,5)
    print(l)
    print(id(l))

l=[1,2,3,4]
print(id(l))
print(l)
changeList(l[:])
print(l)

print()

t=(1,2,3)
print(id(t))
print(t)
changeTuple(t)
print(t)


class Car:
    def __init__(self):
        self.name="BMW"
        self.seats=4


def change_car(car:Car):
    print(id(car))
    car.name="BMV"
    print(id(car))

car=Car()
print(car.name)
print(id(car))
change_car(car)
print(car.name)
