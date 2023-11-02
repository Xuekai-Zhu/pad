def solution():
    # Calculate the total area of the two long sides
    long_side_area = 2 * (8 * 6)

    # Calculate the total area of the two short sides
    short_side_area = 2 * (5 * 6)

    # Calculate the total area of the box (excluding the top and bottom)
    box_area = long_side_area + short_side_area

    # Calculate the total area of the top and bottom
    top_bottom_area = 2 * 40

    # Calculate the total area of velvet needed
    velvet_area = box_area + top_bottom_area

    result = velvet_area
    return result

print(solution())