def solution():
    # Calculate the total number of lines for the triangles
    triangles_lines = 12 * 3

    # Calculate the total number of lines for the squares
    squares_lines = 8 * 4

    # Calculate the total number of lines for the pentagons
    pentagons_lines = 4 * 5

    # Calculate the total number of lines
    total_lines = triangles_lines + squares_lines + pentagons_lines
    result = total_lines
    return result

print(solution())