def solution():
    """An artist uses 3 ounces of paint for every large canvas they cover, and 2 ounces of paint for every small canvas they cover. They have completed 3 large paintings and 4 small paintings. How many ounces of paint have they used?"""
    paint_per_large_canvas = 3
    paint_per_small_canvas = 2
    num_large_paintings = 3
    num_small_paintings = 4
    total_paint_used = (paint_per_large_canvas * num_large_paintings) + (paint_per_small_canvas * num_small_paintings)
    result = total_paint_used
    return result

print(solution())