def solution():
    """Emery looks through the drawer where her mom keeps the cookie cutters. There are 6 cookie cutters shaped like triangles, 4 square ones and 2 hexagons. How many sides are there on the cookie cutters in total?"""
    triangles = 6
    squares = 4
    hexagons = 2
    total_sides = (triangles * 3) + (squares * 4) + (hexagons * 6)
    result = total_sides
    return result

print(solution())