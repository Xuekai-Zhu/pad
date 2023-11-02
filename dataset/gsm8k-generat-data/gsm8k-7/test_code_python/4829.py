def solution():
    triangles = 12
    squares = 8
    pentagons = 4

    # Calculate the total number of lines in all triangles
    triangles_lines = triangles * 3

    # Calculate the total number of lines in all squares
    squares_lines = squares * 4

    # Calculate the total number of lines in all pentagons
    pentagons_lines = pentagons * 5

    # Calculate the total number of lines that Bill drew
    total_lines = triangles_lines + squares_lines + pentagons_lines
    result = total_lines
    return result

print(solution())