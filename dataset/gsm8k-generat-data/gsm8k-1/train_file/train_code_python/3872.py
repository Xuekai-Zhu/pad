def solution():
    """Moses and Tiffany want to see who is faster. But instead of a race, they just start running down the block. Tiffany runs 6 blocks in 3 minutes. Moses runs 12 blocks in 8 minutes. What is the speed (defined as blocks per minute) of the runner with the higher average speed?"""
    tiffany_blocks = 6
    tiffany_time = 3
    moses_blocks = 12
    moses_time = 8
    tiffany_speed = tiffany_blocks / tiffany_time
    moses_speed = moses_blocks / moses_time
    result = max(tiffany_speed, moses_speed)
    return result

print(solution())