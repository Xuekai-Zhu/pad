def solution():
    """Jacob loves to build things. In Jacob's toy bin there are 18 red blocks. There are 7 more yellow blocks than red blocks. There are also 14 more blue blocks than red blocks. How many blocks are there in all?"""
    # Define the number of red blocks
    RED_BLOCKS = 18

    # Calculate the number of yellow blocks
    YELLOW_BLOCKS = RED_BLOCKS + 7

    # Calculate the number of blue blocks
    BLUE_BLOCKS = RED_BLOCKS + 14

    # Calculate the total number of blocks
    total_blocks = RED_BLOCKS + YELLOW_BLOCKS + BLUE_BLOCKS

    # Display the total number of blocks
    result = total_blocks
    return result

print(solution())