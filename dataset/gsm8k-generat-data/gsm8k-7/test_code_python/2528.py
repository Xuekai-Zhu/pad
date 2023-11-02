def solution():
    rectangle_length = 3
    rectangle_width = 6
    square_width = 5

    # Calculate the area of the rectangle
    rectangle_area = rectangle_length * rectangle_width

    # Calculate the area of the square
    square_area = square_width ** 2

    # Calculate the difference in area between the two shapes
    area_difference = rectangle_area - square_area
    result = area_difference
    return result

print(solution())