def solution():
    # Define given values
    tank_capacity = 200
    empty_tank_weight = 80
    fill_percentage = 0.8
    water_weight_per_gallon = 8

    # Calculate the weight of water in the tank
    filled_tank_capacity = fill_percentage * tank_capacity
    water_weight = filled_tank_capacity * water_weight_per_gallon

    # Calculate the total weight of the tank and water
    total_weight = empty_tank_weight + water_weight
    result = total_weight
    return result

print(solution())