def solution():
    
    paint_per_large_canvas = 3
    paint_per_small_canvas = 2
    num_large_paintings = 3
    num_small_paintings = 4
    total_paint_used = (paint_per_large_canvas * num_large_paintings) + (paint_per_small_canvas * num_small_paintings)
    result = total_paint_used
    return result

print(solution())