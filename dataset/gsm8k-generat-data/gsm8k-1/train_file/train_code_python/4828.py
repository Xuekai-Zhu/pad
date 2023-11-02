def solution():
    """After geometry class, Bill wants to count how many lines he drew. For each shape, he drew one line per side. If he drew 12 triangles, 8 squares, and 4 pentagons, how many lines did he draw?"""
    lines_per_triangle = 3
    lines_per_square = 4
    lines_per_pentagon = 5
    num_triangles = 12
    num_squares = 8
    num_pentagons = 4
    total_lines = (lines_per_triangle * num_triangles) + (lines_per_square * num_squares) + (lines_per_pentagon * num_pentagons)
    result = total_lines
    return result

print(solution())