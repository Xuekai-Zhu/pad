def solution():
    # Calculate the total amount of paint needed for all four walls
    total_paint_needed = 16 * 4  # 16 containers of paint for 4 walls

    # Calculate the amount of paint used for one wall and the ceiling
    wall_and_ceiling_paint = 1  # 1 container of paint used for the ceiling and 0 containers used for the tiled wall

    # Calculate the total amount of paint used
    total_paint_used = total_paint_needed - wall_and_ceiling_paint

    # Calculate the number of containers of paint left over
    left_over_paint = total_paint_used - 16
    result = left_over_paint
    return result

print(solution())