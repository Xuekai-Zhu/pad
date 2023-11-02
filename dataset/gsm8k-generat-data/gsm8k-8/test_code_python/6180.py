def solution():
    # Define the amount of paint needed for each canvas
    large_canvas_paint = 3
    small_canvas_paint = 2

    # Calculate the total amount of paint used for the large and small canvases
    total_large_paint = 3 * large_canvas_paint
    total_small_paint = 4 * small_canvas_paint

    # Calculate the total amount of paint used
    total_paint_used = total_large_paint + total_small_paint

    result = total_paint_used
    return result

print(solution())