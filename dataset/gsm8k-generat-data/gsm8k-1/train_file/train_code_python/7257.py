def solution():
    """A single line is worth 1000 points. A tetris is worth 8 times that much. Tim scored 6 singles and 4 tetrises. How many points did he score?"""
    single_line_points = 1000
    tetris_points = 8 * single_line_points
    singles_scored = 6
    tetrises_scored = 4
    total_score = (single_line_points * singles_scored) + (tetris_points * tetrises_scored)
    result = total_score
    return result

print(solution())