def solution():
    """The three angles of a triangle add up to 180 degrees. The largest angle is 5 times bigger than the smallest. The middle angle is 3 times bigger than the smallest. How many degrees is the smallest angle?"""
    x = 1  # assume smallest angle is 1 degree
    largest_angle = 5 * x
    middle_angle = 3 * x
    smallest_angle = x
    total = largest_angle + middle_angle + smallest_angle
    while total != 180:  # adjust smallest angle until total equals 180
        x += 1
        largest_angle = 5 * x
        middle_angle = 3 * x
        smallest_angle = x
        total = largest_angle + middle_angle + smallest_angle

    result = smallest_angle
    return result

print(solution())