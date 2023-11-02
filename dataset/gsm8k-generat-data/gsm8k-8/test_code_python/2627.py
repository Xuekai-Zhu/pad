def solution():
    # Define the number of blocks in the first row
    first_row_blocks = 9

    # Calculate the total number of blocks based on the pattern
    total_blocks = first_row_blocks + (first_row_blocks - 2) + (first_row_blocks - 4) + (first_row_blocks - 6) + (first_row_blocks - 8)

    result = total_blocks
    return result

print(solution())