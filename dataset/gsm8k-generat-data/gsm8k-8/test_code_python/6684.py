def solution():
    total_muffins = 95
    muffins_per_box = 5
    available_boxes = 10

    # Calculate how many boxes are needed to pack all muffins
    boxes_needed = total_muffins // muffins_per_box

    # Calculate how many boxes are still needed
    boxes_still_needed = boxes_needed - available_boxes
    result = boxes_still_needed
    return result

print(solution())