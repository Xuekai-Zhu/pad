def solution():
    total_ribbon = 4.5
    ribbon_per_box = 0.7

    # Calculate the total length of ribbon used to tie all the boxes
    total_ribbon_used = total_ribbon - 1  # Subtract the leftover foot from total ribbon
    num_boxes = total_ribbon_used / ribbon_per_box
    result = num_boxes
    return result

print(solution())