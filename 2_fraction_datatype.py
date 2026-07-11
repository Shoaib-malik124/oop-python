from __future__ import annotations
class Fraction:
    def __init__(self,a:int=1,b:int=1):
        if(b==0):
            raise ValueError("Invalid Denominator")
        
        self.__numerator=a
        self.__denominator=b

        if((a<0 and b <0) or b<0):
            self.__denominator*=-1
            self.__numerator*=-1

    def get_numerator(self):
        return self.__numerator
    
    def get_denominator(self):
        return self.__denominator
    
    def set_numerator(self,newNumerator):
        if(type(newNumerator)==int):
            self.__pin=newNumerator
            print(f"Numerator updated to {newNumerator}")
        else:
            print(f"Invalid value for numerator")

    def set_denominator(self,newDenominator):
        if(type(newDenominator)==int and newDenominator>0):
            self.__amount=newDenominator
            print(f"Pin updated to {newDenominator}")
        else:
            print(f"Invalid amount")

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
        
    def __add__(self,other:Fraction):
        if(self.__denominator==other.__denominator):
            return Fraction(self.__numerator+other.__numerator,self.__denominator)
        else:
            return Fraction(self.__numerator*other.__denominator+self.__denominator*other.__numerator,self.__denominator*other.__denominator)
        

    def __sub__(self,other:Fraction):
        if(self.__denominator==other.__denominator):
            return Fraction(self.__numerator-other.__numerator,self.__denominator)
        else:
            return Fraction(self.__numerator*other.__denominator-self.__denominator*other.__numerator,self.__denominator*other.__denominator)

    def __mul__(self,other:Fraction):
        return Fraction(self.__numerator*other.__numerator,self.__denominator*other.__denominator)
    
    def __truediv__(self,other:Fraction):
        if(other.__denominator==0):
            raise ValueError(f"Invalid Denominator: {other.__denominator}")
        return Fraction(self.__numerator*other.__denominator,self.__denominator*other.__numerator)
    
    def print(self):
        print(f"{self.__numerator}/{self.__denominator}")

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