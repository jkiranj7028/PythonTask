class vehicle(car):
    colour=""
    value=100.00
    def __init__(self, name,colour,kind,value):
        self.name = name
        self.colour = colour
        self.kind = kind
        self.value = value
    def car_desc(self):
        desc_str="%s is a %s %s worth $%.2f." %(self.name,self.colour,self.kind, self.value)
        return desc_str
car1=vehicle("Ferrai", "Red")
car2=vehicle("Ferrai", "Red")
#car1.car_desc()
#car2.car_desc()
print(car1.car_desc())
print(car2.car_desc())