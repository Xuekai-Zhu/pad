def solution():
    """Annie walked 5 blocks from her house to the bus stop. She rode the bus 7 blocks to the coffee shop. Later, she came home the same way. How many blocks did Annie travel in all?"""
    # Define the number of blocks Annie walked and rode on the bus
    walked_blocks = 5
    bus_blocks = 7

    # Calculate the total number of blocks Annie traveled
    total_blocks = (walked_blocks + bus_blocks) * 2

    # return the result
    result = total_blocks
    return result

print(solution())