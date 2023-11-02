def solution():
    # Calculate the total number of cucumber triangles
    cucumber_triangles = 10 * 4  # Each cucumber sandwich is cut into 4 triangles

    # Calculate the total number of egg rectangles
    egg_rectangles = 8 * 2  # Each egg sandwich is cut into 2 rectangles

    # Calculate the total number of bread slices eaten
    total_slices = cucumber_triangles + egg_rectangles

    result = total_slices
    return result

print(solution())