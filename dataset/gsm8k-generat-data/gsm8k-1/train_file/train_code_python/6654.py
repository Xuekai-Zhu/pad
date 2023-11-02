def solution():
    """The three angles of a triangle add up to 180 degrees. The largest angle is 5 times bigger than the smallest. The middle angle is 3 times bigger than the smallest. How many degrees is the smallest angle?"""
    smallest_angle = x
    middle_angle = 3 * x
    largest_angle = 5 * x
    total = smallest_angle + middle_angle + largest_angle
    sum_of_angles = 180
    smallest_angle = (sum_of_angles - (middle_angle + largest_angle)) / 3
    result = smallest_angle
    return result

print(solution())