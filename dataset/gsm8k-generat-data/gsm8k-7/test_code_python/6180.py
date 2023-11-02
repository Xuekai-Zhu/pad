def solution():
    paint_per_large_canvas = 3
    paint_per_small_canvas = 2
    num_large_paintings = 3
    num_small_paintings = 4

    # Calculate the total amount of paint used for all large paintings
    total_paint_for_large = paint_per_large_canvas * num_large_paintings

    # Calculate the total amount of paint used for all small paintings
    total_paint_for_small = paint_per_small_canvas * num_small_paintings

    # Calculate the total amount of paint used for all paintings
    total_paint_used = total_paint_for_large + total_paint_for_small
    result = total_paint_used
    return result

print(solution())