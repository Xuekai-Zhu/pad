def solution():
    """There are two ponds side by side in a park. Pond A has twice as many frogs as Pond B. If there are 32 frogs in Pond A, how many frogs are there in both ponds combined?"""
    # Define the number of frogs in Pond A
    frogs_pond_a = 32

    # Calculate the number of frogs in Pond B
    frogs_pond_b = frogs_pond_a / 2

    # Calculate the total number of frogs in both ponds
    total_frogs = frogs_pond_a + frogs_pond_b

    # return the result
    result = total_frogs
    return result

print(solution())