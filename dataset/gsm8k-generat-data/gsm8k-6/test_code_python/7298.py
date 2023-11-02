def solution():
    # Calculate the amount of fuel used for the journey
    fuel_used = 47 - 14  # liters of fuel used in the journey

    # Calculate the fuel consumption per 100 km
    fuel_consumption = fuel_used / 275 * 100

    result = fuel_consumption
    return result

print(solution())