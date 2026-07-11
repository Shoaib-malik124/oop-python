class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def edit_profile(self,newName,newCity,newPin,newState):
        self.name=newName
        self.address.change_address(newCity,newPin,newState)

class Address:
    def __init__(self,city,pin,state):
        self.city=city
        self.pin=pin
        self.state=state

    def change_address(self,newCity,newPin,newState):
        self.city=newCity
        self.pin=newPin
        self.state=newState

address=Address("Shopian",192303,"J&K")
customer=Customer("Shoaib","Male",address)

print(customer.address.city)

customer.edit_profile("Shoaib","Srinagar",190001,"J&K")
print(customer.address.city)