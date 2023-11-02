def solution():
    bricks_per_course = 10  # Each course has 10 bricks
    total_courses = 6  # The mason has to build 6 courses per wall
    total_walls = 4  # The mason has to build 4 walls

    # Calculate the total number of bricks used
    total_bricks = bricks_per_course * total_courses * total_walls

    # Calculate the number of bricks not used in the last wall
    unused_bricks = 2 * bricks_per_course

    # Subtract the unused bricks from the total
    final_total_bricks = total_bricks - unused_bricks
    result = final_total_bricks
    return result

print(solution())