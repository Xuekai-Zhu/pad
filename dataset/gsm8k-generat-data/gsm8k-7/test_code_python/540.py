def solution():
    num_triangles = 6
    num_squares = 4
    num_hexagons = 2

    # Calculate the total number of sides on all the triangle cookie cutters
    total_triangle_sides = num_triangles * 3

    # Calculate the total number of sides on all the square cookie cutters
    total_square_sides = num_squares * 4

    # Calculate the total number of sides on all the hexagon cookie cutters
    total_hexagon_sides = num_hexagons * 6

    # Calculate the total number of sides on all the cookie cutters
    total_sides = total_triangle_sides + total_square_sides + total_hexagon_sides
    result = total_sides
    return result

print(solution())