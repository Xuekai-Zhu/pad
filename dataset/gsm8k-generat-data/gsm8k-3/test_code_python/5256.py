def solution():
    """Alice wants 1000 folded paper cranes. She folds half by herself, and a friend folds a fifth of the remaining paper cranes for her. How many paper cranes does Alice still need to fold?"""
    # Alice folds half, so she has 500 left to fold
    remaining_cranes = 500

    # Alice's friend folds a fifth of the remaining cranes, so she folds 1/5 * 500 = 100 cranes
    remaining_cranes -= 100

    # Alice still needs to fold the remaining cranes
    result = remaining_cranes
    return result

print(solution())