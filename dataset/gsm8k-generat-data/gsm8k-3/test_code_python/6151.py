def solution():
    """Justin can run 2 blocks in 1.5 minutes. If he is 8 blocks from home, in how many minutes can he run home?"""
    # Define Justin's running speed in blocks per minute
    BLOCKS_PER_MINUTE = 2 / 1.5

    # Define the distance Justin needs to travel
    distance = 8

    # Calculate the time it will take Justin to run home
    time = distance / BLOCKS_PER_MINUTE

    # Display the time it will take Justin to run home
    result = time
    return result

print(solution())