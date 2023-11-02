def solution():
    # Calculate the amount of fuel used during the journey
    fuel_used = 47 - 14

    # Calculate the fuel consumption per km
    fuel_consumption_per_km = fuel_used / 275

    # Convert fuel consumption to per 100 km
    fuel_consumption_per_100km = fuel_consumption_per_km * 100

    result = fuel_consumption_per_100km
    return result

print(solution())