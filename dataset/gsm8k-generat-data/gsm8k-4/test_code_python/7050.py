def solution():
    """On a construction site, a mason has to build 6 courses of a wall, each having 10 bricks per course. He has to build 4 such walls and realized he won't be able to finish two courses of the last wall because there were not enough bricks. What's the total number of bricks that he has used?"""
    # Define the number of courses per wall and the numbers of walls
    COURSES_PER_WALL = 6
    WALLS = 4

    # Define the number of bricks per course
    BRICKS_PER_COURSE = 10

    # Calculate the total number of courses and the bricks used for complete walls
    total_courses = COURSES_PER_WALL * WALLS
    total_bricks = total_courses * BRICKS_PER_COURSE

    # Calculate the bricks used for the incomplete wall
    incomplete_courses = 2
    incomplete_bricks = incomplete_courses * BRICKS_PER_COURSE

    # Calculate the total number of bricks used
    total_bricks_used = total_bricks + incomplete_bricks

    # return the result
    result = total_bricks_used
    return result

print(solution())