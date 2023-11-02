def solution():
    """If a rectangle has a width of 42 inches and an area of 1638, how many rectangles of the same size would reach a length of 390 inches?"""
    width = 42
    area = 1638
    length = area / width
    desired_length = 390
    number_of_rectangles = desired_length / length
    result = round(number_of_rectangles)
    return result

print(solution())