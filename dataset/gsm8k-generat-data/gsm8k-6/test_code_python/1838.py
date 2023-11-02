def solution():
    red_blocks = 18  # number of red blocks
    yellow_blocks = red_blocks + 7  # number of yellow blocks
    blue_blocks = red_blocks + 14  # number of blue blocks

    # Calculate the total number of blocks
    total_blocks = red_blocks + yellow_blocks + blue_blocks
    result = total_blocks
    return result

print(solution())