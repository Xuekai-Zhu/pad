def solution():
    """A child is making a 5-level pyramid by stacking some blocks. In the first row, he has 9 blocks. For the next rows, he has 2 less than the blocks he has from its bottom row. How many blocks did he use in all?"""
    # Define the number of blocks in the first row
    blocks_in_first_row = 9

    # Calculate the total number of blocks in the pyramid
    total_blocks = blocks_in_first_row + (blocks_in_first_row-2) + (blocks_in_first_row-4) + (blocks_in_first_row-6) + (blocks_in_first_row-8)

    # Display the total number of blocks
    result = total_blocks
    return result

print(solution())