def solution():
    """Clara is climbing to the top of a historical tower with stone stairs. Each level has eight huge steps in the stairs. Every step is made up of three massive blocks of stone. By the time she reaches the top, she has climbed past 96 blocks of stone. How many levels are there in the tower?"""
    # Define the number of blocks per step and the number of steps per level
    blocks_per_step = 3
    steps_per_level = 8

    # Calculate the total number of blocks climbed
    total_blocks = 96

    # Calculate the number of levels
    levels = total_blocks // (blocks_per_step * steps_per_level)

    # return the result
    result = levels
    return result

print(solution())