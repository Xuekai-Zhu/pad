def solution():
    """ The building has 42 storage units that are a total of 5040 square feet. Twenty of the units are 8 by 4 feet each. If the remaining units are all the same size, what is the area, in square feet, for one of the remaining units? """
    # Calculate the total square footage of the 20 units
    square_footage_of_20_units = 20 * 8 * 4

    # Calculate the square footage of the remaining units
    remaining_square_footage = 5040 - square_footage_of_20_units

    # Calculate the area, in square feet, for one of the remaining units
    area_of_one_remaining_unit = remaining_square_footage / 22

    # Display the area of one of the remaining units
    result = area_of_one_remaining_unit
    return result

print(solution())