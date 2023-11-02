def solution():
    """How many right triangles with a height of 2 inches and a width of two inches could fit inside a square with 2-inch sides?"""
    # Calculate the area of the square
    square_area = 2 ** 2

    # Calculate the area of each right triangle
    triangle_area = 0.5 * 2 * 2

    # Calculate the number of right triangles that can fit inside the square
    num_triangles = square_area // triangle_area

    # Display the number of right triangles
    result = num_triangles
    return result

print(solution())