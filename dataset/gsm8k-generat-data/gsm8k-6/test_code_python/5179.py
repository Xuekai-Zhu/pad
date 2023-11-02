def solution():
    # Calculate the weight of the water in the tank
    tank_capacity = 200  # gallons
    empty_weight = 80  # pounds
    filled_percent = 0.8  # 80% of capacity
    water_weight_per_gallon = 8 # pounds
    filled_gallons = tank_capacity * filled_percent
    filled_weight = filled_gallons * water_weight_per_gallon
    total_weight = empty_weight + filled_weight
    result = total_weight
    return result

print(solution())