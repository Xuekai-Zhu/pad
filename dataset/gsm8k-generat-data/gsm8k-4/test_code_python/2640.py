def solution():
    """If a rectangle has a width of 42 inches and an area of 1638, how many rectangles of the same size would reach a length of 390 inches?"""
    # Define the width and area of the rectangle
    width = 42
    area = 1638

    # Calculate the length of the rectangle
    length = area / width

    # Calculate the number of rectangles needed to reach a length of 390 inches
    num_rectangles = 390 / length

    # Round up to the nearest whole number
    num_rectangles = int(num_rectangles + 0.5)

    # return the result
    result = num_rectangles
    return result

print(solution())