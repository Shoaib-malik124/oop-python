from __future__ import annotations
class Fraction:
    def __init__(self,a:int=1,b:int=1):
        if(b==0):
            raise ValueError("Invalid Denominator")
        
        self.numerator=a
        self.denominator=b

        if((a<0 and b <0) or b<0):
            self.denominator*=-1
            self.numerator*=-1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
        
    def __add__(self,other:Fraction):
        if(self.denominator==other.denominator):
            return Fraction(self.numerator+other.numerator,self.denominator)
        else:
            return Fraction(self.numerator*other.denominator+self.denominator*other.numerator,self.denominator*other.denominator)
        

    def __sub__(self,other:Fraction):
        if(self.denominator==other.denominator):
            return Fraction(self.numerator-other.numerator,self.denominator)
        else:
            return Fraction(self.numerator*other.denominator-self.denominator*other.numerator,self.denominator*other.denominator)

    def __mul__(self,other:Fraction):
        return Fraction(self.numerator*other.numerator,self.denominator*other.denominator)
    
    def __truediv__(self,other:Fraction):
        if(other.denominator==0):
            raise ValueError(f"Invalid Denominator: {other.denominator}")
        return Fraction(self.numerator*other.denominator,self.denominator*other.numerator)
    
    def print(self):
        print(f"{self.numerator}/{self.denominator}")

fraction_num1=Fraction(6,7)
fraction_num2=Fraction(9,8)

fraction_result1=fraction_num1+fraction_num2
fraction_result2=fraction_num1-fraction_num2
fraction_result3=fraction_num1*fraction_num2
fraction_result4=fraction_num1/fraction_num2
print(fraction_result1)
print(fraction_result2)
print(fraction_result3)
print(fraction_result4)