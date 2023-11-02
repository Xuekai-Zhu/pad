def solution():
    """The bakery made 95 muffins. They will be packed in boxes with 5 muffins in each box. If there are only 10 available boxes, how many boxes do they still need to pack all the muffins?"""
    muffin_count = 95
    boxes_available = 10
    muffins_per_box = 5
    boxes_needed = muffin_count // muffins_per_box
    boxes_remaining = boxes_needed - boxes_available
    result = boxes_remaining
    return result

print(solution())