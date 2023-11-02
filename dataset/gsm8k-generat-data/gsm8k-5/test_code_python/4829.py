def solution():
    # For each shape, Bill drew one line per side
    lines_per_triangle = 3
    lines_per_square = 4
    lines_per_pentagon = 5

    # Bill drew 12 triangles, 8 squares, and 4 pentagons
    num_triangles = 12
    num_squares = 8
    num_pentagons = 4

    # Calculate the total number of lines Bill drew
    total_lines = lines_per_triangle * num_triangles + \
                  lines_per_square * num_squares + \
                  lines_per_pentagon * num_pentagons
    result = total_lines
    return result

print(solution())