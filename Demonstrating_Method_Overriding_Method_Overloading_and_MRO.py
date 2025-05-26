class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        return f"{self.brand} {self.model} engine starting..."
    
    def get_fuel_type(self):
        return "Generic fuel type"

class Car(Vehicle):
    def start_engine(self):
        return f"{self.brand} {self.model} car engine starting with a smooth purr"
    
    def get_fuel_type(self):
        return "Petrol or Diesel"
    
    def drive(self):
        return f"{self.brand} {self.model} is driving on the road"

class ElectricCar(Car):
    def start_engine(self):
        return f"{self.brand} {self.model} electric motor silently activating"
    
    def get_fuel_type(self):
        return "Electricity"
    
    def charge(self):
        return f"{self.brand} {self.model} is charging at the station"

class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return sum(args)
    
    def multiply(self, *args):
        if len(args) == 2:
            return args[0] * args[1]
        elif len(args) == 3:
            return args[0] * args[1] * args[2]
        else:
            result = 1
            for num in args:
                result *= num
            return result

def main():
    print("Example 1: Method Overriding and MRO with Vehicles")
    print("-" * 60)
    
    vehicle = Vehicle("Generic", "Vehicle")
    car = Car("Toyota", "Camry")
    electric_car = ElectricCar("Tesla", "Model 3")
    
    print(f"Vehicle engine: {vehicle.start_engine()}")
    print(f"Car engine: {car.start_engine()}")
    print(f"Electric car engine: {electric_car.start_engine()}")
    
    print(f"\nVehicle fuel: {vehicle.get_fuel_type()}")
    print(f"Car fuel: {car.get_fuel_type()}")
    print(f"Electric car fuel: {electric_car.get_fuel_type()}")
    
    print("\nMRO for ElectricCar:")
    print(ElectricCar.__mro__)
    
    print("\nExample 2: Method Overloading")
    print("-" * 50)
    
    calc = Calculator()
    print(f"Adding two numbers: {calc.add(5, 3)}")
    print(f"Adding three numbers: {calc.add(5, 3, 2)}")
    print(f"Multiplying two numbers: {calc.multiply(5, 3)}")
    print(f"Multiplying three numbers: {calc.multiply(5, 3, 2)}")

if __name__ == "__main__":
    main() 