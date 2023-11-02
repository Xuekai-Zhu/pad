def solution():
    """Kiki made 10 cucumber sandwiches and 8 egg sandwiches for the tea party. Each cucumber sandwich was cut into 4 triangles. Each egg sandwich was cut into 2 rectangles. If her guests ate 28 triangles and 12 rectangles, how many slices of bread did they eat?"""
    cucumber_sandwiches = 10
    egg_sandwiches = 8
    cucumber_triangles_per_sandwich = 4
    egg_rectangles_per_sandwich = 2
    total_cucumber_triangles_eaten = 28
    total_egg_rectangles_eaten = 12
    total_cucumber_sandwich_triangles = cucumber_sandwiches * cucumber_triangles_per_sandwich
    total_egg_sandwich_rectangles = egg_sandwiches * egg_rectangles_per_sandwich
    total_sandwich_slices_eaten = total_cucumber_triangles_eaten / \
        cucumber_triangles_per_sandwich + \
        total_egg_rectangles_eaten / egg_rectangles_per_sandwich
    total_sandwich_slices = total_cucumber_sandwich_triangles / \
        cucumber_triangles_per_sandwich + \
        total_egg_sandwich_rectangles / egg_rectangles_per_sandwich
    bread_slices_eaten = total_sandwich_slices - total_sandwich_slices_eaten
    result = bread_slices_eaten
    return result

print(solution())