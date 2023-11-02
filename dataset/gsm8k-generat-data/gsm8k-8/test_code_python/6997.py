def solution():
    # Calculate the number of boxes Kim sold on Wednesday
    wednesday_boxes = 1200 * 0.5

    # Calculate the number of boxes Kim sold on Tuesday
    tuesday_boxes = wednesday_boxes * 2

    result = tuesday_boxes
    return result

print(solution())