def solution():
    # Calculate the total area of the first twenty units
    area_first_twenty = 20 * (8 * 4)  # 20 units, each 8 ft by 4 ft

    # Calculate the total area of all 42 units
    total_area = 5040

    # Calculate the total area of the remaining units
    remaining_area = total_area - area_first_twenty

    # Calculate the area of each of the remaining units
    num_remaining_units = 42 - 20  # subtract the first 20 units
    area_each_remaining_unit = remaining_area / num_remaining_units

    result = area_each_remaining_unit
    return result

print(solution())