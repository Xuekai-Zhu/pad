def solution():
    """Emery looks through the drawer where her mom keeps the cookie cutters. There are 6 cookie cutters shaped like triangles, 4 square ones and 2 hexagons. How many sides are there on the cookie cutters in total?"""
    triangle_sides = 3 * 6
    square_sides = 4 * 4
    hexagon_sides = 6 * 2
    total_sides = triangle_sides + square_sides + hexagon_sides
    result = total_sides
    return result

print(solution())