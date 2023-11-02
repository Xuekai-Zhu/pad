def solution():
    # Calculate the total number of courses of bricks in the wall
    total_courses = 3 + 2  # they added 2 more courses

    # Calculate the total number of bricks in the wall
    total_bricks = total_courses * 400  # each course has 400 bricks

    # Calculate the number of bricks removed from the last course
    removed_bricks = 0.5 * 400  # half of 400 bricks

    # Subtract the number of removed bricks from the total number of bricks
    final_total_bricks = total_bricks - removed_bricks

    result = final_total_bricks
    return result

print(solution())