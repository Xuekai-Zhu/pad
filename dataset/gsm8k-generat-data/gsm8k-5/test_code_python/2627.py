def solution():
    bottom_row_blocks = 9  # The first row has 9 blocks
    total_blocks = bottom_row_blocks  # Count the blocks in the bottom row

    for level in range(2, 6):  # Loop through the remaining 4 levels
        blocks_in_row = bottom_row_blocks - 2*(level-1)  # Calculate the number of blocks in this level
        total_blocks += blocks_in_row  # Add the blocks in this level to the total

    result = total_blocks
    return result

print(solution())