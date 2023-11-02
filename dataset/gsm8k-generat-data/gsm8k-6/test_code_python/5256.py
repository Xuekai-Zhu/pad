def solution():
    # Calculate the number of paper cranes Alice has folded by herself
    alice_folded = 1000 / 2

    # Calculate the number of paper cranes remaining to be folded
    remaining_cranes = 1000 - alice_folded

    # Calculate the number of paper cranes that Alice's friend folds
    friend_folded = remaining_cranes / 5

    # Calculate the number of paper cranes still needed to reach 1000
    still_needed = 1000 - alice_folded - friend_folded
    result = still_needed
    return result

print(solution())