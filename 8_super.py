class Phone:
    def __init__(self,price,brand,camera):
        self.__price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying Phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying smart phone")
        super().buy()

phone=SmartPhone(150000,'Vivo',13)
phone.buy()