class Parent:
    def __init__(self,num):
        self.__num=num
    
    def get_num(self):
        return self.__num
    
class Child(Parent):
    def __init__(self,val,num):
        self.__val=val

    def get_val(self):
        return self.__val
    
child=Child(100,10)
print(child.get_val())
print(child.get_num()) # AttributeError: 'Child' object has no attribute '_Parent__num'
