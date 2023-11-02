def solution():
    
    width = 42
    area = 1638
    length = area / width
    desired_length = 390
    number_of_rectangles = desired_length / length
    result = round(number_of_rectangles)
    return result

print(solution())