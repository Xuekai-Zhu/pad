def solution():
    """How many right triangles with a height of 2 inches and a width of two inches could fit inside a square with 2-inch sides?"""
    triangle_area = 0.5 * 2 * 2
    square_area = 2 * 2
    num_triangles = square_area // triangle_area
    result = num_triangles
    return result

print(solution())