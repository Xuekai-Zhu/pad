def solution():
    total_ribbon = 4.5  # Marissa has 4.5 feet of ribbon
    ribbon_per_box = 0.7  # Marissa uses 0.7 feet of ribbon per box

    # Calculate the number of boxes Marissa can tie
    num_boxes = int((total_ribbon - 1) / ribbon_per_box)
    result = num_boxes
    return result

print(solution())