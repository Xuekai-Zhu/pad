def solution():
    num_red_blocks = 18

    # Calculate the number of yellow blocks
    num_yellow_blocks = num_red_blocks + 7

    # Calculate the number of blue blocks
    num_blue_blocks = num_red_blocks + 14

    # Calculate the total number of blocks
    total_blocks = num_red_blocks + num_yellow_blocks + num_blue_blocks
    result = total_blocks
    return result

print(solution())