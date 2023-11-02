def solution():
    """Hunter needs to make a square patch of land whose perimeter is twice as large as a rectangular patch of land. If the rectangular patch of land has a length of 400 feet and a width of 300 feet, calculate the length of one side of the square patch of land."""
    # Calculate the perimeter of the rectangular patch of land
    rect_perimeter = 2 * (400 + 300)

    # Calculate the perimeter of the square patch of land
    square_perimeter = 2 * rect_perimeter

    # Calculate the length of one side of the square patch of land
    side_length = square_perimeter / 4

    # Display the length of one side of the square patch of land
    result = side_length
    return result

print(solution())