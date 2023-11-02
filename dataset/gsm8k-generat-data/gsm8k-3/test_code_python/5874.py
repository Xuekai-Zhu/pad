def solution():
    """There are two ponds side by side in a park. Pond A has twice as many frogs as Pond B. If there are 32 frogs in Pond A, how many frogs are there in both ponds combined?"""
    # Calculate the number of frogs in Pond B
    frogs_b = 32/2

    # Calculate the total number of frogs in both ponds
    total_frogs = 32 + frogs_b

    # Display the total number of frogs
    result = total_frogs
    return result

print(solution())