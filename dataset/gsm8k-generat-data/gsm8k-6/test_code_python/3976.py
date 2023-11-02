def solution():
    # Calculate the total number of blocks removed in the 6 rounds
    blocks_removed = 5 * 5 + 1  # 5 players, 5 rounds, and 1 block removed by Jess's father in the 6th round

    # Calculate the total number of blocks in the tower before Jess's turn
    total_blocks = blocks_removed + 1  # one block was removed by Jess before the tower fell

    result = total_blocks
    return result

print(solution())