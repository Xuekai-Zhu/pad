def solution():
    # Calculate the total number of points scored by Tim
    singles_points = 1000 * 6  # 6 singles worth 1000 points each
    tetris_points = 8 * 1000 * 4  # 4 tetrises worth 8 times 1000 points each
    total_points = singles_points + tetris_points
    result = total_points
    return result

print(solution())