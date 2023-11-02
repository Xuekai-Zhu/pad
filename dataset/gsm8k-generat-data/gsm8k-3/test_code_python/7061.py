def solution():
    """Four small boxes can fit in one big box. If 50 big boxes can fit four small boxes each, each having 40 candles, calculate the total number of candles in all small boxes."""
    # Calculate the number of small boxes that can fit in 50 big boxes
    small_boxes = 50 * 4

    # Calculate the total number of candles in all small boxes
    total_candles = small_boxes * 40

    # Display the total number of candles
    result = total_candles
    return result

print(solution())