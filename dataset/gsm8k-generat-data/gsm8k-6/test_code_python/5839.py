def solution():
    # Calculate the total number of granola bars needed
    granola_bars_needed = 2 * 30  # 2 granola bars for each of the 30 kids playing soccer, total 60 granola bars

    # Calculate the number of boxes of granola bars needed
    boxes_needed = granola_bars_needed // 12  # 1 box has 12 granola bars
    if granola_bars_needed % 12 != 0:
        boxes_needed += 1  # if there are any leftover granola bars, add another box

    result = boxes_needed
    return result

print(solution())