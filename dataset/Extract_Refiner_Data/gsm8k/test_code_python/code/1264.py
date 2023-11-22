def solution():
    
    # Define the number of blue blocks
    blue_blocks = 4

    # Calculate the number of yellow blocks
    yellow_blocks = blue_blocks * 2

    # Calculate the total number of blocks
    total_blocks = 32

    # Calculate the number of red blocks
    red_blocks = total_blocks - blue_blocks - yellow_blocks

    # Display the number of red blocks
    result = red_blocks
    return result

print(solution())