def solution():
    # Define the number of red blocks
    red_blocks = 18

    # Calculate the number of yellow blocks and blue blocks
    yellow_blocks = red_blocks + 7
    blue_blocks = red_blocks + 14

    # Calculate the total number of blocks
    total_blocks = red_blocks + yellow_blocks + blue_blocks
    result = total_blocks
    return result

print(solution())