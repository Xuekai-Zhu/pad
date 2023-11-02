def solution():
    tank_capacity = 50  # in liters
    rain_collection = 0.8  # in liters per day
    river_collection = 1.7  # in liters per day

    # Calculate the amount of water needed to fill the tank
    water_needed = tank_capacity * 1000  # convert to milliliters

    # Calculate the total amount of water collected per day
    total_collection = rain_collection * 1000 + river_collection * 1000  # convert to milliliters

    # Calculate the number of days needed to fill the tank
    num_days = water_needed / total_collection
    result = num_days
    return result

print(solution())