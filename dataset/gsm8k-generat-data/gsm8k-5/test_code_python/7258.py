def solution():
    single_line_points = 1000  # Points for a single line
    tetris_points = 8 * single_line_points  # Points for a tetris
    num_single_lines = 6  # Number of single lines scored by Tim
    num_tetrises = 4  # Number of tetrises scored by Tim

    # Calculate the total points scored by Tim
    total_points = (num_single_lines * single_line_points) + (num_tetrises * tetris_points)
    result = total_points
    return result

print(solution())