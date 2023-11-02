def solution():
    """The three angles of a triangle add up to 180 degrees. The largest angle is 5 times bigger than the smallest. The middle angle is 3 times bigger than the smallest. How many degrees is the smallest angle?"""
    # Let x be the smallest angle
    x = 0

    # The largest angle is 5 times bigger than the smallest
    largest = 5*x

    # The middle angle is 3 times bigger than the smallest
    middle = 3*x

    # The sum of all three angles is 180 degrees
    sum_of_angles = x + largest + middle

    # Solve for x
    x = (180 - sum_of_angles)/(-7)

    # Return the value of the smallest angle
    result = x
    return result

print(solution())