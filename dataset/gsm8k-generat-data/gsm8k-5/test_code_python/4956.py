def solution():
    # Calculate the area of the long sides
    long_sides_area = 2 * (8 * 6)

    # Calculate the area of the short sides
    short_sides_area = 2 * (5 * 6)

    # Calculate the area of the top and bottom
    top_bottom_area = 2 * 40

    # Calculate the total area to be covered with velvet
    total_area = long_sides_area + short_sides_area + top_bottom_area

    result = total_area
    return result

print(solution())