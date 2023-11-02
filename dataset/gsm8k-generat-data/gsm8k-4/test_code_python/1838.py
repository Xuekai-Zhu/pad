def solution():
    """Jacob loves to build things. In Jacob's toy bin there are 18 red blocks. There are 7 more yellow blocks than red blocks. There are also 14 more blue blocks than red blocks. How many blocks are there in all?"""
    # Define the number of red blocks
    red_blocks = 18

    # Calculate the number of yellow blocks (7 more than red blocks)
    yellow_blocks = red_blocks + 7

    # Calculate the number of blue blocks (14 more than red blocks)
    blue_blocks = red_blocks + 14

    # Calculate the total number of blocks
    total_blocks = red_blocks + yellow_blocks + blue_blocks

    # Return the result
    result = total_blocks
    return result

print(solution())