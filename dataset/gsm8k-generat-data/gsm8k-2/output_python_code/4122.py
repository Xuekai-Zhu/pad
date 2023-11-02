def solution():
    """The building has 42 storage units that are a total of 5040 square feet. Twenty of the units are 8 by 4 feet each. If the remaining units are all the same size, what is the area, in square feet, for one of the remaining units?"""
    total_area = 5040
    known_area = 20 * (8*4)
    remaining_units = 42 - 20
    remaining_area = total_area - known_area
    area_per_unit = remaining_area / remaining_units
    result = area_per_unit
    return result

print(solution())