def solution():
    oliver_speed = 40  # Oliver can read 40 pages in 1 hour
    lucy_speed = oliver_speed + 20  # Lucy can read 20 more pages than Oliver in 1 hour
    carter_speed = lucy_speed / 2  # Carter can read half as many pages as Lucy in 1 hour
    result = carter_speed
    return result

print(solution())