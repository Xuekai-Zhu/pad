def solution():
    
    first_building_units = 4000
    second_building_units = (2/5) * first_building_units
    third_building_units = 1.2 * second_building_units
    total_units = first_building_units + second_building_units + third_building_units
    result = total_units
    return result

print(solution())