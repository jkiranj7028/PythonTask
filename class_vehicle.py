#OOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes
"""
class vehicle:
    def __init__(self, low, medium, high):
        self.low = low
        self.medium = medium
        self.high = high
        print("Vehicle Mileage instance")
        
veh_mil1=vehicle(30)
veh_mil2=vehicle(50)
veh_mil3=vehicle(90)
print(veh_mil1.low,veh_mil2.medium,veh_mil3.high)
"""
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        print("vehicle mileage details:")
modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)