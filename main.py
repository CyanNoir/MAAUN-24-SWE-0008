from cyannoir import FuelDispenser, CarWash

# Create assets
asset1 = FuelDispenser("Pump 1", 500, 1.5)
asset2 = FuelDispenser("Pump 2", 300, 1.5)
asset3 = CarWash("Main Car Wash", 40, 10)

# Store assets in a list
station_assets = [asset1, asset2, asset3]

total_revenue = 0

# Loop through assets and calculate revenue
for asset in station_assets:
    revenue = asset.calculate_revenue()
    print(asset.name, "revenue:", revenue)
    total_revenue += revenue

print("\nTotal Station Revenue:", total_revenue)