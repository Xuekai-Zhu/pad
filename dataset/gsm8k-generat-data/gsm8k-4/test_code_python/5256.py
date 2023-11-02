def solution():
    """Alice wants 1000 folded paper cranes. She folds half by herself, and a friend folds a fifth of the remaining paper cranes for her. How many paper cranes does Alice still need to fold?"""
    # Define the total number of paper cranes Alice wants
    total_cranes = 1000

    # Calculate the number of paper cranes Alice folds herself
    alice_cranes = total_cranes / 2

    # Calculate the remaining number of paper cranes
    remaining_cranes = total_cranes - alice_cranes

    # Calculate the number of paper cranes Alice's friend folds
    friend_cranes = remaining_cranes / 5

    # Calculate the number of paper cranes Alice still needs to fold
    still_needed = remaining_cranes - friend_cranes

    # return the result
    result = still_needed
    return result

print(solution())