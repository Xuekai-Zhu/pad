def solution():
    # Calculate the total area she intended to paint
    total_area = 4 * wall_size

    # Calculate the area she actually painted
    actual_area = total_area - tile_area - ceiling_area

    # Calculate the amount of paint used
    total_paint = actual_area / paint_coverage

    # Calculate the amount of paint left over
    leftover_paint = paint_containers - total_paint

    result = leftover_paint
    return result

print(solution())