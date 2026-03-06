from abc import ABC, abstractmethod

# Abstract Base Class
class StationAsset(ABC):

    def __init__(self, name):
        self.name = name

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


# Main execution
if __name__ == "__main__":

    # Create assets
    asset1 = FuelDispenser("Pump 1", 500, 1.5)
    asset2 = FuelDispenser("Pump 2", 300, 1.5)
    asset3 = CarWash("Car Wash", 40, 10)

    # Store assets in a list
    station_assets = [asset1, asset2, asset3]

    total_revenue = 0

    # Loop through assets
    for asset in station_assets:
        revenue = asset.calculate_revenue()
        print(asset.name, "revenue:", revenue)
        total_revenue += revenue

    print("\nTotal Station Revenue:", total_revenue)