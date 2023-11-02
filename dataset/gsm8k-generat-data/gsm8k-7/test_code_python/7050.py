def solution():
    courses_per_wall = 6
    bricks_per_course = 10
    num_walls = 4

    # Calculate the total number of bricks needed for all walls
    total_bricks_needed = courses_per_wall * bricks_per_course * num_walls

    # Calculate the number of bricks used, accounting for the two incomplete courses
    num_bricks_used = total_bricks_needed - (2 * bricks_per_course)

    result = num_bricks_used
    return result

print(solution())