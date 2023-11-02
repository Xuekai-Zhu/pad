def solution():
    # Calculate the area of the square
    area_square = 2 * 2  # Two-inch sides

    # Calculate the area of each right triangle
    area_triangle = 0.5 * 2 * 2  # Height of 2 inches and width of 2 inches

    # Calculate the number of right triangles that can fit inside the square
    num_triangles = int(area_square // area_triangle)
    result = num_triangles
    return result

print(solution())