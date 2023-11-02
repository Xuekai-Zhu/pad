def solution():
    """If a rectangle has a width of 42 inches and an area of 1638, how many rectangles of the same size would reach a length of 390 inches?"""
    width = 42
    area = 1638
    length = area / width
    num_rectangles = 390 / length
    result = num_rectangles
    return result

print(solution())