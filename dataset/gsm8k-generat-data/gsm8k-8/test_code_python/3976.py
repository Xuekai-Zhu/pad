def solution():
    # Calculate the total number of blocks in the tower
    total_blocks = 54

    # Calculate the number of blocks removed in the first 5 rounds
    removed_blocks = 5 * 5

    # Calculate the number of blocks remaining after the first 5 rounds
    remaining_blocks = total_blocks - removed_blocks

    # Calculate the number of blocks removed by Jess's father in the sixth round
    father_removed = 1

    # Calculate the number of blocks remaining before Jess's turn
    remaining_blocks -= father_removed

    result = remaining_blocks
    return result

print(solution())