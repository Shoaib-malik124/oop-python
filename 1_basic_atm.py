class Atm:
    def __init__(self):
        self.__pin:str=""
        self.__amount:int=0
        
        while(True):
            self.__menu()

    def get_pin(self):
        return self.__pin
    
    def get_amount(self):
        return self.__amount
    
    def set_pin(self,newPin):
        if(type(newPin)==str and (len(newPin)>=6 and len(newPin)<=12)):
            self.__pin=newPin
            print(f"Pin updated to {newPin}")
        else:
            print(f"Invalid pin")

    def set_amount(self,newAmount):
        if(type(newAmount)==int):
            self.__amount=newAmount
            print(f"Pin updated to {newAmount}")
        else:
            print(f"Invalid amount")
    
    def __menu(self):
        print("""
            Hello, how will you like to proceed:
            (a)Enter 1 for changing your pin
            (b)Enter 2 for checking your balance
            (c)Enter 3 for withdraw
            (d)Enter 4 for deposit
            (e)Enter 5 for creating your pin
            (f)Enter 6 for exit
            """)
        try:
           userInput=int(input('Enter your request: '))
           match userInput:
            case 1:
                self.change_pin()
            case 2:
                self.check_balance()
            case 3:
                self.withdraw()
            case 4:
                self.deposit()
            case 5:
                self.create_pin()
            case 6:
                print("Thank you for using our ATM.")
                raise SystemExit
            case _:
                print('Invalid request,exiting...')
                raise SystemExit
        except ValueError:
            print("Invalid request")
            raise SystemExit
                

    def change_pin(self):
        if(self.__pin==""):
            self.create_pin()
        else:
            oldPin=input("Enter old pin: ")
            if(oldPin==self.__pin):
                newPin=input("Enter new pin: ")
                self.__pin=newPin
                print(f'Your pin updated to {newPin}')
            else:
                print("Incorrect pin")

    def check_balance(self):
        if(self.__pin==""):
            print("You have not configured your pin")
        else:
            pin=input("Enter your pin: ")
            if(pin==self.__pin):
                print(f'Your account balance is: {self.__amount}$')
            else:
                print("Incorrect pin")
    
    def withdraw(self):
        if(self.__pin==""):
            print("You have not configured your pin")
        else:
            pin=input("Enter your pin: ")
            if(self.__pin==pin):
                amount=input("Enter amount: ")
                try:
                    amount=int(amount)
                    if(amount>0):
                        if(self.__amount>=amount):
                            self.__amount-=amount
                            print(f'{amount}$ withdrawal successful')
                        else:
                            print('Insufficient balance')
                    else:
                        print('Invalid input')
                except ValueError:
                    print('Invalid input')
            else:
                print('Incorrct pin')

    def deposit(self):
        if(self.__pin==""):
            print("You have not configured your pin")
        else:
            pin=input("Enter your pin: ")
            if(self.__pin==pin):
                amount=input("Enter your amount: ")
                try:
                    amount=int(amount)
                    if(amount>0):
                        self.__amount+=amount
                        print(f'{amount}$ deposited successful')
                    else:
                        print("Invalid input")
                except ValueError:
                    print("Invalid input")
            else:
                print('Wrong pin')

    def create_pin(self):
        pin=input("Enter pin: ")
        self.__pin=pin
        print(f'Your pin is set to {pin}')

sbi=Atm()