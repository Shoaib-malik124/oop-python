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
        
    def add(self,other:Fraction):
        if(self.denominator==other.denominator):
            return Fraction(self.numerator+other.numerator,self.denominator)
        else:
            return Fraction(self.numerator*other.denominator+self.denominator*other.numerator,self.denominator*other.denominator)
        

    def sub(self,other:Fraction):
        if(self.denominator==other.denominator):
            return Fraction(self.numerator-other.numerator,self.denominator)
        else:
            return Fraction(self.numerator*other.denominator-self.denominator*other.numerator,self.denominator*other.denominator)

    def multiply(self,other:Fraction):
        return Fraction(self.numerator*other.numerator,self.denominator*other.denominator)
    
    def divide(self,other:Fraction):
        if(other.denominator==0):
            raise ValueError(f"Invalid Denominator: {other.denominator}")
        return Fraction(self.numerator*other.denominator,self.denominator*other.numerator)
    
    def print(self):
        print(f"{self.numerator}/{self.denominator}")

fraction_num1=Fraction(6,7)
fraction_num2=Fraction(9,8)

fraction_result=fraction_num1.add(fraction_num2)
print(fraction_result.numerator)
print(fraction_result.denominator)