def solution():
    # Define the amount of paint used by Dexter and Jay
    dexter_paint_used = (3/8) * 4
    jay_paint_used = (5/8) * 4

    # Calculate the total amount of paint used
    total_paint_used = dexter_paint_used + jay_paint_used

    # Calculate the amount of paint left
    paint_left = 4 - total_paint_used
    result = paint_left
    return result

print(solution())