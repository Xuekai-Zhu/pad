def solution():
    # Calculate the area of the two 30x12 walls
    wall_1_area = 30 * 12
    wall_2_area = 30 * 12

    # Calculate the area of the 20x12 wall
    wall_3_area = 20 * 12

    # Calculate the total area of glass needed by adding up the area of all three walls
    total_area = wall_1_area + wall_2_area + wall_3_area
    result = total_area
    return result

print(solution())