def solution():
    # Calculate the perimeter of the rectangular patch of land
    rect_perimeter = 2 * (400 + 300)

    # Calculate the perimeter of the square patch of land
    square_perimeter = 2 * rect_perimeter

    # Calculate the length of one side of the square patch of land
    side_length = square_perimeter / 4
    result = side_length
    return result

print(solution())