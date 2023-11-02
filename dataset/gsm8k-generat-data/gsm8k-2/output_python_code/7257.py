def solution():
    """A single line is worth 1000 points. A tetris is worth 8 times that much. Tim scored 6 singles and 4 tetrises. How many points did he score?"""
    single_line_points = 1000
    tetris_points = 8 * single_line_points
    total_points = (6 * single_line_points) + (4 * tetris_points)
    result = total_points
    return result

print(solution())