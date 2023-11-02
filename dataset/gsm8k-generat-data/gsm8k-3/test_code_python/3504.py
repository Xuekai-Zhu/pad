def solution():
    """Joe and Adam built a garden wall with three courses of bricks. They realized the wall was too low and added 2 more courses. If each course of the wall had 400 bricks, and they took out half of the bricks in the last course to allow easy checkup of the garden, calculate the total number of bricks the wall has."""
    # Define the number of courses of the wall
    num_courses = 5

    # Define the number of bricks per course
    bricks_per_course = 400

    # Calculate the total number of bricks
    total_bricks = (num_courses - 1) * bricks_per_course + (bricks_per_course / 2)

    # Display the total number of bricks
    result = total_bricks
    return result

print(solution())