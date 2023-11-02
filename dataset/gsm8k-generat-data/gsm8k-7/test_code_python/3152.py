def solution():
    num_cucumber_sandwiches = 10
    num_egg_sandwiches = 8

    num_triangles_per_cucumber_sandwich = 4
    num_rectangles_per_egg_sandwich = 2

    num_triangles_eaten = 28
    num_rectangles_eaten = 12

    # Calculate the total number of cucumber sandwich triangles
    total_cucumber_triangles = num_cucumber_sandwiches * num_triangles_per_cucumber_sandwich

    # Calculate the total number of egg sandwich rectangles
    total_egg_rectangles = num_egg_sandwiches * num_rectangles_per_egg_sandwich

    # Calculate the total number of bread slices eaten
    total_slices_eaten = total_cucumber_triangles + total_egg_rectangles
    result = total_slices_eaten
    return result

print(solution())