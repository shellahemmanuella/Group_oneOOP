#creating a class with instance attributes
class Vehicle():
    def __init__(self,max_speed,mileage): #instance attributes
        self.max_speed=max_speed
        self.mileage=mileage
land_rover=Vehicle(270,19) #created an instance
print(land_rover.max_speed,land_rover.mileage)

#creating class without variables
class Animals():
    pass


#2

#creating an object that inherits attributes from the mentioned class
class Vehicle():
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehicle): #class inheriting from the parent class vehicle
    pass

bus_kate=Bus("Volvo",180,12)
print("Vehicle Name:", bus_kate.name,"Speed: ",bus_kate.max_speed, "Mileage:", bus_kate.mileage)


#3
#creating a base class
class Vehicle():
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    
    def seating_capacity(self, capacity):
           return super().seating_capacity(capacity=50) #from the super() ojects are able to attain properties and methods of the parent class
#creating a class that inherits from the base class
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        
        return f"The seating capacity of a {bus_kate.name} is {capacity} passengers" #using the f string to attain expressions in the braces
    def output(self,condition="weak"):
        return f"the vehicles {bus_kate.name} is very {condition} please"    
bus_kate=Bus("Volvo",180,12)
print(bus_kate.seating_capacity())
print(bus_kate.output())

#4
#assaigning a class default attribute
color="White"
class Vehicle():
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehicle):#sub classes that inherit from class Vehicle
    pass
class Car(Vehicle):#sub classes that inherit from class Vehicle
    pass
bus_kate=Bus("Volvo",180,12)
print("Color:",color,"Vehicle Name:", bus_kate.name,"Speed: ",bus_kate.max_speed, "Mileage:", bus_kate.mileage)
prado=Car("Prado",567,34)
print("Color:",color,"Vehicle Name:", prado.name,"Speed: ",prado.max_speed, "Mileage:", prado.mileage)


#5
class Vehicle():
    def __init__(self,name,max_speed,mileage,capacity):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity
    def fare(self):
        return self.capacity*100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

bus_kate= Bus("School Volvo", 12, 50,50)
print("Total Bus fare is:", bus_kate.fare())
