def solution():
    
    total_kids = 30
    bars_per_kid = 2
    bars_per_box = 12
    total_bars_needed = total_kids * bars_per_kid
    boxes_needed = total_bars_needed // bars_per_box + int(total_bars_needed % bars_per_box != 0)
    result = boxes_needed
    return result

print(solution())