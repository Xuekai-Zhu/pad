def solution():
    num_muffins = 95
    muffins_per_box = 5
    num_boxes_available = 10

    # Calculate the total number of boxes needed to pack all the muffins
    total_boxes_needed = num_muffins / muffins_per_box

    # Calculate the number of boxes still needed
    boxes_still_needed = total_boxes_needed - num_boxes_available
    result = round(boxes_still_needed)
    return result

print(solution())