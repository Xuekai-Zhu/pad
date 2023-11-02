def solution():
    # Let x be the amount of money Susan had at first
    # She spent 1/5 of it in September, so she has 4/5 of it left
    # She spent 1/4 of the remaining amount in October, so she has 3/4 * 4/5 = 3/5 of it left
    # She spent $120 in November, so she has 3/5 * x - 120 = 540
    # Solving for x, we get...
    x = (540 + 120) / (3/5)
    result = x
    return result

print(solution())