def solution():
    # Calculate the perimeter of the rectangle
    rect_perimeter = 2 * (400 + 300)

    # Calculate the perimeter of the square
    sq_perimeter = 2 * rect_perimeter

    # Calculate the length of one side of the square
    sq_side_length = sq_perimeter / 4

    result = sq_side_length
    return result

print(solution())