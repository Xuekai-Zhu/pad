def solution():
    num_kids = 30
    num_bars_per_kid = 2
    num_bars_per_box = 12

    # Calculate the total number of bars needed
    total_bars_needed = num_kids * num_bars_per_kid

    # Calculate the total number of boxes needed
    total_boxes_needed = total_bars_needed / num_bars_per_box
    if total_bars_needed % num_bars_per_box != 0:
        total_boxes_needed += 1

    result = total_boxes_needed
    return result

print(solution())