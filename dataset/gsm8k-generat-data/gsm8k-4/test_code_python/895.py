def solution():
    """Henrietta is repainting her house. The walls in the living room take up 600 square feet. She has three bedrooms. The walls in each bedroom take up 400 square feet. If one gallon of paint can cover 600 square feet, how many gallons of paint does Henrietta need to paint her house?"""
    # Calculate the total square footage of the walls in the bedrooms
    bedroom_square_footage = 3 * 400

    # Calculate the total square footage of the walls in the house
    house_square_footage = 600 + bedroom_square_footage

    # Calculate the number of gallons of paint needed, assuming each gallon covers 600 square feet
    gallons_of_paint = house_square_footage / 600

    result = gallons_of_paint
    return result

print(solution())