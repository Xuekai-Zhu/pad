def solution():
    """Hunter needs to make a square patch of land whose perimeter is twice as large as a rectangular patch of land.
    If the rectangular patch of land has a length of 400 feet and a width of 300 feet, calculate the length of one side of the square patch of land."""
    rectangular_perimeter = 2 * (400 + 300)
    square_perimeter = 2 * rectangular_perimeter
    # The perimeter of a square is 4 times the length of one of its sides
    square_side_length = square_perimeter / 4
    result = square_side_length
    return result

print(solution())