def solution():
    """A child is making a 5-level pyramid by stacking some blocks. In the first row, he has 9 blocks. For the next rows, he has 2 less than the blocks he has from its bottom row. How many blocks did he use in all?"""
    blocks = 9
    total_blocks = 9
    for i in range(1, 5):
        blocks -= 2
        total_blocks += blocks * 2
    
    result = total_blocks
    return result

print(solution())