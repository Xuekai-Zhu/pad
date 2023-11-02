def solution():
    # Calculate the number of walls that Mikaela is painting
    num_walls = 4

    # Calculate the number of containers of paint needed to paint the four walls
    paint_needed = 16

    # Calculate the number of containers of paint needed to paint the flowers on the ceiling
    paint_for_ceiling = 1

    # Calculate the total number of containers of paint used
    total_paint_used = paint_needed + paint_for_ceiling

    # Calculate the number of containers of paint left over
    paint_left_over = 20 - total_paint_used  # Mikaela originally bought 20 containers of paint
    result = paint_left_over
    return result

print(solution())