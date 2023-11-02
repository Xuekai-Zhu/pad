def solution():
    """Alice wants 1000 folded paper cranes. She folds half by herself, and a friend folds a fifth of the remaining paper cranes for her. How many paper cranes does Alice still need to fold?"""
    total_cranes = 1000
    cranes_folded_by_alice = total_cranes / 2
    cranes_folded_by_friend = (total_cranes - cranes_folded_by_alice) / 5
    cranes_left_to_fold = total_cranes - cranes_folded_by_alice - cranes_folded_by_friend
    result = cranes_left_to_fold
    return result

print(solution())