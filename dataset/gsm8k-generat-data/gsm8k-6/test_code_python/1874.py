def solution():
    # Calculate the number of boxes of cookies left for Sonny
    initial_boxes = 45
    given_away_boxes = 12 + 9 + 7
    boxes_left = initial_boxes - given_away_boxes
    result = boxes_left
    return result

print(solution())