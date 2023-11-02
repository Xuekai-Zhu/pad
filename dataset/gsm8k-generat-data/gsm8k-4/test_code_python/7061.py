def solution():
    """Four small boxes can fit in one big box. If 50 big boxes can fit four small boxes each, each having 40 candles, calculate the total number of candles in all small boxes."""
    # Define the number of big boxes
    big_boxes = 50

    # Define the number of small boxes in each big box
    small_boxes_per_big_box = 4

    # Define the number of candles in each small box
    candles_per_small_box = 40

    # Calculate the total number of small boxes
    total_small_boxes = big_boxes * small_boxes_per_big_box

    # Calculate the total number of candles in all small boxes
    total_candles = total_small_boxes * candles_per_small_box

    # return the result
    result = total_candles
    return result

print(solution())