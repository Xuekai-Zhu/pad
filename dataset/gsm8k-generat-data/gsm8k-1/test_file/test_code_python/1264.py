def solution():
    """A tower is made out of 4 blue blocks, twice as many yellow blocks, and an unknown number of red blocks. If there are 32 blocks in the tower in total, how many red blocks are there?"""
    blue_blocks = 4
    yellow_blocks = blue_blocks * 2
    total_blocks = 32
    red_blocks = total_blocks - (blue_blocks + yellow_blocks)
    result = red_blocks
    return result

print(solution())