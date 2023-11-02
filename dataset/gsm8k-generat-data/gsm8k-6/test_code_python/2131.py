def solution():
    # Calculate the area of the square and the area of each triangle
    square_area = 2**2
    triangle_area = 0.5 * 2 * 2  # height * base / 2

    # Divide the area of the square by the area of each triangle to find how many triangles can fit inside
    num_triangles = square_area // triangle_area
    result = num_triangles
    return result

print(solution())