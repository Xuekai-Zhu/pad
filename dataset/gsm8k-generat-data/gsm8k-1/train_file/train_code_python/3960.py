def solution():
    """Janet lives in a city built on a grid system. She walks 3 blocks north, then seven times as many blocks west. Then she turns around and walks 8 blocks south and twice as many blocks east in the direction of her home. If Janet can walk 2 blocks/minute, how long will it take her to get home?"""
    north_blocks = 3
    west_blocks = north_blocks * 7
    south_blocks = 8
    east_blocks = west_blocks * 2
    total_blocks = north_blocks + south_blocks + east_blocks
    time_in_minutes = total_blocks / 2
    result = time_in_minutes
    return result

print(solution())