"""Question 6: Vehicle base class with Car and Bike subclasses overriding a method."""


class Vehicle:
    """Base class holding what every vehicle has in common."""

    def __init__(self, make, model, wheels=4):
        self.make = make
        self.model = model
        self.wheels = wheels

    def describe(self):
        return f"{self.make} {self.model} with {self.wheels} wheel(s)"

    # This is the method the subclasses will override
    def start_engine(self):
        return "The vehicle starts."


class Car(Vehicle):
    def __init__(self, make, model, doors=4):
        super().__init__(make, model, wheels=4)  # reuse the base constructor
        self.doors = doors

    def start_engine(self):  # OVERRIDE
        return f"The {self.make} {self.model} starts with the push of a button. Vroom!"

    def describe(self):  # OVERRIDE that extends the base
        return super().describe() + f" and {self.doors} doors"


class Bike(Vehicle):
    def __init__(self, make, model, engine_cc=150):
        super().__init__(make, model, wheels=2)
        self.engine_cc = engine_cc

    def start_engine(self):  # OVERRIDE
        return f"The {self.make} {self.model} ({self.engine_cc}cc) kick-starts. Brrrm!"


if __name__ == "__main__":
    vehicles = [
        Vehicle("Generic", "Transport"),
        Car("Toyota", "Corolla", doors=4),
        Bike("Honda", "CG125", engine_cc=125),
    ]

    for vehicle in vehicles:
        print(vehicle.describe())
        print("  ", vehicle.start_engine())  # polymorphism in action
        print()

    car = vehicles[1]
    print("isinstance(car, Vehicle):", isinstance(car, Vehicle))
    print("Base version, called explicitly:", Vehicle.start_engine(car))
