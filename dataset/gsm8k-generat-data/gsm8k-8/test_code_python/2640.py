def solution():
    # Calculate the length of the rectangle using the area and width
    area = 1638
    width = 42
    length = area / width

    # Calculate the number of rectangles needed to reach a length of 390 inches
    total_length = 390
    num_rectangles = total_length / length
    result = num_rectangles
    return result

print(solution())