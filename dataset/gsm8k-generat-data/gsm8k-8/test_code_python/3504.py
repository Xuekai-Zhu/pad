def solution():
    # Calculate the number of bricks in the first three courses
    first_three_courses = 3 * 400

    # Calculate the number of bricks in the last two courses
    last_two_courses = 2 * 400

    # Calculate the number of bricks taken out in the last course
    bricks_taken_out = 0.5 * 400

    # Calculate the total number of bricks
    total_bricks = first_three_courses + last_two_courses - bricks_taken_out
    result = total_bricks
    return result

print(solution())