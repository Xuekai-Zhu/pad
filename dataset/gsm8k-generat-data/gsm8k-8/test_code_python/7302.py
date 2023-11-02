def solution():
    # Calculate the total surface area of the room
    total_surface_area = 2 * ((20 * 8) + (20 * 8) + (20 * 20))

    # Calculate the area of the doorway on the first wall
    doorway1_area = 3 * 7

    # Calculate the area of the window on the second wall
    window_area = 6 * 4

    # Calculate the area of the doorway on the third wall
    doorway2_area = 5 * 7

    # Calculate the total area to be painted
    area_to_paint = total_surface_area - (doorway1_area + window_area + doorway2_area)

    result = area_to_paint
    return result

print(solution())