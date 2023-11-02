def solution():
    # Find the length of the rectangle
    area = 1638
    width = 42
    length = area / width

    # Find the number of rectangles needed to reach a length of 390 inches
    target_length = 390
    num_rectangles = target_length / length
    result = num_rectangles
    return result

print(solution())