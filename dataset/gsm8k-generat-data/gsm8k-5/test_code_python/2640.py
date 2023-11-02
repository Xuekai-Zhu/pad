def solution():
    # Calculate the length of the rectangle using the given width and area
    width = 42
    area = 1638
    length = area / width

    # Calculate how many rectangles of the same size would reach a length of 390 inches
    target_length = 390
    num_rectangles = target_length / length
    result = num_rectangles
    return result

print(solution())