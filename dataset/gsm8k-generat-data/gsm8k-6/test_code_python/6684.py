def solution():
    # Calculate the total number of boxes needed to pack all the muffins
    total_boxes_needed = 95 / 5  # 5 muffins per box
    # Calculate the remaining boxes needed
    remaining_boxes_needed = total_boxes_needed - 10  # only 10 boxes available
    result = remaining_boxes_needed
    return result

print(solution())