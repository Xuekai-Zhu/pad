def solution():
    # Calculate the area of the two long sides
    long_side_area = 2 * (8 * 6)

    # Calculate the area of the two short sides
    short_side_area = 2 * (5 * 6)

    # Calculate the area of the top and bottom
    top_bottom_area = 2 * 40

    # Calculate the total area to be covered in velvet
    total_area = long_side_area + short_side_area + top_bottom_area

    result = total_area
    return result

print(solution())