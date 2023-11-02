def solution():
    num_units_first_building = 4000
    num_units_second_building = (2/5) * num_units_first_building
    num_units_third_building = 1.2 * num_units_second_building

    # Calculate the total number of units across all three buildings
    total_units = num_units_first_building + num_units_second_building + num_units_third_building
    result = total_units
    return result

print(solution())