def solution():
    paint_per_large_canvas = 3  # The artist uses 3 ounces of paint for every large canvas
    paint_per_small_canvas = 2  # The artist uses 2 ounces of paint for every small canvas
    num_large_paintings = 3  # The artist completed 3 large paintings
    num_small_paintings = 4  # The artist completed 4 small paintings

    # Calculate the total amount of paint used for large paintings
    total_paint_for_large = paint_per_large_canvas * num_large_paintings

    # Calculate the total amount of paint used for small paintings
    total_paint_for_small = paint_per_small_canvas * num_small_paintings

    # Calculate the total amount of paint used
    total_paint_used = total_paint_for_large + total_paint_for_small
    result = total_paint_used
    return result

print(solution())