def solution():
    """A child is making a 5-level pyramid by stacking some blocks. In the first row, he has 9 blocks. For the next rows, he has 2 less than the blocks he has from its bottom row. How many blocks did he use in all?"""
    first_row_blocks = 9
    total_blocks = first_row_blocks
    for i in range(2, 6):
        row_blocks = first_row_blocks - (i - 1) * 2
        total_blocks += row_blocks * i

    result = total_blocks
    return result

print(solution())