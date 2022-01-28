class car():
    print("The details  of the two cars:")  
    def __init__(self, cname, ccost, ccolour):
        self.cname = cname
        self.ccost = ccost
        self.ccolour=ccolour
        
    def print_cardetails(self):
        print("Car Name: ",self.cname)
        print("Car Cost: ",self.ccost)
        print("Car Colour: ",self.ccolour)
        
carobj1=car("Ferrai", "$70,000", "Red")
carobj2=car("JEEP", "$15,000","Blue")
carobj1.print_cardetails()  
carobj2.print_cardetails()
