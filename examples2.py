class A:
    def m1(self):
        return 20

class B(A):
    def m1(self): # type:ignore
        return super().m1()+30
    
class C(B):
    def m1(self):
        return self.m1()+20
    
obj=C()
print(obj.m1())