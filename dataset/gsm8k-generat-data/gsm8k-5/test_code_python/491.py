def solution():
    total_blocks = 11 + 6 + 8  # Jess has to walk a total of 11+6+8 = 25 blocks
    blocks_walked = 5  # Jess has already walked 5 blocks
    blocks_remaining = total_blocks - blocks_walked  # Jess has to walk the remaining blocks to get to work
    result = blocks_remaining
    return result

print(solution())