def solution():
    """Hunter needs to make a square patch of land whose perimeter is twice as large as a rectangular patch of land. If the rectangular patch of land has a length of 400 feet and a width of 300 feet, calculate the length of one side of the square patch of land."""
    # Define the dimensions of the rectangular patch
    length_rect = 400
    width_rect = 300

    # Calculate the perimeter of the rectangular patch
    perimeter_rect = 2 * (length_rect + width_rect)

    # Calculate the perimeter of the square patch
    perimeter_square = 2 * perimeter_rect

    # Calculate the length of one side of the square patch
    side_length = perimeter_square / 4

    result = side_length
    return result

print(solution())