def solution():
    """Joe and Adam built a garden wall with three courses of bricks.
    They realized the wall was too low and added 2 more courses.
    If each course of the wall had 400 bricks, and they took out half of
    the bricks in the last course to allow easy checkup of the garden,
    calculate the total number of bricks the wall has."""
    # Define the number of courses of bricks before and after adding more courses
    initial_courses = 3
    final_courses = 5

    # Define the number of bricks per course and the fraction of bricks taken out of the last course
    bricks_per_course = 400
    fraction_removed = 0.5

    # Calculate the total number of bricks in the wall
    total_bricks = (initial_courses + final_courses) * bricks_per_course - fraction_removed * bricks_per_course
    
    result = total_bricks
    return result

print(solution())