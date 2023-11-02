def solution():
    """Nathan wants to line the inside of a box with velvet. The box has two long sides that measure 8 inches by 6 inches, two short sides that measure 5 inches by six inches and a top and a bottom that each measure 40 square inches. How many square inches of velvet does Nathan need?"""
    # Calculate the area of the two long sides
    long_sides_area = 2 * (8 * 6)

    # Calculate the area of the two short sides
    short_sides_area = 2 * (5 * 6)

    # Calculate the area of the top and bottom
    top_and_bottom_area = 2 * 40

    # Calculate the total area of the inside of the box
    total_area = long_sides_area + short_sides_area + top_and_bottom_area

    # Display the total area required for the velvet lining
    result = total_area
    return result

print(solution())