def solution():
    """An artist uses 3 ounces of paint for every large canvas they cover, and 2 ounces of paint for every small canvas they cover.
    They have completed 3 large paintings and 4 small paintings. How many ounces of paint have they used?"""
    # Define the amount of paint used for each canvas size
    large_canvas_paint = 3
    small_canvas_paint = 2

    # Calculate the total amount of paint used for large paintings
    total_large_paint = large_canvas_paint * 3

    # Calculate the total amount of paint used for small paintings
    total_small_paint = small_canvas_paint * 4

    # Calculate the total amount of paint used for all paintings
    total_paint = total_large_paint + total_small_paint

    # return the result
    result = total_paint
    return result

print(solution())