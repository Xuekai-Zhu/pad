def solution():
    # Calculate the total number of blocks Jess must walk
    total_blocks = 11 + 6 + 8  # Jess walks 11 blocks to the store, 6 blocks to the gallery, and 8 blocks to work
    remaining_blocks = total_blocks - 5  # Jess has already walked 5 blocks
    result = remaining_blocks
    return result

print(solution())