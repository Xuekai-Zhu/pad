def solution():
    # Calculate the number of granola bars needed
    total_granola_bars = 2 * 30
    # Calculate the number of boxes needed
    boxes_needed = total_granola_bars // 12
    if total_granola_bars % 12 != 0:
        boxes_needed += 1
    result = boxes_needed
    return result

print(solution())