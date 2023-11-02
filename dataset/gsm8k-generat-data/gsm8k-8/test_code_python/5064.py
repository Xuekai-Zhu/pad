def solution():
    # Calculate the total area of the courtyard
    area = 10 * 25

    # Calculate the total number of tiles needed
    total_tiles = area * 4

    # Calculate the number of green marble tiles needed
    green_tiles = int(total_tiles * 0.4)

    # Calculate the number of red tiles needed
    red_tiles = total_tiles - green_tiles

    # Calculate the total cost of the green tiles
    green_cost = green_tiles * 3

    # Calculate the total cost of the red tiles
    red_cost = red_tiles * 1.5

    # Calculate the total cost of all the tiles
    total_cost = green_cost + red_cost
    result = total_cost
    return result

print(solution())