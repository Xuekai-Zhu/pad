def solution():
    num_courses_before = 3
    num_courses_after = 5
    num_bricks_per_course = 400

    # Calculate the total number of bricks before the wall was extended
    total_bricks_before = num_courses_before * num_bricks_per_course

    # Calculate the total number of bricks after the wall was extended
    total_bricks_after = num_courses_after * num_bricks_per_course

    # Calculate the number of bricks removed from the last course
    num_bricks_removed = 0.5 * num_bricks_per_course

    # Calculate the total number of bricks after removing half of the last course
    total_bricks_final = total_bricks_after - num_bricks_removed

    result = total_bricks_final
    return result

print(solution())