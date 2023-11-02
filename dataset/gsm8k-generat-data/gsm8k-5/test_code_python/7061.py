def solution():
    candles_per_small_box = 40  # Each small box contains 40 candles
    small_boxes_per_big_box = 4  # Four small boxes can fit in one big box
    big_boxes = 50  # There are 50 big boxes

    # Calculate the total number of small boxes
    total_small_boxes = big_boxes * small_boxes_per_big_box

    # Calculate the total number of candles in all small boxes
    total_candles = total_small_boxes * candles_per_small_box
    result = total_candles
    return result

print(solution())