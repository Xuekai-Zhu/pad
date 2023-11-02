def solution():
    total_cranes = 1000  # Alice wants 1000 folded paper cranes
    alice_cranes = total_cranes / 2  # Alice folds half by herself
    remaining_cranes = total_cranes - alice_cranes  # Alice needs to fold the remaining cranes
    friend_cranes = remaining_cranes / 5  # A friend folds a fifth of the remaining paper cranes
    alice_still_needs = remaining_cranes - friend_cranes  # Alice still needs to fold this many cranes
    result = alice_still_needs
    return result

print(solution())