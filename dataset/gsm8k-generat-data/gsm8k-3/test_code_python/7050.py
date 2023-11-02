def solution():
    """On a construction site, a mason has to build 6 courses of a wall, each having 10 bricks per course. He has to build 4 such walls and realized he won't be able to finish two courses of the last wall because there were not enough bricks. What's the total number of bricks that he has used?"""
    # Define the number of courses per wall and bricks per course
    COURSES_PER_WALL = 6
    BRICKS_PER_COURSE = 10

    # Define the number of walls to be built
    NUM_WALLS = 4

    # Calculate the total number of bricks needed for all the walls
    total_bricks_needed = NUM_WALLS * COURSES_PER_WALL * BRICKS_PER_COURSE

    # Calculate the number of bricks that the mason was unable to use
    unused_bricks = 2 * BRICKS_PER_COURSE

    # Calculate the total number of bricks used
    total_bricks_used = total_bricks_needed - unused_bricks

    # Display the total number of bricks used
    result = total_bricks_used
    return result

print(solution())