def solution():
    """Emily has 6 marbles. Megan gives Emily double the number she has. Emily then gives Megan back half of her new total plus 1. How many marbles does Emily have now?"""
    emily_marbles = 6
    megan_marbles = 2 * emily_marbles
    emily_marbles = (emily_marbles + megan_marbles) / 2 + 1
    result = emily_marbles
    return result

print(solution())