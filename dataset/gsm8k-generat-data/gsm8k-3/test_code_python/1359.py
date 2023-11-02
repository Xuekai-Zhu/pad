def solution():
    """Carter can read half as many pages as Lucy in 1 hour. Lucy can read 20 more pages than Oliver in 1 hour. Oliver can read 40 pages. How many pages can Carter read in 1 hour?"""
    # Define Oliver's reading speed in pages per hour
    OLIVER_SPEED = 40

    # Calculate Lucy's reading speed in pages per hour
    lucy_speed = OLIVER_SPEED + 20

    # Calculate Carter's reading speed in pages per hour
    carter_speed = lucy_speed / 2

    # Display Carter's reading speed
    result = carter_speed
    return result

print(solution())