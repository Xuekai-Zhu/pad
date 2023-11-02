def solution():
    # Calculate the total number of blocks of stone
    total_blocks = 96

    # Calculate the number of steps in the stairs
    total_steps = total_blocks / 3

    # Calculate the number of levels in the tower
    levels = total_steps / 8
    result = levels
    return result

print(solution())