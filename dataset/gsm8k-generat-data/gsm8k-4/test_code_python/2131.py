def solution():
    """How many right triangles with a height of 2 inches and a width of two inches could fit inside a square with 2-inch sides?"""
    # Calculate the area of a right triangle with a height and width of 2 inches
    triangle_area = (2 * 2) / 2

    # Calculate the area of the square with 2-inch sides
    square_area = 2 * 2

    # Divide the area of the square by the area of the triangle to get the number of triangles that can fit inside the square
    num_triangles = square_area / triangle_area

    # Round down the number of triangles to the nearest whole number
    num_triangles = int(num_triangles)

    result = num_triangles
    return result

print(solution())