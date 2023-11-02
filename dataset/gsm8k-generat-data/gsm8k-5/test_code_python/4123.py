def solution():
    # Calculate the total area of the 20 units
    area_of_20_units = 20 * (8 * 4)

    # Calculate the area of the remaining units
    area_of_remaining_units = 5040 - area_of_20_units

    # Calculate the number of remaining units
    number_of_remaining_units = 42 - 20

    # Calculate the area of one remaining unit
    area_of_one_unit = area_of_remaining_units / number_of_remaining_units
    result = area_of_one_unit
    return result

print(solution())