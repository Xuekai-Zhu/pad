def solution():
    # Calculate the area of each wall
    wall_area = 10 * 16

    # Calculate the total area of all four walls
    total_area = 4 * wall_area

    # Calculate the total area that needs to be painted (3 coats)
    total_paint_area = 3 * total_area

    # Calculate the total time required to paint the kitchen
    time_required = total_paint_area / 40  # 40 square feet per hour

    result = time_required
    return result

print(solution())