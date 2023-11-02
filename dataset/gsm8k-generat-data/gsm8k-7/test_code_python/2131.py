def solution():
    height = 2
    width = 2
    square_side = 2

    # Calculate the area of one right triangle
    triangle_area = (height * width) / 2

    # Calculate the area of the square
    square_area = square_side ** 2

    # Calculate the number of right triangles that can fit inside the square
    num_triangles = square_area // triangle_area
    result = num_triangles
    return result

print(solution())