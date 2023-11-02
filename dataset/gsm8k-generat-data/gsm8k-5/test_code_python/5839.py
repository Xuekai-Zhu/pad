def solution():
    num_kids = 30  # There are 30 kids playing soccer, including Katie
    num_bars_per_kid = 2  # Katie's mother wants to get 2 granola bars for each kid
    num_bars_per_box = 12  # Each box of granola bars has 12 bars in it

    # Calculate the total number of bars needed for all the kids
    total_bars_needed = num_kids * num_bars_per_kid

    # Calculate the number of boxes needed to get enough granola bars
    num_boxes_needed = total_bars_needed // num_bars_per_box

    # If there are any leftover bars, add an extra box
    if total_bars_needed % num_bars_per_box != 0:
        num_boxes_needed += 1

    result = num_boxes_needed
    return result

print(solution())