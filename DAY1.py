from abc import ABC, abstractmethod

# 1. ABSTRACTION: Define a blueprint (Abstract Base Class)
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

# 2. INHERITANCE: Car 'is-a' Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand          # Public Attribute
        self.model = model          # ✅ FIX: model initialized
        self._odometer = 0          # Protected Attribute (convention)
        self.__engine_code = "x1"   # Private Attribute (Encapsulation)

    # 3. POLYMORPISM: Specific implementation of move()
    def move(self):
        return f"The {self.brand} {self.model} drives on roads."

    # 4. ENCAPSULATION: Getter for private data
    def get_engine_status(self):
        return f"Engine Code: {self.__engine_code}"

class Boat(Vehicle):
    def move(self):
        return "The Boat sails on Water."

# Usage
my_car = Car("Tesla","Model 3")
print(my_car.move())            # Polymorphic behaviour
print(my_car.get_engine_status())   # Encapsulated access