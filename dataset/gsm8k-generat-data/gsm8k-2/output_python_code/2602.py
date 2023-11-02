def solution():
    """Anna has 3 times as many toys as Mandy and 2 fewer toys than Amanda. If they have 142 toys all together, how many toys does Mandy have?"""
    total_toys = 142
    # Let Mandy have 'm' toys
    m = total_toys / 6
    # Anna has 3 times as many toys as Mandy
    a = 3 * m
    # Amanda has 2 more toys than Anna
    b = a + 2
    # Total number of toys
    total = m + a + b
    # Mandy's toys
    result = m
    return result

print(solution())