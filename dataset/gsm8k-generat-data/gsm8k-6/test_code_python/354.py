def solution():
    # Start with the number of boxes Seth has now and work backwards
    remaining_boxes = 4
    remaining_boxes *= 2  # double the number of remaining boxes to account for the boxes he gave away
    remaining_boxes += 1  # add the box he gave to his mother
    result = remaining_boxes
    return result

print(solution())