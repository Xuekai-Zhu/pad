def solution():
    # Calculate the area of the square
    square_area = 2 * 2

    # Calculate the area of each right triangle
    triangle_area = (2 * 2) / 2

    # Calculate how many triangles can fit inside the square
    num_triangles = square_area // triangle_area

    result = num_triangles
    return result

print(solution())