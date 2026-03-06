from abc import ABC, abstractmethod

# Abstract Base Class
class StationAsset(ABC):

    def __init__(self, name):
        self.name = name

    # Abstract method (must be implemented by child classes)
    @abstractmethod
    def calculate_revenue(self):
        pass


# FuelDispenser class
class FuelDispenser(StationAsset):

    def __init__(self, name, liters_sold, price_per_liter):
        super().__init__(name)
        self.liters_sold = liters_sold
        self.price_per_liter = price_per_liter

    def calculate_revenue(self):
        return self.liters_sold * self.price_per_liter


# CarWash class
class CarWash(StationAsset):

    def __init__(self, name, cars_washed, price_per_car):
        super().__init__(name)
        self.cars_washed = cars_washed
        self.price_per_car = price_per_car

    def calculate_revenue(self):
        return self.cars_washed * self.price_per_car