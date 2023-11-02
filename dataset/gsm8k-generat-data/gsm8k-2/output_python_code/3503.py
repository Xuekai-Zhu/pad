def solution():
    """Joe and Adam built a garden wall with three courses of bricks. They realized the wall was too low and added 2 more courses. If each course of the wall had 400 bricks, and they took out half of the bricks in the last course to allow easy checkup of the garden, calculate the total number of bricks the wall has."""
    brick_per_course = 400
    initial_courses = 3
    added_courses = 2
    total_courses = initial_courses + added_courses
    last_course_bricks = brick_per_course / 2
    total_bricks = (brick_per_course * initial_courses) + (brick_per_course * added_courses) + last_course_bricks
    result = total_bricks
    return result

print(solution())