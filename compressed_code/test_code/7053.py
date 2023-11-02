def solution():
    
    initial_water = 4
    first_drink = initial_water / 4
    remaining_water = initial_water - first_drink
    second_drink = remaining_water * (2/3)
    water_left = remaining_water - second_drink
    result = water_left
    return result

print(solution())