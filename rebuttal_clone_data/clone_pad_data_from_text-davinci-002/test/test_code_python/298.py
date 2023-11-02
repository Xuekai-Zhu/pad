def solution():
    num_triangles = 6
    num_squares = 4
    num_hexagons = 2
    total_sides = (num_triangles * 3) + (num_squares * 4) + (num_hexagons * 6)
    result = total_sides
    return result

print(solution())