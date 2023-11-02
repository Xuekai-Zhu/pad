def solution():
    # Calculate the amount of water left in the bottle
    initial_water = 4  # liters of water in the bottle
    first_drink = initial_water / 4  # amount of water consumed in the first drink
    remaining_water = initial_water - first_drink  # liters of water remaining after the first drink
    second_drink = (2/3) * remaining_water  # amount of water consumed in the second drink
    water_left = remaining_water - second_drink  # liters of water left in the bottle
    result = water_left
    return result

print(solution())