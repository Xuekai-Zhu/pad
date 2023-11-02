def solution():
    # Define the perimeter and the length-to-width ratio
    perimeter = 30
    length_to_width_ratio = 2

    # Use the perimeter formula to solve for the width
    width = perimeter / (2 + length_to_width_ratio)
    result = width
    return result

print(solution())