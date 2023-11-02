def solution():
    total_water = 65
    water_for_cars = 2 * 7
    water_for_plants = water_for_cars - 11
    remaining_water = total_water - water_for_cars - water_for_plants
    water_for_cleaning = remaining_water / 2
    result = water_for_cleaning
    return result

print(solution())