def solution():
    """After geometry class, Bill wants to count how many lines he drew. For each shape, he drew one line per side. If he drew 12 triangles, 8 squares, and 4 pentagons, how many lines did he draw?"""
    # Define the number of sides for each shape
    triangle_sides = 3
    square_sides = 4
    pentagon_sides = 5

    # Count the total number of lines drawn
    total_lines = (triangle_sides * 12) + (square_sides * 8) + (pentagon_sides * 4)

    result = total_lines
    return result

print(solution())