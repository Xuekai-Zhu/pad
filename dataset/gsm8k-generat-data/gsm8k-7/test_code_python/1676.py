def solution():
    num_walls = 4
    num_paint_containers = 16

    # Subtract the amount of paint needed for the ceiling and tile wall
    num_paint_containers -= 1  # for the ceiling
    num_paint_containers -= 1  # for the tile wall

    # Calculate the number of paint containers left over
    num_paint_containers_left = num_paint_containers - num_walls
    result = num_paint_containers_left
    return result

print(solution())