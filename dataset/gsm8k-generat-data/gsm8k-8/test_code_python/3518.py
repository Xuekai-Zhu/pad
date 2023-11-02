def solution():
    # Calculate the surface area of each wall
    wall1 = 10 * 16
    wall2 = 10 * 16
    wall3 = 10 * 12
    wall4 = 10 * 12

    # Calculate the total surface area to be painted
    total_surface_area = (2 * wall1) + (2 * wall2) + wall3 + wall4

    # Calculate the total area to be covered with primer and paint
    total_area_to_cover = total_surface_area * 3

    # Calculate the time needed to paint the kitchen
    hours_needed = total_area_to_cover / 40
    result = hours_needed
    return result

print(solution())