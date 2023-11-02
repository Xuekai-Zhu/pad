def solution():
    """A rectangle has a length of 3 inches and a width of 6 inches. A square has a width of 5 inches. What is the difference in area between the two shapes?"""
    rectangle_length = 3
    rectangle_width = 6
    square_width = 5
    rectangle_area = rectangle_length * rectangle_width
    square_area = square_width ** 2
    difference = rectangle_area - square_area
    result = difference
    return result

print(solution())