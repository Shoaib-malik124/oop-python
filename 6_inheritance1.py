class Product:
    def __init__(self,price,brand,ram,year=2026):
        print("Constructor of child not found, so by default i am called by python interpreter")
        self.year=year
        self.price=price
        self.brand=brand
        self.__ram=ram # I am private to Product, so SmartPhone won't be able to inherit me

    def get_ram(self): # I will get shadowed by child's get_ram,but if that is absent, i child's object can get this private
        return self.__ram # field of Product although it hasn't inherited it.

class SmartPhone(Product):
    def get_ram(self): # Method overriding. Analogy=I could grow Apples like my father, but i Chose Engineering as "profession".
        return self.__ram 

phone=SmartPhone(100000,"Oppo","16GB",2025)
print(phone.year)
print(phone.get_ram()) # AttributeError: 'SmartPhone' object has no attribute '_SmartPhone__ram'