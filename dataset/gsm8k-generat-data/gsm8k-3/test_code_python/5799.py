def solution():
    """Trent walked 4 blocks from his house to the bus stop. He rode the bus 7 blocks to the library. Later, he came home the same way. How many blocks did Trent travel in all?"""
    # Define the number of blocks walked and ridden by bus
    BLOCKS_WALKED = 4
    BLOCKS_RIDDEN = 7

    # Calculate the total number of blocks traveled
    total_blocks = BLOCKS_WALKED + 2 * BLOCKS_RIDDEN

    # Display the total number of blocks traveled
    result = total_blocks
    return result

print(solution())