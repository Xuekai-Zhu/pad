def solution():
    # Calculate the total square footage of the walls in the bedrooms
    bedroom_square_footage = 3 * 400

    # Calculate the total square footage of all the walls
    total_square_footage = 600 + bedroom_square_footage

    # Calculate the number of gallons of paint needed to cover all the walls
    gallons_of_paint = total_square_footage / 600

    result = gallons_of_paint
    return result

print(solution())