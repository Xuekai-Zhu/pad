def solution():
    """Justin can run 2 blocks in 1.5 minutes. If he is 8 blocks from home, in how many minutes can he run home?"""
    blocks_per_min = 2 / 1.5
    blocks_to_home = 8
    time_to_home = blocks_to_home / blocks_per_min
    result = time_to_home
    return result

print(solution())