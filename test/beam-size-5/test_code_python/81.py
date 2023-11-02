def solution():
    
    # Define the number of blocks per shirt
    BLOCKS_PER_SHIRT = 4

    # Define the age of Gene's vacations
    VACATION_AGE = 23

    # Calculate the number of blocks Gene has been vacationing
    vacation_blocks = VACATION_AGE * 4

    # Calculate the number of blocks Gene has left
    blocks_left = 34 - vacation_blocks - vacation_blocks

    # Calculate the total number of blocks
    total_blocks = blocks_left * BLOCKS_PER_SHIRT

    # Display the total number of blocks
    result = total_blocks
    return result

print(solution())