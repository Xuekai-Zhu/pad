def solution():
    """An artist uses 3 ounces of paint for every large canvas they cover, and 2 ounces of paint for every small canvas they cover. They have completed 3 large paintings and 4 small paintings. How many ounces of paint have they used?"""
    # Define the amount of paint used per large and small canvas
    LARGE_CANVAS_PAINT = 3
    SMALL_CANVAS_PAINT = 2

    # Define the number of large and small canvases completed
    large_canvases = 3
    small_canvases = 4

    # Calculate the total amount of paint used
    total_paint_used = (large_canvases * LARGE_CANVAS_PAINT) + (small_canvases * SMALL_CANVAS_PAINT)

    # Display the total amount of paint used
    result = total_paint_used
    return result

print(solution())