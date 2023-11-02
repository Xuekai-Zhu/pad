def solution():
    # Define the ratios of blue, green, and white paint
    blue_ratio = 1
    green_ratio = 2
    white_ratio = 5

    # Calculate the total ratio of paint
    total_ratio = blue_ratio + green_ratio + white_ratio

    # Calculate the amount of green paint used
    green_paint_used = 6

    # Calculate the amount of total paint used
    total_paint_used = green_paint_used * (total_ratio / green_ratio)
    result = total_paint_used
    return result

print(solution())