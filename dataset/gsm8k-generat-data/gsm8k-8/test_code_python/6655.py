def solution():
    # Let x be the measure of the smallest angle
    x = 0
    # The largest angle is 5 times bigger than the smallest
    largest = 5 * x
    # The middle angle is 3 times bigger than the smallest
    middle = 3 * x
    # The sum of all angles in a triangle is 180 degrees
    total = x + largest + middle
    # Solve for x
    x = (180 - 0.5 * total) / 2
    result = x
    return result

print(solution())