def solution():
    """Janet lives in a city built on a grid system. She walks 3 blocks north, then seven times as many blocks west. Then she turns around and walks 8 blocks south and twice as many blocks east in the direction of her home. If Janet can walk 2 blocks/minute, how long will it take her to get home?"""
    # Calculate the total distance north to south
    total_distance_north_south = 3 + 8

    # Calculate the total distance east to west
    total_distance_east_west = 7 * 3 + 2 * 7 * 3

    # Calculate the total distance Janet must travel
    total_distance = (total_distance_north_south ** 2 + total_distance_east_west ** 2) ** 0.5

    # Calculate the time it will take Janet to get home
    time = total_distance / 2

    # Display the time it will take Janet to get home
    result = time
    return result

print(solution())