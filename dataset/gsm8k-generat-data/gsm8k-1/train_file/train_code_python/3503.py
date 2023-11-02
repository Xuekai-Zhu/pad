def solution():
    """Joe and Adam built a garden wall with three courses of bricks. They realized the wall was too low and added 2 more courses. If each course of the wall had 400 bricks, and they took out half of the bricks in the last course to allow easy checkup of the garden, calculate the total number of bricks the wall has."""
    courses_initial = 3
    courses_added = 2
    bricks_per_course = 400
    bricks_in_last_course = bricks_per_course // 2
    total_courses = courses_initial + courses_added
    total_bricks = total_courses * bricks_per_course - bricks_per_course + bricks_in_last_course
    result = total_bricks
    return result

print(solution())