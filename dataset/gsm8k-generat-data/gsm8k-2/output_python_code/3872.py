def solution():
    """Moses and Tiffany want to see who is faster. But instead of a race, they just start running down the block.
    Tiffany runs 6 blocks in 3 minutes. Moses runs 12 blocks in 8 minutes. What is the speed (defined as blocks per minute)
    of the runner with the higher average speed?"""
    tiffany_speed = 6 / 3  # blocks per minute
    moses_speed = 12 / 8  # blocks per minute
    if tiffany_speed > moses_speed:
        result = tiffany_speed
    else:
        result = moses_speed
    return result

print(solution())