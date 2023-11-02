def solution():
    """There are two ponds side by side in a park. Pond A has twice as many frogs as Pond B. If there are 32 frogs in Pond A, how many frogs are there in both ponds combined?"""
    frogs_in_pond_a = 32
    frogs_in_pond_b = frogs_in_pond_a / 2
    total_frogs = frogs_in_pond_a + frogs_in_pond_b
    result = total_frogs
    return result

print(solution())