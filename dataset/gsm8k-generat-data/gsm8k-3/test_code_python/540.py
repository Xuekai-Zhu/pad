def solution():
    """Emery looks through the drawer where her mom keeps the cookie cutters. There are 6 cookie cutters shaped like triangles, 4 square ones and 2 hexagons. How many sides are there on the cookie cutters in total?"""
    # Define the number of sides for each type of cookie cutter
    TRIANGLE_SIDES = 3
    SQUARE_SIDES = 4
    HEXAGON_SIDES = 6

    # Define the number of each type of cookie cutter
    triangle_cutters = 6
    square_cutters = 4
    hexagon_cutters = 2

    # Calculate the total number of sides on all the cookie cutters
    total_sides = (triangle_cutters * TRIANGLE_SIDES) + (square_cutters * SQUARE_SIDES) + (hexagon_cutters * HEXAGON_SIDES)

    # Display the total number of sides
    result = total_sides
    return result

print(solution())