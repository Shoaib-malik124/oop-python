class Atm:
    def __init__(self):
        self.pin:str=""
        self.amount:int=0
        
        while(True):
            self.menu()
    
    def menu(self):
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
        if(self.pin==""):
            self.create_pin()
        else:
            oldPin=input("Enter old pin: ")
            if(oldPin==self.pin):
                newPin=input("Enter new pin: ")
                self.pin=newPin
                print(f'Your pin updated to {newPin}')
            else:
                print("Incorrect pin")

    def check_balance(self):
        if(self.pin==""):
            print("You have not configured your pin")
        else:
            pin=input("Enter your pin: ")
            if(pin==self.pin):
                print(f'Your account balance is: {self.amount}$')
            else:
                print("Incorrect pin")
    
    def withdraw(self):
        if(self.pin==""):
            print("You have not configured your pin")
        else:
            pin=input("Enter your pin: ")
            if(self.pin==pin):
                amount=input("Enter amount: ")
                try:
                    amount=int(amount)
                    if(amount>0):
                        if(self.amount>=amount):
                            self.amount-=amount
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
        if(self.pin==""):
            print("You have not configured your pin")
        else:
            pin=input("Enter your pin: ")
            if(self.pin==pin):
                amount=input("Enter your amount: ")
                try:
                    amount=int(amount)
                    if(amount>0):
                        self.amount+=amount
                        print(f'{amount}$ deposited successful')
                    else:
                        print("Invalid input")
                except ValueError:
                    print("Invalid input")
            else:
                print('Wrong pin')

    def create_pin(self):
        pin=input("Enter pin: ")
        self.pin=pin
        print(f'Your pin is set to {pin}')

sbi=Atm()