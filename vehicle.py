class Vehicle:
    def __init__(self, make, model, year, mileage, condition):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.condition = condition
    
    def start(self):
        print(f"{self.model} has engine on.")
    
    def stop(self):
        print(f"{self.model} has engine off.")
    
    def drive(self, distance):
        self.mileage += distance
        print(f"{self.model} has {self.mileage} miles on it.")
    
class Car(Vehicle):
    def __init__(self, make, model, year, mileage, condition, num_doors, num_wheels, fuel_type):
        super().__init__(make, model, year, mileage, condition)
        self.num_doors = num_doors
        self.num_wheels = num_wheels
        self.fuel_type = fuel_type
    
    def accelerate(self):
        print(f"{self.model} is accelerating.")
    
    def brake(self):
        print(f"{self.model} is braking.")

class ElectricCar(Car):
    def __init__(self, make, model, year, mileage, condition, num_doors, num_wheels, fuel_type, battery_size, range):
        super().__init__(make, model, year, mileage, condition, num_doors, num_wheels, fuel_type)
        self.battery_size = battery_size
        self.range = range
    
    def charg(self):
        print(f"{self.model} is charging.")
    
    def estimate_range(self):
        print(f"{self.model} has {self.range} miles of range")


electricCar = ElectricCar("Tesla", "Model S", "2022", 120000, "Used", 4, 4, "Electric", "Large", 320)
electricCar.accelerate()
electricCar.drive(100)
electricCar.estimate_range()