def solution():
    water_bottle_size = 4
    first_drink = water_bottle_size / 4  # Consumes a quarter of the water
    remaining_water = water_bottle_size - first_drink
    second_drink = remaining_water * (2/3)  # Consumes 2/3 of the remaining water
    water_left = remaining_water - second_drink
    result = water_left
    return result

print(solution())