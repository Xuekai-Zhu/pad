def solution():
    """Kiki made 10 cucumber sandwiches and 8 egg sandwiches for the tea party. Each cucumber sandwich was cut into 4 triangles. Each egg sandwich was cut into 2 rectangles. If her guests ate 28 triangles and 12 rectangles, how many slices of bread did they eat?"""
    # Calculate the total number of cucumber sandwich triangles
    cucumber_triangles = 10 * 4

    # Calculate the total number of egg sandwich rectangles
    egg_rectangles = 8 * 2

    # Calculate the total number of bread slices
    bread_slices = cucumber_triangles + egg_rectangles

    # Calculate the number of bread slices eaten by the guests
    guest_slices = 28 + 12

    # Calculate the number of bread slices left
    remaining_slices = bread_slices - guest_slices

    # return the result
    result = bread_slices
    return result

print(solution())