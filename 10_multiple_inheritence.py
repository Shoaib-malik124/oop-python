class Phone:
    def __init__(self,price,brand,camera):
        print('Inside Phone Constructor')
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print('Buying phone')

class Product:
    def __init__(self):
        print('Inside Product Constructor')
    def review(self):
        print("Customer review")
    def buy(self):
        print("Buying Product")

class SmartPhone(Phone,Product): # If there is no constructor inside SmartPhone, then Phone's constructor is called and 
    pass                         # if that is also absent, then Product's constructor is called.


s=SmartPhone(100000,'Apple',13)
s.buy() # Phone is first in the sequence of inheritence for SmartPhone, so buy() of Phone will be executed. This is called MRO(Method Resolution Order)
s.review()