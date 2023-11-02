def solution():
    tank_capacity = 200  # gallons
    empty_weight = 80  # pounds
    fill_percentage = 0.8
    water_weight_per_gallon = 8  # pounds

    # Calculate the volume of water in the tank
    water_volume = tank_capacity * fill_percentage

    # Calculate the weight of the water in the tank
    water_weight = water_volume * water_weight_per_gallon

    # Calculate the total weight of the tank with water
    total_weight = empty_weight + water_weight
    result = total_weight
    return result

print(solution())