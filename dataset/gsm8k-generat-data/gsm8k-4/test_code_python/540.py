def solution():
    """Emery looks through the drawer where her mom keeps the cookie cutters. There are 6 cookie cutters shaped like triangles, 4 square ones and 2 hexagons. How many sides are there on the cookie cutters in total?"""
    # Define the number of sides on each type of cookie cutter
    triangle_sides = 3
    square_sides = 4
    hexagon_sides = 6

    # Calculate the total number of sides
    total_sides = (triangle_sides * 6) + (square_sides * 4) + (hexagon_sides * 2)

    # return the result
    result = total_sides
    return result

print(solution())