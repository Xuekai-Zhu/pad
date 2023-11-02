def solution():
    small_boxes_per_big_box = 4
    candles_per_small_box = 40
    big_boxes = 50

    # Calculate the total number of small boxes
    total_small_boxes = big_boxes * small_boxes_per_big_box

    # Calculate the total number of candles
    total_candles = total_small_boxes * candles_per_small_box
    result = total_candles
    return result

print(solution())