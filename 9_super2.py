class Phone:
    def __init__(self,price,brand,camera):
        self.__price=price
        self.brand=brand
        self.camera=camera

class SmartPhone(Phone):
    def __init__(self,price,brand,camera,color,ram,os):
        super().__init__(price,brand,camera)
        self.color=color
        self.ram=ram
        self.os=os


phone=SmartPhone(100000,'Samsung',14,'black','16GB','Android')
print(phone.brand)
print(phone.ram)
print(phone.os)