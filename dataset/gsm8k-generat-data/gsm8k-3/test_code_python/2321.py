def solution():
    """Pete walked 5 blocks from his house to the bus garage in Houston. He rode the bus 20 blocks to the post office to get some stamps. Later, he came home the same way. How many blocks did Pete travel in all?"""
    # Define the number of blocks traveled on foot
    WALKING_BLOCKS = 5

    # Define the number of blocks traveled by bus
    BUS_BLOCKS = 20

    # Calculate the total number of blocks traveled
    total_blocks = 2 * (WALKING_BLOCKS + BUS_BLOCKS)

    # Display the total number of blocks traveled
    result = total_blocks
    return result

print(solution())