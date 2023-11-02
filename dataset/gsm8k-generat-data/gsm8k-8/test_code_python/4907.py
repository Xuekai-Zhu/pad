def solution():
    # Calculate the number of units in the second building
    second_building_units = 2/5 * 4000

    # Calculate the number of units in the third building
    third_building_units = 1.2 * second_building_units

    # Calculate the total number of units
    total_units = 4000 + second_building_units + third_building_units

    result = total_units
    return result

print(solution())