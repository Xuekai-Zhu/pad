def solution():
    """After geometry class, Bill wants to count how many lines he drew. For each shape, he drew one line per side. If he drew 12 triangles, 8 squares, and 4 pentagons, how many lines did he draw?"""
    # Define the number of sides for each shape
    TRIANGLE_SIDES = 3
    SQUARE_SIDES = 4
    PENTAGON_SIDES = 5

    # Define the number of shapes of each type drawn
    triangle_count = 12
    square_count = 8
    pentagon_count = 4

    # Calculate the total number of lines drawn
    total_lines = triangle_count * TRIANGLE_SIDES + square_count * SQUARE_SIDES + pentagon_count * PENTAGON_SIDES

    # Display the total number of lines drawn
    result = total_lines
    return result

print(solution())