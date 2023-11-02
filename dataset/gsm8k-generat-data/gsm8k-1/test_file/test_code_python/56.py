def solution():
    """A basket contains 25 oranges among which 1 is bad, 20% are unripe, 2 are sour and the rest are good. How many oranges are good?"""
    total_oranges = 25
    bad_oranges = 1
    unripe_oranges = int(total_oranges * 0.2)
    sour_oranges = 2
    good_oranges = total_oranges - bad_oranges - unripe_oranges - sour_oranges
    result = good_oranges
    return result

print(solution())