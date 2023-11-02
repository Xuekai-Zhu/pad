def solution():
    # Number of sides on a triangle cookie cutter = 3
    # Number of triangle cookie cutters = 6
    triangle_sides = 3 * 6

    # Number of sides on a square cookie cutter = 4
    # Number of square cookie cutters = 4
    square_sides = 4 * 4

    # Number of sides on a hexagon cookie cutter = 6
    # Number of hexagon cookie cutters = 2
    hexagon_sides = 6 * 2

    # Total number of sides on all cookie cutters
    total_sides = triangle_sides + square_sides + hexagon_sides
    result = total_sides
    return result

print(solution())