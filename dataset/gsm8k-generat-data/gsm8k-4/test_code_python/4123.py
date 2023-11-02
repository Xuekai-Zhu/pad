def solution():
    """The building has 42 storage units that are a total of 5040 square feet. Twenty of the units are 8 by 4 feet each. If the remaining units are all the same size, what is the area, in square feet, for one of the remaining units?"""
    # Define the total area and the area of the known units
    total_area = 5040
    known_units_area = 20 * 8 * 4

    # Calculate the area of the remaining units
    remaining_units_area = total_area - known_units_area

    # Calculate the area of one remaining unit
    one_remaining_unit_area = remaining_units_area / 22

    result = one_remaining_unit_area
    return result

print(solution())