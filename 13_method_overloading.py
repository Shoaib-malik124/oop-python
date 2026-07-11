class Geometry:
    def area(self,a,b=0):
        if(b==0):
            return f"Circle area: {3.14*a*a}"
        else:
            return f"Rectangle area: {a*b}"

obj=Geometry()
print(obj.area(5))
print(obj.area(5,4))