def solution():
    wall_1_solid = ((20 * 8) - (3 * 7))
    wall_2_solid = ((20 * 8) - (6 * 4))
    wall_3_solid = ((20 * 8) - (5 * 7))
    wall_4_solid = (20 * 8)
    total_wall_space = wall_1_solid + wall_2_solid + wall_3_solid + wall_4_solid
    result = total_wall_space
    return result

print(solution())