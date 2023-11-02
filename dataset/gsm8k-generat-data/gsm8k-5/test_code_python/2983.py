def solution():
    tank_capacity = 50  # Jacob's water tank can hold up to 50 liters of water
    daily_collection = 0.8 + 1.7  # Jacob can collect 800 mL from rain and 1700 mL from river every day
    days_to_fill = tank_capacity / daily_collection
    result = days_to_fill
    return result

print(solution())