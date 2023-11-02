def solution():
    """Alice wants 1000 folded paper cranes. She folds half by herself, and a friend folds a fifth of the remaining paper cranes for her. How many paper cranes does Alice still need to fold?"""
    total_cranes = 1000
    alice_cranes = total_cranes / 2
    remaining_cranes = total_cranes - alice_cranes
    friend_cranes = remaining_cranes / 5
    alice_still_needs = remaining_cranes - friend_cranes
    result = alice_still_needs
    return result

print(solution())