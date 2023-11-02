def solution():
    """Carter can read half as many pages as Lucy in 1 hour. Lucy can read 20 more pages than Oliver in 1 hour. Oliver can read 40 pages. How many pages can Carter read in 1 hour?"""
    # Define Oliver's reading speed
    oliver_speed = 40

    # Define Lucy's reading speed
    lucy_speed = oliver_speed + 20

    # Define Carter's reading speed
    carter_speed = lucy_speed / 2

    result = carter_speed
    return result

print(solution())