def solution():
    points_single = 1000
    points_tetris = points_single * 8
    singles = 6
    tetrises = 4
    total_points = singles * points_single + tetrises * points_tetris
    result = total_points
    return result

print(solution())