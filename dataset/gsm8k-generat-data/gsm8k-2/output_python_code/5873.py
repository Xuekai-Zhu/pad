def solution():
    """There are two ponds side by side in a park. Pond A has twice as many frogs as Pond B. If there are 32 frogs in Pond A, how many frogs are there in both ponds combined?"""
    pond_a_frogs = 32
    pond_b_frogs = pond_a_frogs / 2
    total_frogs = pond_a_frogs + pond_b_frogs
    result = total_frogs
    return result

print(solution())