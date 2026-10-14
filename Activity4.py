class Vehicle:
    # Encapsulation
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    # Abstraction
    def start(self):
        print("Vehicle is starting.")


# Inheritance
class Car(Vehicle):

    # Polymorphism
    def start(self):
        print("Car engine is starting.")


# Create objects
vehicle = Vehicle("Toyota", 100)
car = Car("Honda", 120)

# Call start methods
vehicle.start()
car.start()