def solution():
    """Janet lives in a city built on a grid system. She walks 3 blocks north, then seven times as many blocks west. Then she turns around and walks 8 blocks south and twice as many blocks east in the direction of her home. If Janet can walk 2 blocks/minute, how long will it take her to get home?"""
    
    # Define the number of blocks Janet walks in each direction
    north_blocks = 3
    west_blocks = 7 * north_blocks
    south_blocks = 8
    east_blocks = 2 * south_blocks

    # Calculate the total number of blocks Janet walks
    total_blocks = north_blocks + west_blocks + south_blocks + east_blocks

    # Calculate the time it takes Janet to walk the total distance
    time = total_blocks / 2

    # Return the result
    result = time
    return result

print(solution())