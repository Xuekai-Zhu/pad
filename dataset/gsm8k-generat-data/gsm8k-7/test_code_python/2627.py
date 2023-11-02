def solution():
    num_blocks = 0
    num_levels = 5
    bottom_row = 9

    # Calculate the number of blocks in each row and add them up
    for i in range(num_levels):
        num_blocks += bottom_row - 2*i
    result = num_blocks
    return result

print(solution())