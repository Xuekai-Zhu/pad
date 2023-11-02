def solution():
    # Calculate the total number of blocks removed in the previous 5 rounds
    blocks_removed = 5 * 5  # 5 players, 5 rounds

    # Calculate the total number of blocks remaining before Jess's turn
    blocks_remaining = 54 - blocks_removed - 1  # Jess's father removed one block in the sixth round

    result = blocks_remaining
    return result

print(solution())