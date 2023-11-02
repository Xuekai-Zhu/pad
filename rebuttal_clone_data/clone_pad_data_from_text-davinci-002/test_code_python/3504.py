def solution():
    initial_courses = 3
    additional_courses = 2
    initial_bricks_per_course = 400
    removed_bricks = initial_bricks_per_course / 2
    total_bricks = (initial_courses + additional_courses) * initial_bricks_per_course - removed_bricks
    result = total_bricks
    return result

print(solution())