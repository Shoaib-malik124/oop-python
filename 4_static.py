class Car:
    __serial=0
    def __init__(self):
        Car.__serial+=1
        self.__number=Car.__serial
    
    @staticmethod
    def get_serial():
        return Car.__serial
    
    @staticmethod
    def set_serial(sr):
        if(type(sr)==int and sr>=0):
            Car.__serial=sr
        else:
            print("Invalid serail")
    
    def get_number(self):
        return self.__number
    
    def set_number(self,no):
        if(type(no)==int and no>=0):
            self.__number=no
        else:
            print("Invalid number")

car1=Car()
car2=Car()
car3=Car()

print(car1.get_number())
print(car2.get_number())
print(car3.get_number())

print(Car.get_serial())
Car.set_serial('abc')

# Car._Car__serial="abcd"