def solution():
    remaining_boxes = 4  # Seth has 4 boxes left after giving one to his mother and half away
    total_boxes = remaining_boxes * 2  # Double the number of remaining boxes to get the original number
    total_boxes += 1  # Add the box that he gave to his mother
    result = total_boxes
    return result

print(solution())