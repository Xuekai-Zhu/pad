def solution():
    """On a construction site, a mason has to build 6 courses of a wall, each having 10 bricks per course. He has to build 4 such walls and realized he won't be able to finish two courses of the last wall because there were not enough bricks. What's the total number of bricks that he has used?"""
    courses_per_wall = 6
    bricks_per_course = 10
    total_walls = 4
    total_bricks = courses_per_wall * bricks_per_course * total_walls
    bricks_left = 2 * bricks_per_course
    bricks_used = total_bricks - bricks_left
    result = bricks_used
    return result

print(solution())