def solution():
    
    courses_initial = 3
    courses_added = 2
    bricks_per_course = 400
    bricks_in_last_course = bricks_per_course // 2
    total_courses = courses_initial + courses_added
    total_bricks = total_courses * bricks_per_course - bricks_per_course + bricks_in_last_course
    result = total_bricks
    return result

print(solution())