def solution():
    """After geometry class, Bill wants to count how many lines he drew. For each shape, he drew one line per side. If he drew 12 triangles, 8 squares, and 4 pentagons, how many lines did he draw?"""
    triangles = 12
    squares = 8
    pentagons = 4
    total_lines = triangles*3 + squares*4 + pentagons*5
    result = total_lines
    return result

print(solution())