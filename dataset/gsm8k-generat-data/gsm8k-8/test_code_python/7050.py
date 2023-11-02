def solution():
    # Define the number of courses and bricks per course
    num_courses = 6
    bricks_per_course = 10

    # Calculate the total number of bricks for each wall
    bricks_per_wall = num_courses * bricks_per_course

    # Calculate the total number of bricks for the first three walls
    total_bricks_first_three_walls = bricks_per_wall * 3

    # Calculate the number of bricks used in the last wall
    bricks_used_in_last_wall = (num_courses - 2) * bricks_per_course

    # Calculate the total number of bricks used
    total_bricks_used = total_bricks_first_three_walls + bricks_used_in_last_wall
    result = total_bricks_used
    return result

print(solution())