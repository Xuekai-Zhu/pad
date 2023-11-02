def solution():
    # Define the tile painting rates in tiles per minute
    don_rate = 3
    ken_rate = don_rate + 2
    laura_rate = ken_rate * 2
    kim_rate = laura_rate - 3

    # Calculate the number of tiles painted by each person in 15 minutes
    don_tiles = don_rate * 15
    ken_tiles = ken_rate * 15
    laura_tiles = laura_rate * 15
    kim_tiles = kim_rate * 15

    # Calculate the total number of tiles painted
    total_tiles = don_tiles + ken_tiles + laura_tiles + kim_tiles

    result = total_tiles
    return result

print(solution())