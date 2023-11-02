def solution():
    """If a rectangle has a width of 42 inches and an area of 1638, how many rectangles of the same size would reach a length of 390 inches?"""
    # Calculate the length of the rectangle with a width of 42 inches and an area of 1638 square inches
    length = 1638 / 42
    # Calculate the number of rectangles needed to reach a length of 390 inches
    num_rectangles = 390 / length
    result = num_rectangles
    return result

print(solution())