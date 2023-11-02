def solution():
    total_boxes = 45  # Sonny received 45 boxes of cookies
    boxes_given = 12 + 9 + 7  # Sonny gave away 12 boxes to his brother, 9 boxes to his sister, and 7 boxes to his cousin
    boxes_left = total_boxes - boxes_given  # Sonny is left with the remaining boxes

    result = boxes_left
    return result

print(solution())