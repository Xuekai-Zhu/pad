def solution():
    # Find the number of boxes sold on Wednesday and Tuesday
    wednesday_boxes = 1200 * 2  # Kim sold twice as many boxes on Wednesday as on Thursday
    tuesday_boxes = wednesday_boxes * 2  # Kim sold twice as many boxes on Tuesday as on Wednesday

    result = tuesday_boxes
    return result

print(solution())