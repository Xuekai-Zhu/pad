def solution():
    # Calculate the total number of cucumber triangles
    cucumber_triangles = 10 * 4

    # Calculate the total number of egg rectangles
    egg_rectangles = 8 * 2

    # Calculate the total number of bread slices eaten
    total_slices = cucumber_triangles + egg_rectangles

    # Verify if the number of slices matches the number eaten
    if total_slices == 28 + 12:
        result = total_slices
    else:
        result = "Error: number of slices does not match number eaten"

    return result

print(solution())