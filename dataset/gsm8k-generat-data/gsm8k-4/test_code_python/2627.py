def solution():
    """A child is making a 5-level pyramid by stacking some blocks. In the first row, he has 9 blocks. For the next rows, he has 2 less than the blocks he has from its bottom row. How many blocks did he use in all?"""
    # Define the number of rows and the number of blocks in the first row
    rows = 5
    first_row_blocks = 9

    # Calculate the total number of blocks used
    total_blocks = 0
    for i in range(rows):
        row_blocks = first_row_blocks - 2*i
        total_blocks += row_blocks*(i+1)

    result = total_blocks
    return result

print(solution())