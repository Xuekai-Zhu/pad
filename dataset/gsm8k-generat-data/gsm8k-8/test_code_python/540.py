def solution():
    # Calculate the total number of sides on the triangle cookie cutters
    triangle_sides = 6 * 3

    # Calculate the total number of sides on the square cookie cutters
    square_sides = 4 * 4

    # Calculate the total number of sides on the hexagon cookie cutters
    hexagon_sides = 2 * 6

    # Calculate the total number of sides on all the cookie cutters combined
    total_sides = triangle_sides + square_sides + hexagon_sides
    result = total_sides
    return result

print(solution())