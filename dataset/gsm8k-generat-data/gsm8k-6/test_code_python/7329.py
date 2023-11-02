def solution():
    # Calculate the area of the shoebox
    area_shoebox = 4 * 6

    # Calculate the area of the block
    area_block = 4 * 4

    # Calculate the area of the uncovered space
    area_uncovered = area_shoebox - area_block
    result = area_uncovered
    return result

print(solution())