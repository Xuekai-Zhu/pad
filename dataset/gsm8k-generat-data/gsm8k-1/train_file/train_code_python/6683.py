def solution():
    """The bakery made 95 muffins. They will be packed in boxes with 5 muffins in each box. If there are only 10 available boxes, how many boxes do they still need to pack all the muffins?"""
    muffins = 95
    muffins_per_box = 5
    available_boxes = 10
    boxes_needed = (muffins + (muffins_per_box-1)) // muffins_per_box  # Round up to nearest integer
    boxes_left = boxes_needed - available_boxes
    result = boxes_left if boxes_left > 0 else 0
    return result

print(solution())