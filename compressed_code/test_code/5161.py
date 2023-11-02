def solution():
    
    muffin_count = 95
    boxes_available = 10
    muffins_per_box = 5
    boxes_needed = muffin_count // muffins_per_box
    boxes_remaining = boxes_needed - boxes_available
    result = boxes_remaining
    return result

print(solution())