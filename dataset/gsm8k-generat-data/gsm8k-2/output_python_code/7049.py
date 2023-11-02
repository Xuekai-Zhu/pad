def solution():
    """On a construction site, a mason has to build 6 courses of a wall, each having 10 bricks per course. He has to build 4 such walls
    and realized he won't be able to finish two courses of the last wall because there were not enough bricks. What's the total number of bricks that he has used?"""
    bricks_per_course = 10
    completed_walls = 3
    partial_wall_courses = 4
    total_bricks = (bricks_per_course * 6 * completed_walls) + (bricks_per_course * partial_wall_courses * 8)
    result = total_bricks
    return result

print(solution())