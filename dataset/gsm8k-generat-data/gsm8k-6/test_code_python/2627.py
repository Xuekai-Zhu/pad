def solution():
    # Calculate the total number of blocks used for the 5-level pyramid
    total_blocks = 9 + (9-2) + (7-2) + (5-2) + (3-2)  # the child has 9 blocks in the first row, and 2 less blocks in each subsequent row
    result = total_blocks
    return result

print(solution())