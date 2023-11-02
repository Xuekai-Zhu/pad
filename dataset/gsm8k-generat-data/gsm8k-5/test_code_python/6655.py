def solution():
    # Let x be the measure of the smallest angle
    x = 0

    # The largest angle is 5 times bigger than the smallest
    largest_angle = 5 * x

    # The middle angle is 3 times bigger than the smallest
    middle_angle = 3 * x

    # The sum of the three angles is 180 degrees
    total_angle = x + largest_angle + middle_angle

    # Solve for x
    x = (180 - total_angle) / 9

    result = x
    return result

print(solution())