def solution():
    # Convert 50 liters to milliliters
    tank_capacity = 50 * 1000

    # Calculate the daily water collection
    daily_collection = 800 + 1700

    # Calculate the number of days needed to fill the tank
    num_days = tank_capacity / daily_collection
    result = num_days
    return result

print(solution())