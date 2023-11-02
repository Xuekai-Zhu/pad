def solution():
    # Calculate the total amount of paint needed
    total_paint = 140 / 0.7

    # Calculate the amount of red paint needed
    red_paint = 0.2 * total_paint

    # Calculate the amount of white paint needed
    white_paint = total_paint - 140 - red_paint

    result = white_paint
    return result

print(solution())