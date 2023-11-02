def solution():
    """Clara is climbing to the top of a historical tower with stone stairs. Each level has eight huge steps in the stairs. Every step is made up of three massive blocks of stone. By the time she reaches the top, she has climbed past 96 blocks of stone. How many levels are there in the tower?"""
    # Define the number of blocks in each step and the number of steps in each level
    BLOCKS_PER_STEP = 3
    STEPS_PER_LEVEL = 8

    # Calculate the total number of steps taken by Clara
    total_steps = 96 // BLOCKS_PER_STEP

    # Calculate the number of levels in the tower
    levels = total_steps // STEPS_PER_LEVEL

    # Display the number of levels
    result = levels
    return result

print(solution())