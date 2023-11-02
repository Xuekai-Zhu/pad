def solution():
    # Calculate the total number of lines drawn by Bill
    lines_triangles = 12 * 3  # Bill drew 1 line per side of a triangle
    lines_squares = 8 * 4  # Bill drew 1 line per side of a square
    lines_pentagons = 4 * 5  # Bill drew 1 line per side of a pentagon
    total_lines = lines_triangles + lines_squares + lines_pentagons
    result = total_lines
    return result

print(solution())