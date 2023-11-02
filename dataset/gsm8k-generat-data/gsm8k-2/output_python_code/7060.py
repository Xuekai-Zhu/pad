def solution():
    """Four small boxes can fit in one big box. If 50 big boxes can fit four small boxes each, each having 40 candles, calculate the total number of candles in all small boxes."""
    small_boxes_in_big_box = 4
    big_boxes = 50
    small_boxes = big_boxes * small_boxes_in_big_box
    candles_per_small_box = 40
    total_candles = small_boxes * candles_per_small_box
    result = total_candles
    return result

print(solution())