def solution():
    # Calculate the area of the shoebox
    shoebox_area = 4 * 6

    # Calculate the area of the square block
    block_area = 4 * 4

    # Calculate the area of the uncovered space
    uncovered_area = shoebox_area - block_area
    result = uncovered_area
    return result

print(solution())