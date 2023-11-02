def solution():
    courses_initial = 3  # The wall initially had 3 courses
    courses_final = 5  # The wall was later extended by 2 courses
    bricks_per_course = 400  # Each course had 400 bricks
    bricks_last_course = bricks_per_course / 2  # Half of the bricks in the last course were removed for easy garden checkup

    # Calculate the total number of bricks in the wall
    total_bricks = (courses_initial + courses_final - 1) * bricks_per_course + bricks_last_course
    result = total_bricks
    return result

print(solution())