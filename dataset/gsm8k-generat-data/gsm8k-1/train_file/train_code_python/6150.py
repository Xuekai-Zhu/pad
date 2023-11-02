def solution():
    """Justin can run 2 blocks in 1.5 minutes. If he is 8 blocks from home, in how many minutes can he run home?"""
    blocks_per_time = 2/1.5
    blocks_home = 8
    time_home = blocks_home / blocks_per_time
    result = time_home
    return result

print(solution())